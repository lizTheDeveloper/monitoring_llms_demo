"""
Advanced RAG Metrics Demo using RAGAs

This script demonstrates advanced evaluation metrics:
- Answer Correctness: Measures correctness using both semantic similarity and factual accuracy
- Context Relevancy: Measures how relevant the context is to the question
- Aspect Critic: Custom evaluation criteria using LLM-as-a-judge
- Rubrics Score: Evaluation based on user-defined rubrics
"""

import os
from dotenv import load_dotenv
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    answer_correctness,
    context_relevancy,
    AspectCritic,
    RubricsScore,
)
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the evaluator LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
evaluator_llm = LangchainLLMWrapper(llm)


def create_advanced_dataset():
    """Create a dataset for advanced evaluation"""
    data_samples = {
        "question": [
            "Explain quantum computing in simple terms",
            "What are the benefits of renewable energy?",
            "How does machine learning work?",
        ],
        "answer": [
            "Quantum computing uses quantum mechanical phenomena like superposition and entanglement to perform computations. Unlike classical computers that use bits (0 or 1), quantum computers use quantum bits or qubits that can exist in multiple states simultaneously, allowing for parallel processing of information.",
            "Renewable energy sources like solar and wind power offer numerous benefits including reduced greenhouse gas emissions, lower long-term costs, energy independence, and job creation in the green energy sector. They are also sustainable and don't deplete natural resources.",
            "Machine learning is a subset of artificial intelligence where algorithms learn patterns from data. It involves training models on datasets to make predictions or decisions without being explicitly programmed for each task. The model improves its performance through experience.",
        ],
        "contexts": [
            [
                "Quantum computing leverages quantum mechanical properties such as superposition and entanglement.",
                "Qubits can exist in multiple states simultaneously, enabling parallel computation.",
                "Classical computers use binary bits, while quantum computers use qubits.",
            ],
            [
                "Renewable energy reduces carbon emissions and environmental impact.",
                "Solar and wind power are sustainable energy sources.",
                "Renewable energy can reduce dependence on fossil fuels.",
            ],
            [
                "Machine learning algorithms learn from data patterns.",
                "Training involves feeding data to models to improve predictions.",
                "ML is a subset of AI focused on pattern recognition.",
            ],
        ],
        "ground_truth": [
            "Quantum computing uses quantum mechanics (superposition, entanglement) to process information. Qubits can be in multiple states at once, unlike classical bits.",
            "Renewable energy benefits include reduced emissions, sustainability, lower costs over time, and energy independence.",
            "Machine learning trains algorithms on data to recognize patterns and make predictions without explicit programming for each task.",
        ],
    }
    return Dataset.from_dict(data_samples)


def run_advanced_evaluation():
    """Run advanced RAG evaluation"""
    print("=" * 60)
    print("Advanced RAG Metrics Demo")
    print("=" * 60)
    
    # Create dataset
    dataset = create_advanced_dataset()
    
    print("\nSample Dataset:")
    print(dataset.to_pandas())
    
    # Define custom aspect critic for clarity
    clarity_critic = AspectCritic(
        name="clarity",
        definition="Evaluate how clear and understandable the answer is. Return 1 if the answer is clear and well-explained, 0 otherwise.",
        llm=evaluator_llm,
    )
    
    # Define rubrics for comprehensiveness
    comprehensiveness_rubrics = {
        "score1_description": "The answer is incomplete and misses key information.",
        "score2_description": "The answer covers some aspects but lacks important details.",
        "score3_description": "The answer is reasonably comprehensive but could be more detailed.",
        "score4_description": "The answer is comprehensive and covers most important points.",
        "score5_description": "The answer is highly comprehensive and covers all important aspects thoroughly.",
    }
    
    comprehensiveness_score = RubricsScore(
        rubrics=comprehensiveness_rubrics,
        llm=evaluator_llm,
        name="comprehensiveness",
    )
    
    # Define metrics
    metrics = [
        answer_correctness,
        context_relevancy,
        clarity_critic,
        comprehensiveness_score,
    ]
    
    print("\n" + "=" * 60)
    print("Running Advanced Evaluation...")
    print("=" * 60)
    
    # Run evaluation
    result = evaluate(
        dataset=dataset,
        metrics=metrics,
        llm=evaluator_llm,
    )
    
    print("\n" + "=" * 60)
    print("Evaluation Results")
    print("=" * 60)
    
    # Display results
    results_df = result.to_pandas()
    print("\nDetailed Results:")
    print(results_df)
    
    print("\n" + "=" * 60)
    print("Summary Metrics")
    print("=" * 60)
    print(result.summary_metrics)
    
    return result


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        exit(1)
    
    run_advanced_evaluation()

