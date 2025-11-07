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

### Production Monitoring Dashboard

Use the monitoring dashboard for enhanced reporting and alerting:

```bash
python monitoring_dashboard.py
```

Or integrate it into your validation scripts:

```python
from monitoring_dashboard import MonitoringDashboard

dashboard = MonitoringDashboard()
analysis = dashboard.analyze_result(suite_result, 'data_integrity')
dashboard.save_reports()
dashboard.print_dashboard()
```

### Automated Monitoring Workflow

Run automated monitoring that can be scheduled:

```bash
# With sample data
python automated_monitoring.py

# With your own data file
python automated_monitoring.py --data /path/to/data.csv

# Skip model evaluation for faster runs
python automated_monitoring.py --skip-model-eval
```

### End-to-End Integration Example

See a complete integration example:

```bash
python integration_example.py
```

This demonstrates:
- Complete monitoring pipeline
- Data quality validation
- Data drift detection
- Model evaluation
- Alert generation
- Report generation

## Features

- **Data Integrity Checks**: Validates data quality, missing values, duplicates, etc.
- **Train-Test Validation**: Checks for data drift, label distribution, feature importance changes
- **Model Evaluation**: Evaluates model performance, confusion matrix, feature importance, etc.
- **LLM Data Validation**: Validates structured data used in RAG systems and LLM training pipelines
- **Production Monitoring Dashboard**: Enhanced reporting, visualization, and alerting
- **Automated Workflows**: Scheduled monitoring and CI/CD integration
- **Alert Configuration**: Configurable thresholds for automated alerting

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

### Monitoring Dashboard:
- `monitoring_results/monitoring_summary.txt` - Text summary
- `monitoring_results/results_history.json` - Historical results
- `monitoring_results/alerts.json` - Active alerts
- `monitoring_results/monitoring_history.csv` - CSV report

## Alert Configuration

Configure alert thresholds in `alert_config.json`:

```json
{
  "data_integrity": {
    "missing_values_threshold": 0.05,
    "duplicates_threshold": 0.01,
    "data_quality_score": 0.8
  },
  "data_drift": {
    "drift_score_threshold": 0.2,
    "feature_drift_threshold": 0.15,
    "label_drift_threshold": 0.1
  },
  "model_performance": {
    "accuracy_threshold": 0.7,
    "performance_degradation": 0.1
  }
}
```

## CI/CD Integration

The repository includes GitHub Actions workflows for automated monitoring:

- **`.github/workflows/deepchecks-ci.yml`**: Automated validation on push/PR
- Scheduled daily monitoring runs
- Artifact upload
- Alert generation

To use in your repository:
1. Copy `.github/workflows/deepchecks-ci.yml` to your repo
2. Adjust paths and configurations as needed
3. Push to trigger automated runs

## Integration with LLM Monitoring

DeepChecks complements LLM monitoring tools:

- **DeepChecks**: Validates structured/tabular data quality, detects data drift
- **DeepEval**: Evaluates LLM outputs (toxicity, hallucination, faithfulness)
- **RAGAs**: Evaluates RAG system performance (retrieval quality, answer quality)

Use DeepChecks to ensure data quality before it reaches your LLM systems, and use DeepEval/RAGAs to evaluate the LLM outputs themselves.

## Documentation

For more information, see the [DeepChecks documentation](https://docs.deepchecks.com/).
