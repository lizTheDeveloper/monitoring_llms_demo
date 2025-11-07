# RAGAs Demo

This directory contains a comprehensive demonstration of [RAGAs](https://github.com/explodinggradients/ragas), an open-source framework for evaluating Retrieval-Augmented Generation (RAG) systems and LLM applications.

## What is RAGAs?

RAGAs (Retrieval Augmented Generation Assessment) is a framework that helps you evaluate your RAG pipelines. It provides metrics to assess:
- **Retrieval Quality**: How well your retrieval system finds relevant context
- **Generation Quality**: How well your LLM generates answers from the context
- **End-to-End Quality**: Overall performance of your RAG system

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
   Create a `.env` file in this directory:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## Demo Scripts

### 1. Basic RAG Evaluation (`basic_rag_evaluation.py`)

Demonstrates fundamental RAG evaluation metrics:
- **Faithfulness**: Measures if the answer is grounded in the retrieved context
- **Answer Relevancy**: Measures how relevant the answer is to the question
- **Context Precision**: Measures how precise the retrieved context is
- **Context Recall**: Measures how much of the relevant context was retrieved

**Run:**
```bash
python basic_rag_evaluation.py
```

### 2. Advanced Metrics (`advanced_metrics.py`)

Demonstrates advanced evaluation capabilities:
- **Answer Correctness**: Combines semantic similarity and factual accuracy
- **Context Relevancy**: Measures relevance of context to the question
- **Aspect Critic**: Custom evaluation criteria using LLM-as-a-judge
- **Rubrics Score**: Evaluation based on user-defined rubrics (e.g., comprehensiveness)

**Run:**
```bash
python advanced_metrics.py
```

### 3. Multi-Turn Conversation Evaluation (`multi_turn_evaluation.py`)

Demonstrates evaluation of conversational AI systems:
- **Agent Goal Accuracy**: Measures if the agent achieved the user's goal (with/without reference)
- **Tool Call Accuracy**: Evaluates correct tool usage in agent interactions

**Run:**
```bash
python multi_turn_evaluation.py
```

### 4. Toxicity, Bias, and Fairness (`toxicity_bias_fairness.py`)

Demonstrates critical alignment metrics for production systems:
- **Toxicity Detection**: Identifies harmful, offensive, or inappropriate content
- **Bias Detection**: Evaluates bias toward or against demographic groups, topics, or perspectives
- **Fairness Evaluation**: Assesses equitable treatment and accommodation of different needs

**Priority**: HIGH - Critical for production user-facing agents

**Run:**
```bash
python toxicity_bias_fairness.py
```

### 5. Code Generation Agent Evaluation (`code_agent_evaluation.py`)

Demonstrates monitoring for code generation agents (like Cursor, Claude Code):
- **Code Security**: Detects security vulnerabilities (SQL injection, XSS, hardcoded secrets)
- **Code Quality**: Assesses code structure, best practices, and correctness

**Priority**: MEDIUM - Important for task-executing agents

**Run:**
```bash
python code_agent_evaluation.py
```

### 6. Comprehensive Production Evaluation (`production_evaluation.py`)

Demonstrates how to evaluate a production-ready system using all critical metrics together:
- Combines faithfulness, answer relevancy, toxicity, bias, and fairness
- Shows threshold selection and trade-offs
- Demonstrates production evaluation best practices

**Run:**
```bash
python production_evaluation.py
```

## Key Concepts

### Metrics Types

RAGAs provides two types of metrics:

1. **Computation-based Metrics**: Use mathematical methods (e.g., ROUGE, BLEU)
   - Fast and cost-effective
   - Good for surface-level similarity

2. **LLM-based Metrics**: Use language models as judges
   - More nuanced understanding
   - Better for semantic evaluation
   - Requires API calls

### Evaluation Dataset Format

RAGAs expects datasets with specific fields:
- `question`: The user's query
- `answer`: The generated response
- `contexts`: List of retrieved context chunks
- `ground_truth`: Reference answer (optional, for some metrics)

### Single-Turn vs Multi-Turn

- **Single-Turn**: Evaluate individual Q&A pairs
- **Multi-Turn**: Evaluate entire conversations with multiple exchanges

## Available Metrics

### Retrieval Metrics
- `context_precision`: Precision of retrieved context
- `context_recall`: Recall of relevant context
- `context_relevancy`: Relevance of context to question

### Generation Metrics
- `faithfulness`: Answer groundedness in context
- `answer_relevancy`: Answer relevance to question
- `answer_correctness`: Factual correctness (requires ground truth)

### Custom Metrics
- `AspectCritic`: Define custom evaluation criteria
- `RubricsScore`: Score-based evaluation with custom rubrics
- `DiscreteMetric`: Custom discrete value metrics

### Alignment Metrics
- **Toxicity Detection**: Identify harmful or offensive content
- **Bias Detection**: Evaluate bias in responses
- **Fairness Evaluation**: Assess equitable treatment

### Agent Metrics
- `AgentGoalAccuracy`: Evaluate if agent achieved user goal
- `ToolCallAccuracy`: Evaluate tool usage correctness
- **Code Security**: Evaluate code for security vulnerabilities
- **Code Quality**: Assess code structure and best practices

## Requirements

- Python 3.8+
- OpenAI API key (for LLM-based metrics)
- RAGAs library
- LangChain OpenAI integration

## Resources

- [RAGAs Documentation](https://docs.ragas.io/)
- [RAGAs GitHub](https://github.com/explodinggradients/ragas)
- [RAGAs Metrics Guide](https://docs.ragas.io/concepts/metrics)

## Notes

- All demos use `gpt-4o-mini` for cost efficiency. You can change the model in each script.
- Some metrics require ground truth data, while others are reference-free.
- Multi-turn evaluation uses async/await patterns.
- Results can be exported to pandas DataFrames for further analysis.

