# DeepChecks Implementation

This directory contains a DeepChecks implementation for monitoring and validating machine learning models and data.

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies (if needed):**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Tabular Data Validation

Run the example script for tabular data validation:

```bash
python example_tabular.py
```

This will:
- Load sample data
- Run data integrity checks
- Run train-test validation checks
- Train a model and run model evaluation checks
- Generate HTML reports in the `results/` directory

### LLM System Data Validation

Run the script for validating structured data used by LLM systems:

```bash
python llm_data_validation.py
```

This demonstrates:
- Validating RAG system metadata (document chunks, embeddings, retrieval metrics)
- Validating training data quality for LLM fine-tuning
- Detecting data drift in production LLM pipelines
- Monitoring structured data quality in LLM systems

**Note**: DeepChecks validates structured/tabular data. For LLM-specific metrics (toxicity, hallucination, faithfulness), use DeepEval or RAGAs.

## Features

- **Data Integrity Checks**: Validates data quality, missing values, duplicates, etc.
- **Train-Test Validation**: Checks for data drift, label distribution, feature importance changes
- **Model Evaluation**: Evaluates model performance, confusion matrix, feature importance, etc.
- **LLM Data Validation**: Validates structured data used in RAG systems and LLM training pipelines

## Output

Results are saved as HTML reports in the `results/` directory:

### Tabular Data Validation:
- `data_integrity_report.html`
- `train_test_validation_report.html`
- `model_evaluation_report.html`

### LLM System Data Validation:
- `rag_metadata_integrity_report.html`
- `rag_metadata_validation_report.html`
- `training_data_integrity_report.html`
- `training_data_validation_report.html`

## Integration with LLM Monitoring

DeepChecks complements LLM monitoring tools:

- **DeepChecks**: Validates structured/tabular data quality, detects data drift
- **DeepEval**: Evaluates LLM outputs (toxicity, hallucination, faithfulness)
- **RAGAs**: Evaluates RAG system performance (retrieval quality, answer quality)

Use DeepChecks to ensure data quality before it reaches your LLM systems, and use DeepEval/RAGAs to evaluate the LLM outputs themselves.

## Documentation

For more information, see the [DeepChecks documentation](https://docs.deepchecks.com/).

