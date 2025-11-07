# AI Alignment Demo: Monitoring and Evaluating LLM Systems

This repository demonstrates three frameworks for monitoring Large Language Model (LLM) applications: **DeepEval**, **RAGAs**, and **DeepChecks**. These tools help ensure AI systems produce reliable, safe outputs.

**Working demo repository** tested on macOS, Linux, and Windows.

## 📚 Documentation

### Getting Started
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Installation and setup instructions
- **[ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md)** - Key metrics: faithfulness, toxicity, bias, fairness

### Production Use
- **[PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md)** - User-facing agent monitoring
- **[TASK_EXECUTING_AGENTS.md](TASK_EXECUTING_AGENTS.md)** - Code generation and task-executing agents
- **[ENTERPRISE_MONITORING.md](ENTERPRISE_MONITORING.md)** - Organizational-level monitoring

### Implementation
- **[IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md)** - Code examples
- **[BEST_PRACTICES.md](BEST_PRACTICES.md)** - Implementation guidance
- **[CRITICAL_THINKING.md](CRITICAL_THINKING.md)** - Evaluation framework

## What is AI Alignment?

AI alignment ensures AI systems behave safely and as intended. Key properties:
- **Correctness** - Factually accurate outputs
- **Relevancy** - Responses match user queries
- **Safety** - Appropriate, non-harmful outputs
- **Fairness** - Unbiased, equitable treatment

## Tools Overview

### DeepEval (`deepeval_demo/`)
Comprehensive LLM evaluation framework for conversational agents, custom criteria, and multi-turn conversations.

### RAGAs (`ragas_demo/`)
Specialized RAG system evaluation for retrieval quality, generation quality, and agent tool usage.

### DeepChecks (`deepchecks/`)
Data and model validation for detecting data drift, quality issues, and performance degradation.

### When to Use Which Tool
- **DeepEval** - Conversational agents, custom evaluation criteria
- **RAGAs** - RAG systems, retrieval-based applications, agent tool usage
- **DeepChecks** - Data quality validation, drift detection, model monitoring
- **All Three** - Production systems requiring comprehensive coverage

## Quick Start

**Prerequisites**: Python 3.8+, OpenAI API key

**Setup Steps**:
1. Set `OPENAI_API_KEY` environment variable
2. Navigate to a demo directory (`deepeval_demo/`, `ragas_demo/`, or `deepchecks/`)
3. Create virtual environment: `python3 -m venv venv`
4. Activate: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
5. Install: `pip install -r requirements.txt`
6. Run demos: `python <script_name>.py`

**See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions.**

## Demo Structure

```
monitoring_llms_demo/
├── deepeval_demo/          # Comprehensive LLM evaluation
├── ragas_demo/             # RAG system evaluation  
├── deepchecks/             # Data quality & drift detection
└── docs/                   # Implementation guides
```

Each demo directory contains:
- Example scripts demonstrating key metrics
- `README.md` with usage instructions
- `requirements.txt` for dependencies

## Key Demo Scripts

### DeepEval (`deepeval_demo/`)
- `basic_metrics.py` - Answer relevancy, correctness, helpfulness
- `rag_metrics.py` - RAG evaluation and hallucination detection
- `conversational_metrics.py` - Multi-turn conversation evaluation
- `toxicity_metrics.py` - Toxicity detection ⚠️ **Critical**
- `bias_metrics.py` - Bias detection ⚠️ **Critical**
- `fairness_metrics.py` - Fairness evaluation ⚠️ **Critical**
- `code_quality_metrics.py` - Code security and quality
- `comprehensive_alignment_demo.py` - Combined metrics

### RAGAs (`ragas_demo/`)
- `basic_rag_evaluation.py` - Core RAG metrics
- `advanced_metrics.py` - Custom criteria and rubrics
- `multi_turn_evaluation.py` - Agent goal and tool accuracy
- `toxicity_bias_fairness.py` - Critical alignment metrics ⚠️
- `code_agent_evaluation.py` - Code generation monitoring
- `production_evaluation.py` - Production best practices

### DeepChecks (`deepchecks/`)
- `example_tabular.py` - Data integrity and model validation
- `llm_data_validation.py` - LLM system data validation
- `monitoring_dashboard.py` - Production monitoring dashboard
- `automated_monitoring.py` - Scheduled monitoring
- `integration_example.py` - End-to-end pipeline

## Learning Path

**Beginners**: 
1. [SETUP_GUIDE.md](SETUP_GUIDE.md) → Set up demos
2. [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) → Learn key metrics
3. Run demo scripts → See metrics in action

**Production Systems**:
1. [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) → User-facing agents
2. [TASK_EXECUTING_AGENTS.md](TASK_EXECUTING_AGENTS.md) → Code generation agents
3. [IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md) → Code examples
4. [BEST_PRACTICES.md](BEST_PRACTICES.md) → Implementation guidance

**Enterprise/Organization**:
1. [ENTERPRISE_MONITORING.md](ENTERPRISE_MONITORING.md) → Organizational monitoring
2. [CRITICAL_THINKING.md](CRITICAL_THINKING.md) → Evaluation framework

## External Resources

- **DeepEval**: [Docs](https://docs.confident-ai.com/) | [GitHub](https://github.com/confident-ai/deepeval)
- **RAGAs**: [Docs](https://docs.ragas.io/) | [GitHub](https://github.com/explodinggradients/ragas)
- **DeepChecks**: [Docs](https://docs.deepchecks.com/) | [GitHub](https://github.com/deepchecks/deepchecks)

## License

Educational demonstration repository. See individual tool licenses for usage terms.

