# AI Alignment Demo: Monitoring and Evaluating LLM Systems

This repository demonstrates three essential frameworks for monitoring, evaluating, and aligning Large Language Model (LLM) applications: **DeepEval**, **RAGAs**, and **DeepChecks**. These tools help ensure that AI systems behave as intended, produce reliable outputs, and maintain quality over time—critical components of AI alignment.

**This is a working demo repository** that has been tested on macOS and Windows. All scripts are ready to run locally with proper setup.

## 📚 Course Materials

This repository is organized into focused guides for different aspects of AI alignment monitoring:

### Core Guides

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete setup instructions for macOS, Linux, and Windows
- **[ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md)** - Detailed guide to critical alignment metrics: faithfulness, hallucination, relevance, toxicity, bias, and fairness
- **[PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md)** - Strategies for monitoring user-facing agents in production
- **[TASK_EXECUTING_AGENTS.md](TASK_EXECUTING_AGENTS.md)** - Monitoring agents that perform work (code generation, automation, tool usage)
- **[ENTERPRISE_MONITORING.md](ENTERPRISE_MONITORING.md)** - Organizational-level monitoring to prevent agentic misalignment
- **[CRITICAL_THINKING.md](CRITICAL_THINKING.md)** - Framework for critical thinking about AI alignment and evaluation
- **[IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md)** - Code examples for implementing custom metrics
- **[BEST_PRACTICES.md](BEST_PRACTICES.md)** - Best practices for implementing and maintaining AI alignment monitoring

## What is AI Alignment?

AI alignment refers to ensuring that AI systems behave in ways that are beneficial, predictable, and aligned with human values and intentions. In the context of prompt engineering and agent development, alignment means:

- **Correctness**: The system produces factually accurate outputs
- **Relevancy**: Responses are relevant to user queries
- **Reliability**: Consistent behavior across different inputs
- **Safety**: Outputs are appropriate and don't cause harm
- **Transparency**: We can understand and explain system behavior

This demo shows how to measure and improve these alignment properties using automated evaluation frameworks.

## Overview of Tools

### 1. DeepEval
**Purpose**: Comprehensive evaluation framework for LLM applications

**Key Capabilities**:
- Single-turn and multi-turn conversation evaluation
- Custom evaluation criteria using LLM-as-a-judge
- RAG pipeline evaluation
- Role adherence and goal accuracy tracking

**Best For**: Evaluating complete LLM applications, conversational agents, and custom evaluation scenarios

**Location**: `deepeval_demo/`

### 2. RAGAs (Retrieval Augmented Generation Assessment)
**Purpose**: Specialized evaluation framework for RAG systems

**Key Capabilities**:
- Retrieval quality metrics (context precision, recall, relevancy)
- Generation quality metrics (faithfulness, answer relevancy, correctness)
- Agent evaluation (goal accuracy, tool call accuracy)
- Custom rubrics and aspect-based evaluation

**Best For**: RAG pipelines, retrieval systems, and agent-based applications

**Location**: `ragas_demo/`

### 3. DeepChecks
**Purpose**: Data and model validation for ML systems

**Key Capabilities**:
- Data integrity checks (missing values, duplicates, quality)
- Train-test validation (data drift, distribution shifts)
- Model evaluation (performance metrics, feature importance)
- Continuous monitoring capabilities

**Best For**: Validating data quality, detecting drift, and monitoring model performance

**Location**: `deepchecks/`

## How These Tools Support AI Alignment

### Measuring Alignment Properties

| Alignment Property | DeepEval | RAGAs | DeepChecks |
|-------------------|----------|-------|------------|
| **Correctness** | ✅ GEval metrics, factual accuracy | ✅ Answer correctness | ✅ Model performance |
| **Relevancy** | ✅ Answer relevancy | ✅ Context/answer relevancy | - |
| **Reliability** | ✅ Consistent evaluation | ✅ Consistent metrics | ✅ Data drift detection |
| **Safety** | ✅ Custom criteria | ✅ Custom rubrics | - |
| **Transparency** | ✅ Detailed reasoning | ✅ Metric explanations | ✅ Comprehensive reports |

### Use Cases

- **Prompt Engineering**: Use DeepEval to test different prompts and measure their effectiveness
- **RAG Systems**: Use RAGAs to ensure your retrieval and generation components work correctly
- **Production Monitoring**: Use DeepChecks to detect when your system's behavior changes over time
- **Agent Development**: Use all three tools to validate agent behavior, tool usage, and goal achievement

## Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (for LLM-based evaluations)
- Virtual environment (recommended)

### Setup

1. **Clone and navigate to the repository**:
   ```bash
   cd monitoring_llms_demo
   ```

2. **Set up environment variables**:
   Create a `.env` file in each demo directory (or at the root):
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Run each demo**:

   **DeepEval Demo**:
   
   **macOS/Linux**:
   ```bash
   cd deepeval_demo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python basic_metrics.py
   python rag_metrics.py
   python conversational_metrics.py
   python toxicity_metrics.py
   python bias_metrics.py
   python fairness_metrics.py
   python code_quality_metrics.py
   python comprehensive_alignment_demo.py
   ```
   
   **Windows**:
   ```cmd
   cd deepeval_demo
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python basic_metrics.py
   python rag_metrics.py
   python conversational_metrics.py
   python toxicity_metrics.py
   python bias_metrics.py
   python fairness_metrics.py
   python code_quality_metrics.py
   python comprehensive_alignment_demo.py
   ```

   **RAGAs Demo**:
   
   **macOS/Linux**:
   ```bash
   cd ragas_demo
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python basic_rag_evaluation.py
   python advanced_metrics.py
   python multi_turn_evaluation.py
   python toxicity_bias_fairness.py
   python code_agent_evaluation.py
   python production_evaluation.py
   ```
   
   **Windows**:
   ```cmd
   cd ragas_demo
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python basic_rag_evaluation.py
   python advanced_metrics.py
   python multi_turn_evaluation.py
   python toxicity_bias_fairness.py
   python code_agent_evaluation.py
   python production_evaluation.py
   ```

   **DeepChecks Demo**:
   
   **macOS/Linux**:
   ```bash
   cd deepchecks
   python3 -m venv venv  # if creating new venv
   source venv/bin/activate
   pip install -r requirements.txt
   python example_tabular.py
   python llm_data_validation.py
   python monitoring_dashboard.py
   python automated_monitoring.py
   python integration_example.py
   ```
   
   **Windows**:
   ```cmd
   cd deepchecks
   python -m venv venv  # if creating new venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python example_tabular.py
   python llm_data_validation.py
   python monitoring_dashboard.py
   python automated_monitoring.py
   python integration_example.py
   ```

## Demo Structure

```
monitoring_llms_demo/
├── README.md                    # This file
├── deepeval_demo/              # DeepEval demonstrations
│   ├── basic_metrics.py        # Basic LLM evaluation metrics
│   ├── rag_metrics.py          # RAG-specific evaluation
│   ├── conversational_metrics.py  # Multi-turn conversation evaluation
│   ├── toxicity_metrics.py     # Toxicity detection
│   ├── bias_metrics.py         # Bias detection
│   ├── fairness_metrics.py     # Fairness evaluation
│   ├── code_quality_metrics.py # Code generation agent monitoring
│   ├── comprehensive_alignment_demo.py  # Production monitoring demo
│   ├── requirements.txt
│   ├── README.md
│   └── NEXT_STEPS.md           # Implementation roadmap
├── ragas_demo/                 # RAGAs demonstrations
│   ├── basic_rag_evaluation.py # Core RAG metrics
│   ├── advanced_metrics.py     # Advanced evaluation techniques
│   ├── multi_turn_evaluation.py # Agent and conversation evaluation
│   ├── toxicity_bias_fairness.py # Critical alignment metrics
│   ├── code_agent_evaluation.py # Code generation agent monitoring
│   ├── production_evaluation.py # Comprehensive production evaluation
│   ├── requirements.txt
│   ├── README.md
│   └── NEXT_STEPS.md           # Implementation roadmap
└── deepchecks/                 # DeepChecks demonstrations
    ├── example_tabular.py      # Data and model validation
    ├── llm_data_validation.py  # LLM system data validation
    ├── monitoring_dashboard.py # Production monitoring dashboard
    ├── automated_monitoring.py # Automated monitoring workflow
    ├── integration_example.py  # End-to-end integration example
    ├── requirements.txt
    ├── README.md
    └── NEXT_STEPS.md           # Implementation roadmap
```

### Implementation Status

Each demo folder has a `NEXT_STEPS.md` file tracking what's implemented and what's planned:

- **[deepeval_demo/NEXT_STEPS.md](deepeval_demo/NEXT_STEPS.md)** - DeepEval implementation roadmap
- **[ragas_demo/NEXT_STEPS.md](ragas_demo/NEXT_STEPS.md)** - RAGAs implementation roadmap
- **[deepchecks/NEXT_STEPS.md](deepchecks/NEXT_STEPS.md)** - DeepChecks implementation roadmap

## Understanding the Demos

### DeepEval Demos

1. **`basic_metrics.py`**: Demonstrates fundamental evaluation metrics
   - Answer relevancy: Is the response relevant to the query?
   - GEval correctness: Is the output factually correct?
   - GEval helpfulness: Is the response helpful to the user?

2. **`rag_metrics.py`**: Evaluates RAG pipelines
   - Contextual relevancy: Is the retrieved context relevant?
   - Faithfulness: Is the answer grounded in the context?
   - RAG triad metrics: Comprehensive RAG evaluation

3. **`conversational_metrics.py`**: Evaluates multi-turn conversations
   - Role adherence: Does the assistant follow its role?
   - Topic adherence: Does the conversation stay on topic?
   - Knowledge retention: Does the model remember context?
   - Goal accuracy: Does the conversation achieve its goal?

4. **`toxicity_metrics.py`**: Toxicity detection for production safety
   - Detects harmful, offensive, or inappropriate content
   - High threshold (0.95+) for production use

5. **`bias_metrics.py`**: Bias detection for fairness
   - Detects demographic, cultural, and implicit bias
   - Examples of biased vs. unbiased responses

6. **`fairness_metrics.py`**: Fairness evaluation for equitable outcomes
   - Evaluates fair and equitable treatment
   - Equal vs. equitable treatment scenarios

7. **`code_quality_metrics.py`**: Code generation agent monitoring
   - Code security: Detects vulnerabilities and insecure configurations
   - Code correctness: Validates functional correctness
   - Code quality: Assesses structure and best practices

8. **`comprehensive_alignment_demo.py`**: Production monitoring with all metrics
   - Combines all critical metrics together
   - Threshold selection guidance
   - Metric combination strategies

**Implementation Status**: ✅ **All critical metrics implemented**. See [deepeval_demo/NEXT_STEPS.md](deepeval_demo/NEXT_STEPS.md) for complete implementation status and optional future enhancements.

### RAGAs Demos

1. **`basic_rag_evaluation.py`**: Core RAG evaluation metrics
   - Faithfulness: Answer groundedness in context
   - Answer relevancy: Answer relevance to question
   - Context precision: Precision of retrieved context
   - Context recall: Recall of relevant context

2. **`advanced_metrics.py`**: Advanced evaluation techniques
   - Answer correctness: Semantic similarity + factual accuracy
   - Context relevancy: Context relevance to question
   - Aspect Critic: Custom evaluation criteria
   - Rubrics Score: User-defined evaluation rubrics

3. **`multi_turn_evaluation.py`**: Agent and conversation evaluation
   - Agent goal accuracy: Did the agent achieve the user's goal?
   - Tool call accuracy: Were tools used correctly?

4. **`toxicity_bias_fairness.py`**: Critical alignment metrics for production
   - Toxicity detection: Identifies harmful or offensive content
   - Bias detection: Evaluates bias in responses
   - Fairness evaluation: Assesses equitable treatment

5. **`code_agent_evaluation.py`**: Code generation agent monitoring
   - Code security: Detects security vulnerabilities
   - Code quality: Assesses structure and best practices

6. **`production_evaluation.py`**: Comprehensive production evaluation
   - Combines all critical metrics (faithfulness, relevancy, toxicity, bias, fairness)
   - Shows threshold selection and trade-offs
   - Demonstrates production best practices

**Implementation Status**: ✅ **All critical metrics implemented**. See [ragas_demo/NEXT_STEPS.md](ragas_demo/NEXT_STEPS.md) for complete implementation status and optional future enhancements.

### DeepChecks Demo

1. **`example_tabular.py`**: Data and model validation
   - Data integrity: Missing values, duplicates, quality issues
   - Train-test validation: Data drift, distribution shifts
   - Model evaluation: Performance metrics, feature importance

2. **`llm_data_validation.py`**: LLM system data validation
   - RAG system metadata validation
   - Training data quality validation for LLM fine-tuning
   - Data drift detection for production LLM pipelines

3. **`monitoring_dashboard.py`**: Production monitoring dashboard
   - Enhanced reporting and visualization
   - Alert configuration and tracking
   - Historical results tracking

4. **`automated_monitoring.py`**: Automated monitoring workflow
   - Scheduled monitoring support
   - Command-line interface
   - Configurable validation suites

5. **`integration_example.py`**: End-to-end integration example
   - Complete monitoring pipeline
   - Data quality → drift → model evaluation flow

**Implementation Status**: ✅ **All critical features implemented**. See [deepchecks/NEXT_STEPS.md](deepchecks/NEXT_STEPS.md) for complete implementation status and optional future enhancements.

## Quick Navigation

**New to AI Alignment?** Start here:
1. Read [What is AI Alignment?](#what-is-ai-alignment) below
2. Follow [SETUP_GUIDE.md](SETUP_GUIDE.md) to get the demos running
3. Review [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) to understand the metrics
4. Check out [CRITICAL_THINKING.md](CRITICAL_THINKING.md) for evaluation frameworks

**Building Production Systems?** Focus on:
- [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) - Monitoring strategies for user-facing agents
- [TASK_EXECUTING_AGENTS.md](TASK_EXECUTING_AGENTS.md) - Monitoring agents that perform work
- [ENTERPRISE_MONITORING.md](ENTERPRISE_MONITORING.md) - Organizational monitoring and misalignment prevention
- [IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md) - Code examples
- [BEST_PRACTICES.md](BEST_PRACTICES.md) - Implementation guidance

**Want Code Examples?** See:
- [IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md) - Custom metric implementations
- Demo scripts in each directory:
  - [deepeval_demo/](deepeval_demo/) - DeepEval demos ([roadmap](deepeval_demo/NEXT_STEPS.md))
  - [ragas_demo/](ragas_demo/) - RAGAs demos ([roadmap](ragas_demo/NEXT_STEPS.md))
  - [deepchecks/](deepchecks/) - DeepChecks demos ([roadmap](deepchecks/NEXT_STEPS.md))

## Key Concepts for AI Alignment

### Evaluation Metrics

**Reference-Based Metrics**: Compare outputs to ground truth (e.g., correctness, accuracy)
- Use when you have expected outputs
- Good for measuring factual accuracy

**Reference-Free Metrics**: Evaluate without ground truth (e.g., relevancy, faithfulness)
- Use when ground truth is unavailable
- Good for measuring quality and appropriateness

**LLM-as-a-Judge**: Use LLMs to evaluate other LLMs
- Flexible and can evaluate nuanced criteria
- Requires API calls and has associated costs
- **Important**: LLM judges can have their own biases—validate with human evaluation

### Continuous Monitoring

AI alignment isn't a one-time check—it requires ongoing monitoring:
- **Data Drift**: Input distributions change over time
- **Model Degradation**: Performance decreases over time
- **Behavioral Shifts**: System behavior changes unexpectedly
- **Adversarial Inputs**: Users may try to manipulate the system

Use DeepChecks to monitor data quality and drift, and combine with DeepEval/RAGAs for application-level monitoring.

## Best Practices

See [BEST_PRACTICES.md](BEST_PRACTICES.md) for comprehensive guidance. Key principles:

1. **Start with Basic Metrics**: Begin with simple, well-understood metrics before adding complexity
2. **Combine Multiple Metrics**: No single metric captures everything—use multiple metrics together
3. **Set Appropriate Thresholds**: Thresholds should reflect your quality requirements
4. **Monitor Over Time**: Set up continuous evaluation, not just one-time checks
5. **Validate with Humans**: Don't rely solely on automated metrics—include human evaluation

For detailed best practices, threshold recommendations, and implementation guidance, see [BEST_PRACTICES.md](BEST_PRACTICES.md).

## When to Use Which Tool

- **Use DeepEval** when:
  - Evaluating complete LLM applications
  - Need custom evaluation criteria
  - Working with conversational agents
  - Want a comprehensive evaluation framework

- **Use RAGAs** when:
  - Building RAG systems
  - Need specialized retrieval/generation metrics
  - Evaluating agent tool usage
  - Want reference-free evaluation

- **Use DeepChecks** when:
  - Validating data quality
  - Detecting data drift
  - Monitoring model performance
  - Need production monitoring

- **Use All Three** when:
  - Building production systems
  - Need comprehensive coverage
  - Want to validate at multiple levels (data, model, application)

## Resources

### DeepEval
- [Documentation](https://docs.confident-ai.com/)
- [GitHub](https://github.com/confident-ai/deepeval)
- [Metrics Guide](https://docs.confident-ai.com/docs/metrics-introduction)

### RAGAs
- [Documentation](https://docs.ragas.io/)
- [GitHub](https://github.com/explodinggradients/ragas)
- [Metrics Guide](https://docs.ragas.io/concepts/metrics)

### DeepChecks
- [Documentation](https://docs.deepchecks.com/)
- [GitHub](https://github.com/deepchecks/deepchecks)

## Setup Instructions

For detailed setup instructions for macOS, Linux, and Windows, see **[SETUP_GUIDE.md](SETUP_GUIDE.md)**.

### Quick Start

1. **Set up environment variables**: Create a `.env` file with your OpenAI API key
2. **Choose a demo**: Navigate to `deepeval_demo/`, `ragas_demo/`, or `deepchecks/`
3. **Create virtual environment**: `python3 -m venv venv` (macOS/Linux) or `python -m venv venv` (Windows)
4. **Activate and install**: `source venv/bin/activate && pip install -r requirements.txt` (macOS/Linux) or `venv\Scripts\activate && pip install -r requirements.txt` (Windows)
5. **Run demos**: Execute the Python scripts in each directory

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for complete instructions, troubleshooting, and platform-specific notes.

## Contributing

This is a demonstration repository for educational purposes. Feel free to:
- Add more examples
- Improve documentation
- Add new evaluation scenarios
- Share feedback and suggestions

## License

This demo repository is provided for educational purposes. Please refer to the individual tool licenses for usage terms.

