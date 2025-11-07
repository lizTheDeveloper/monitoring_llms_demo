"""
Automated Monitoring Workflow for DeepChecks.

This script provides automated monitoring workflows that can be scheduled
for regular data quality and model performance checks.
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import (
    data_integrity,
    model_evaluation,
    train_test_validation,
)
from monitoring_dashboard import MonitoringDashboard
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('monitoring.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def load_data_from_file(data_path: str) -> tuple:
    """Load data from CSV file."""
    try:
        df = pd.read_csv(data_path)
        logger.info(f"Loaded data from {data_path}: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data from {data_path}: {e}")
        raise


def create_sample_data():
    """Create sample data for demonstration."""
    from sklearn.datasets import make_classification
    import pandas as pd
    
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        n_classes=2,
        random_state=42
    )
    
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
    df['target'] = y
    
    return df


def run_automated_validation(data_path: Optional[str] = None, 
                            include_model_eval: bool = True):
    """
    Run automated validation workflow.
    
    Args:
        data_path: Path to CSV file with data (optional, uses sample if not provided)
        include_model_eval: Whether to include model evaluation checks
    """
    logger.info("=" * 80)
    logger.info("Starting Automated DeepChecks Validation")
    logger.info("=" * 80)
    
    # Initialize dashboard
    dashboard = MonitoringDashboard()
    
    # Load data
    if data_path and Path(data_path).exists():
        df = load_data_from_file(data_path)
    else:
        logger.info("No data file provided, using sample data")
        df = create_sample_data()
    
    # Split data
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df['target'] if 'target' in df.columns else None
    )
    
    logger.info(f"Train set: {train_df.shape}, Test set: {test_df.shape}")
    
    # Prepare datasets
    label_col = 'target' if 'target' in train_df.columns else train_df.columns[-1]
    train_dataset = Dataset(train_df, label=label_col, cat_features=[])
    test_dataset = Dataset(test_df, label=label_col, cat_features=[])
    
    # Run data integrity checks
    logger.info("\nRunning data integrity checks...")
    integrity_suite = data_integrity()
    integrity_result = integrity_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    dashboard.analyze_result(integrity_result, 'data_integrity')
    integrity_result.save_as_html('results/data_integrity_report.html')
    
    # Run train-test validation
    logger.info("\nRunning train-test validation...")
    validation_suite = train_test_validation()
    validation_result = validation_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    dashboard.analyze_result(validation_result, 'train_test_validation')
    validation_result.save_as_html('results/train_test_validation_report.html')
    
    # Run model evaluation if requested
    if include_model_eval:
        logger.info("\nRunning model evaluation...")
        train_features = train_df.drop(label_col, axis=1)
        train_labels = train_df[label_col]
        test_features = test_df.drop(label_col, axis=1)
        
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(train_features, train_labels)
        logger.info("Model trained successfully")
        
        evaluation_suite = model_evaluation()
        evaluation_result = evaluation_suite.run(
            train_dataset=train_dataset,
            test_dataset=test_dataset,
            model=model
        )
        dashboard.analyze_result(evaluation_result, 'model_evaluation')
        evaluation_result.save_as_html('results/model_evaluation_report.html')
    
    # Save dashboard reports
    logger.info("\nGenerating monitoring reports...")
    dashboard.save_reports()
    dashboard.print_dashboard()
    
    logger.info("\n" + "=" * 80)
    logger.info("Automated validation completed successfully")
    logger.info("=" * 80)
    
    # Return exit code based on alerts
    critical_alerts = [a for a in dashboard.alerts if a['level'] == 'critical']
    if critical_alerts:
        logger.error(f"CRITICAL: {len(critical_alerts)} critical alerts detected!")
        return 1
    
    return 0


def main():
    """Main entry point for automated monitoring."""
    parser = argparse.ArgumentParser(
        description='Automated DeepChecks monitoring workflow'
    )
    parser.add_argument(
        '--data',
        type=str,
        help='Path to CSV file with data (optional, uses sample if not provided)'
    )
    parser.add_argument(
        '--skip-model-eval',
        action='store_true',
        help='Skip model evaluation checks (faster for data-only validation)'
    )
    parser.add_argument(
        '--output-dir',
        type=str,
        default='results',
        help='Output directory for reports (default: results)'
    )
    
    args = parser.parse_args()
    
    # Set output directory
    Path(args.output_dir).mkdir(exist_ok=True)
    Path('monitoring_results').mkdir(exist_ok=True)
    
    # Run validation
    exit_code = run_automated_validation(
        data_path=args.data,
        include_model_eval=not args.skip_model_eval
    )
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()

