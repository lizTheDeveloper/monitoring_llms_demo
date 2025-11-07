"""
DeepChecks validation for structured data used by LLM systems.

This script demonstrates how DeepChecks can be used to validate:
- Structured data used in RAG systems
- Training datasets for LLM fine-tuning
- Data quality in production LLM pipelines
- Data drift detection for LLM inputs

Note: DeepChecks is designed for tabular/structured data validation.
For LLM-specific metrics (toxicity, hallucination, faithfulness), use DeepEval or RAGAs.
"""

import logging
from pathlib import Path

import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import (
    data_integrity,
    train_test_validation,
)
from sklearn.model_selection import train_test_split

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_rag_metadata_example():
    """
    Create example structured metadata for a RAG system.
    
    In a real RAG system, this might be:
    - Document embeddings metadata
    - Chunk quality scores
    - Source document information
    - Retrieval performance metrics
    """
    data = {
        'document_id': [f'doc_{i}' for i in range(1000)],
        'chunk_index': [i % 10 for i in range(1000)],
        'chunk_length': [100 + (i % 500) for i in range(1000)],
        'embedding_dim': [768] * 1000,
        'source_type': ['pdf', 'web', 'database'] * 333 + ['pdf'],
        'quality_score': [0.7 + (i % 30) / 100 for i in range(1000)],
        'has_citations': [i % 2 == 0 for i in range(1000)],
        'retrieval_count': [i % 20 for i in range(1000)],
    }
    return pd.DataFrame(data)


def create_training_data_example():
    """
    Create example structured training data metadata.
    
    In LLM fine-tuning, this might track:
    - Training example quality
    - Label distribution
    - Data source information
    - Annotation quality scores
    """
    data = {
        'example_id': [f'ex_{i}' for i in range(2000)],
        'input_length': [50 + (i % 500) for i in range(2000)],
        'output_length': [20 + (i % 200) for i in range(2000)],
        'source': ['human', 'synthetic', 'augmented'] * 666 + ['human', 'synthetic'],
        'quality_score': [0.6 + (i % 40) / 100 for i in range(2000)],
        'annotation_confidence': [0.8 + (i % 20) / 100 for i in range(2000)],
        'has_issues': [i % 10 == 0 for i in range(2000)],
    }
    return pd.DataFrame(data)


def validate_rag_metadata(train_data, test_data):
    """
    Validate structured metadata for RAG systems.
    
    This checks:
    - Data quality and integrity
    - Distribution shifts between train/test
    - Feature drift that might affect retrieval quality
    """
    logger.info("Validating RAG metadata...")
    
    # Convert boolean columns to categorical for DeepChecks
    train_data = train_data.copy()
    test_data = test_data.copy()
    
    train_data['has_citations'] = train_data['has_citations'].astype(str)
    test_data['has_citations'] = test_data['has_citations'].astype(str)
    
    train_dataset = Dataset(
        train_data,
        cat_features=['document_id', 'source_type', 'has_citations']
    )
    test_dataset = Dataset(
        test_data,
        cat_features=['document_id', 'source_type', 'has_citations']
    )
    
    # Run data integrity checks
    integrity_suite = data_integrity()
    integrity_result = integrity_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    
    # Run train-test validation to detect drift
    validation_suite = train_test_validation()
    validation_result = validation_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    
    return integrity_result, validation_result


def validate_training_data_quality(train_data, test_data):
    """
    Validate training data quality for LLM fine-tuning.
    
    This checks:
    - Data integrity issues
    - Quality score distributions
    - Label/source distribution shifts
    - Annotation confidence patterns
    """
    logger.info("Validating training data quality...")
    
    # Convert boolean columns to categorical
    train_data = train_data.copy()
    test_data = test_data.copy()
    
    train_data['has_issues'] = train_data['has_issues'].astype(str)
    test_data['has_issues'] = test_data['has_issues'].astype(str)
    
    train_dataset = Dataset(
        train_data,
        cat_features=['example_id', 'source', 'has_issues']
    )
    test_dataset = Dataset(
        test_data,
        cat_features=['example_id', 'source', 'has_issues']
    )
    
    # Run data integrity checks
    integrity_suite = data_integrity()
    integrity_result = integrity_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    
    # Run train-test validation
    validation_suite = train_test_validation()
    validation_result = validation_suite.run(
        train_dataset=train_dataset,
        test_dataset=test_dataset
    )
    
    return integrity_result, validation_result


def main():
    """Main execution function for LLM data validation."""
    logger.info("Starting DeepChecks validation for LLM system data...")
    
    output_dir = Path('results')
    output_dir.mkdir(exist_ok=True)
    
    # Example 1: RAG System Metadata Validation
    logger.info("\n" + "="*60)
    logger.info("Example 1: Validating RAG System Metadata")
    logger.info("="*60)
    
    rag_data = create_rag_metadata_example()
    rag_train, rag_test = train_test_split(
        rag_data,
        test_size=0.2,
        random_state=42
    )
    
    rag_integrity, rag_validation = validate_rag_metadata(rag_train, rag_test)
    
    rag_integrity.save_as_html(
        str(output_dir / 'rag_metadata_integrity_report.html')
    )
    rag_validation.save_as_html(
        str(output_dir / 'rag_metadata_validation_report.html')
    )
    
    logger.info("RAG metadata validation completed")
    logger.info(f"Results saved to {output_dir}/")
    
    # Example 2: Training Data Quality Validation
    logger.info("\n" + "="*60)
    logger.info("Example 2: Validating LLM Training Data Quality")
    logger.info("="*60)
    
    training_data = create_training_data_example()
    train_train, train_test = train_test_split(
        training_data,
        test_size=0.2,
        random_state=42
    )
    
    train_integrity, train_validation = validate_training_data_quality(
        train_train, train_test
    )
    
    train_integrity.save_as_html(
        str(output_dir / 'training_data_integrity_report.html')
    )
    train_validation.save_as_html(
        str(output_dir / 'training_data_validation_report.html')
    )
    
    logger.info("Training data validation completed")
    logger.info(f"Results saved to {output_dir}/")
    
    # Display summaries
    print("\n" + "="*60)
    print("RAG METADATA INTEGRITY SUMMARY")
    print("="*60)
    print(rag_integrity)
    
    print("\n" + "="*60)
    print("RAG METADATA VALIDATION SUMMARY")
    print("="*60)
    print(rag_validation)
    
    print("\n" + "="*60)
    print("TRAINING DATA INTEGRITY SUMMARY")
    print("="*60)
    print(train_integrity)
    
    print("\n" + "="*60)
    print("TRAINING DATA VALIDATION SUMMARY")
    print("="*60)
    print(train_validation)
    
    logger.info("\nDeepChecks validation for LLM system data completed successfully")
    logger.info("\nNote: For LLM-specific metrics (toxicity, hallucination, faithfulness),")
    logger.info("use DeepEval or RAGAs. DeepChecks validates structured/tabular data quality.")


if __name__ == '__main__':
    main()

