# DeepEval Demo

This directory contains a comprehensive demonstration of [DeepEval](https://github.com/confident-ai/deepeval), an open-source framework for evaluating and improving Large Language Model (LLM) applications.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate  # On Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

## Demo Scripts

### 1. Basic Metrics (`basic_metrics.py`)
Demonstrates fundamental evaluation metrics:
- **Answer Relevancy**: Measures how relevant the output is to the input
- **GEval - Correctness**: Custom evaluation for factual correctness
- **GEval - Helpfulness**: Custom evaluation for response helpfulness

**Run:**
```bash
python basic_metrics.py
```

### 2. RAG Metrics (`rag_metrics.py`)
Demonstrates Retrieval-Augmented Generation evaluation:
- **RAG Triad**: Contextual Relevancy, Recall, and Precision
- **Faithfulness**: Ensures output is grounded in retrieved context
- **Enhanced Hallucination Detection**: Various types of hallucinations (fabricated facts, invented citations, unsupported claims, contradictory information, partial hallucinations)
- **Comprehensive RAG Evaluation**: Multiple metrics together

**Run:**
```bash
python rag_metrics.py
```

### 3. Conversational Metrics (`conversational_metrics.py`)
Demonstrates multi-turn conversation evaluation:
- **Role Adherence**: Checks if assistant follows its defined role
- **Topic Adherence**: Ensures conversation stays on topic
- **Knowledge Retention**: Verifies the model remembers information across turns
- **Goal Accuracy**: Evaluates if the conversation achieves its goal

**Run:**
```bash
python conversational_metrics.py
```

### 4. Toxicity Detection (`toxicity_metrics.py`) ⚠️ HIGH PRIORITY
Demonstrates toxicity detection for production user-facing agents:
- **Toxicity Detection**: Identifies toxic, harmful, or inappropriate content
- **Threshold Discussion**: Importance of high thresholds (>= 0.95) for safety
- **Edge Cases**: Handling sarcasm and cultural context

**Run:**
```bash
python toxicity_metrics.py
```

### 5. Bias Detection (`bias_metrics.py`) ⚠️ HIGH PRIORITY
Demonstrates bias detection for fairness and compliance:
- **Demographic Bias**: Detects bias based on race, gender, age, etc.
- **Cultural Bias**: Identifies cultural stereotypes and bias
- **Implicit Bias**: Detects subtle, unconscious biases

**Run:**
```bash
python bias_metrics.py
```

### 6. Fairness Evaluation (`fairness_metrics.py`) ⚠️ HIGH PRIORITY
Demonstrates fairness evaluation for equitable outcomes:
- **Equal vs. Equitable**: Understanding when to use each approach
- **Unfair Treatment Examples**: Identifying discriminatory responses
- **Context-Specific Fairness**: Fairness in different contexts (hiring, service, education)

**Run:**
```bash
python fairness_metrics.py
```

### 7. Code Quality Metrics (`code_quality_metrics.py`)
Demonstrates monitoring for code generation agents:
- **Code Security**: Detects vulnerabilities (SQL injection, XSS, hardcoded secrets)
- **Code Correctness**: Verifies code implements requested functionality
- **Code Quality**: Evaluates readability, maintainability, and best practices

**Run:**
```bash
python code_quality_metrics.py
```

### 8. Comprehensive Alignment Demo (`comprehensive_alignment_demo.py`)
Demonstrates combining all critical alignment metrics:
- **Production Monitoring**: Using multiple metrics together
- **Threshold Selection**: Understanding trade-offs and recommendations
- **Metric Combination Strategies**: Different approaches for different use cases
- **RAG with Alignment**: Combining RAG metrics with alignment metrics

**Run:**
```bash
python comprehensive_alignment_demo.py
```

## Key Concepts

### Test Cases
- **LLMTestCase**: For single-turn LLM interactions
- **ConversationalTestCase**: For multi-turn conversations

### Metrics
DeepEval provides various metrics:
- **Built-in Metrics**: Answer Relevancy, Faithfulness, Contextual metrics, etc.
- **GEval**: Custom evaluation criteria using LLM-as-a-judge
- **RAG Metrics**: Specialized metrics for RAG pipelines

### Evaluation
Use the `evaluate()` function to run test cases against metrics:
```python
from deepeval import evaluate
evaluate(test_cases=[test_case], metrics=[metric])
```

## Requirements

- Python 3.8+
- OpenAI API key (for evaluation metrics)
- DeepEval library

## Resources

- [DeepEval Documentation](https://docs.confident-ai.com/)
- [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- [DeepEval Metrics Guide](https://docs.confident-ai.com/docs/metrics-introduction)

## Metric Priorities

### High Priority (Critical for Production)
- **Toxicity Detection**: Use threshold >= 0.95
- **Bias Detection**: Use threshold >= 0.8
- **Fairness Evaluation**: Use threshold >= 0.8

### Medium Priority
- **Code Quality Metrics**: Security (>= 0.95), Correctness (>= 0.8), Quality (>= 0.7)
- **Enhanced Hallucination Detection**: Use threshold >= 0.7

### Standard Metrics
- **Answer Relevancy**: Use threshold >= 0.7
- **RAG Metrics**: Use threshold >= 0.7
- **Conversational Metrics**: Use threshold >= 0.7

## Notes

- All demos use `gpt-4o-mini` for cost efficiency. You can change the model in each script.
- Thresholds vary by metric type (see priorities above).
- The `include_reason=True` parameter provides explanations for scores.
- For production monitoring, combine multiple metrics for comprehensive evaluation.

