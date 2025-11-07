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

## Notes

- All demos use `gpt-4o-mini` for cost efficiency. You can change the model in each script.
- Thresholds are set to 0.7 by default but can be adjusted.
- The `include_reason=True` parameter provides explanations for scores.

