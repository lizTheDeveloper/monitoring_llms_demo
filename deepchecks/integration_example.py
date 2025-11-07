"""
End-to-End Integration Example for DeepChecks.

This script demonstrates how to integrate DeepChecks into a complete
monitoring pipeline, including data validation, model evaluation, and alerting.
"""

import logging
from datetime import datetime
from pathlib import Path

import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import (
    data_integrity,
    model_evaluation,
    train_test_validation,
)
from monitoring_dashboard import AlertConfig, MonitoringDashboard
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MonitoringPipeline:
    """Complete monitoring pipeline integrating all DeepChecks components."""
    
    def __init__(self, alert_config_path: str = 'alert_config.json'):
        """Initialize monitoring pipeline."""
        self.alert_config = AlertConfig(alert_config_path)
        self.dashboard = MonitoringDashboard(self.alert_config)
        self.results_dir = Path('results')
        self.results_dir.mkdir(exist_ok=True)
    
    def validate_data_quality(self, train_data: pd.DataFrame, 
                             test_data: pd.DataFrame, label_col: str):
        """
        Validate data quality using DeepChecks.
        
        Args:
            train_data: Training dataset
            test_data: Test dataset
            label_col: Name of the label column
            
        Returns:
            SuiteResult from data integrity checks
        """
        logger.info("Step 1: Validating data quality...")
        
        train_dataset = Dataset(train_data, label=label_col, cat_features=[])
        test_dataset = Dataset(test_data, label=label_col, cat_features=[])
        
        suite = data_integrity()
        result = suite.run(train_dataset=train_dataset, test_dataset=test_dataset)
        
        # Analyze and track
        self.dashboard.analyze_result(result, 'data_integrity')
        
        # Save report
        report_path = self.results_dir / f'data_integrity_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        result.save_as_html(str(report_path))
        logger.info(f"Data integrity report saved to {report_path}")
        
        return result
    
    def validate_data_drift(self, train_data: pd.DataFrame, 
                           test_data: pd.DataFrame, label_col: str):
        """
        Validate data drift between train and test sets.
        
        Args:
            train_data: Training dataset
            test_data: Test dataset
            label_col: Name of the label column
            
        Returns:
            SuiteResult from train-test validation
        """
        logger.info("Step 2: Validating data drift...")
        
        train_dataset = Dataset(train_data, label=label_col, cat_features=[])
        test_dataset = Dataset(test_data, label=label_col, cat_features=[])
        
        suite = train_test_validation()
        result = suite.run(train_dataset=train_dataset, test_dataset=test_dataset)
        
        # Analyze and track
        self.dashboard.analyze_result(result, 'train_test_validation')
        
        # Save report
        report_path = self.results_dir / f'data_drift_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        result.save_as_html(str(report_path))
        logger.info(f"Data drift report saved to {report_path}")
        
        return result
    
    def evaluate_model(self, train_data: pd.DataFrame, test_data: pd.DataFrame,
                      model, label_col: str):
        """
        Evaluate model performance.
        
        Args:
            train_data: Training dataset
            test_data: Test dataset
            model: Trained model
            label_col: Name of the label column
            
        Returns:
            SuiteResult from model evaluation
        """
        logger.info("Step 3: Evaluating model performance...")
        
        train_dataset = Dataset(train_data, label=label_col, cat_features=[])
        test_dataset = Dataset(test_data, label=label_col, cat_features=[])
        
        suite = model_evaluation()
        result = suite.run(
            train_dataset=train_dataset,
            test_dataset=test_dataset,
            model=model
        )
        
        # Analyze and track
        self.dashboard.analyze_result(result, 'model_evaluation')
        
        # Save report
        report_path = self.results_dir / f'model_evaluation_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        result.save_as_html(str(report_path))
        logger.info(f"Model evaluation report saved to {report_path}")
        
        return result
    
    def run_complete_pipeline(self, train_data: pd.DataFrame, 
                              test_data: pd.DataFrame, model, label_col: str):
        """
        Run complete monitoring pipeline.
        
        Args:
            train_data: Training dataset
            test_data: Test dataset
            model: Trained model
            label_col: Name of the label column
            
        Returns:
            Dictionary with all results and alerts
        """
        logger.info("=" * 80)
        logger.info("Starting Complete Monitoring Pipeline")
        logger.info("=" * 80)
        
        # Step 1: Data quality validation
        integrity_result = self.validate_data_quality(train_data, test_data, label_col)
        
        # Step 2: Data drift validation
        drift_result = self.validate_data_drift(train_data, test_data, label_col)
        
        # Step 3: Model evaluation
        evaluation_result = self.evaluate_model(train_data, test_data, model, label_col)
        
        # Generate and save reports
        logger.info("\nGenerating monitoring dashboard...")
        self.dashboard.save_reports()
        self.dashboard.print_dashboard()
        
        # Return summary
        return {
            'integrity_result': integrity_result,
            'drift_result': drift_result,
            'evaluation_result': evaluation_result,
            'alerts': self.dashboard.alerts,
            'summary': self.dashboard.generate_summary_report()
        }


def main():
    """Example usage of the complete monitoring pipeline."""
    # Create sample data
    from sklearn.datasets import make_classification
    
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
    
    # Split data
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df['target']
    )
    
    # Train model
    train_features = train_df.drop('target', axis=1)
    train_labels = train_df['target']
    test_features = test_df.drop('target', axis=1)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(train_features, train_labels)
    logger.info("Model trained successfully")
    
    # Initialize and run pipeline
    pipeline = MonitoringPipeline()
    results = pipeline.run_complete_pipeline(
        train_df, test_df, model, 'target'
    )
    
    logger.info("\n" + "=" * 80)
    logger.info("Pipeline completed successfully")
    logger.info("=" * 80)
    
    # Check for critical alerts
    critical_alerts = [a for a in results['alerts'] if a['level'] == 'critical']
    if critical_alerts:
        logger.error(f"WARNING: {len(critical_alerts)} critical alerts detected!")
        return 1
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())

