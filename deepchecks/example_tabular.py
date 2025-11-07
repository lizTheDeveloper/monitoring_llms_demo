"""
Example DeepChecks implementation for tabular data validation.

This script demonstrates how to use DeepChecks to validate:
- Data integrity
- Train-test split
- Model performance
"""

import logging
from pathlib import Path

import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import (
    data_integrity,
    model_evaluation,
    train_test_validation,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_sample_data():
    """Load sample data for demonstration."""
    # Using a simple synthetic dataset
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
    
    return df


def run_data_integrity_checks(train_data, test_data):
    """Run data integrity checks on training and test datasets."""
    logger.info("Running data integrity checks...")
    
    train_dataset = Dataset(
        train_data,
        label='target',
        cat_features=[]
    )
    test_dataset = Dataset(
        test_data,
        label='target',
        cat_features=[]
    )
    
    suite = data_integrity()
    result = suite.run(train_dataset=train_dataset, test_dataset=test_dataset)
    
    return result


def run_train_test_validation(train_data, test_data):
    """Run train-test validation checks."""
    logger.info("Running train-test validation checks...")
    
    train_dataset = Dataset(
        train_data,
        label='target',
        cat_features=[]
    )
    test_dataset = Dataset(
        test_data,
        label='target',
        cat_features=[]
    )
    
    suite = train_test_validation()
    result = suite.run(train_dataset=train_dataset, test_dataset=test_dataset)
    
    return result


def run_model_evaluation(train_data, test_data, model):
    """Run model evaluation checks."""
    logger.info("Running model evaluation checks...")
    
    train_dataset = Dataset(
        train_data,
        label='target',
        cat_features=[]
    )
    test_dataset = Dataset(
        test_data,
        label='target',
        cat_features=[]
    )
    
    suite = model_evaluation()
    result = suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset,
        model=model
    )
    
    return result


def main():
    """Main execution function."""
    logger.info("Starting DeepChecks validation pipeline...")
    
    # Load data
    df = load_sample_data()
    logger.info(f"Loaded dataset with shape: {df.shape}")
    
    # Split data
    train_df, test_df = train_test_split(
        df,
        test_size=0.2,
        random_state=42,
        stratify=df['target']
    )
    logger.info(f"Train set shape: {train_df.shape}, Test set shape: {test_df.shape}")
    
    # Prepare features and labels
    train_features = train_df.drop('target', axis=1)
    train_labels = train_df['target']
    test_features = test_df.drop('target', axis=1)
    test_labels = test_df['target']
    
    # Run data integrity checks
    integrity_result = run_data_integrity_checks(train_df, test_df)
    logger.info("Data integrity checks completed")
    
    # Run train-test validation
    validation_result = run_train_test_validation(train_df, test_df)
    logger.info("Train-test validation checks completed")
    
    # Train a simple model
    logger.info("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(train_features, train_labels)
    logger.info("Model training completed")
    
    # Run model evaluation
    evaluation_result = run_model_evaluation(train_df, test_df, model)
    logger.info("Model evaluation checks completed")
    
    # Save results
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    
    integrity_result.save_as_html(str(output_dir / 'data_integrity_report.html'))
    validation_result.save_as_html(str(output_dir / 'train_test_validation_report.html'))
    evaluation_result.save_as_html(str(output_dir / 'model_evaluation_report.html'))
    
    logger.info(f"Results saved to {output_dir}/")
    logger.info("DeepChecks validation pipeline completed successfully")
    
    # Display results summary
    print("\n" + "="*50)
    print("DATA INTEGRITY SUMMARY")
    print("="*50)
    print(integrity_result)
    
    print("\n" + "="*50)
    print("TRAIN-TEST VALIDATION SUMMARY")
    print("="*50)
    print(validation_result)
    
    print("\n" + "="*50)
    print("MODEL EVALUATION SUMMARY")
    print("="*50)
    print(evaluation_result)


if __name__ == '__main__':
    main()

