"""
Basic RAG Evaluation Demo using RAGAs

This script demonstrates fundamental RAG evaluation metrics:
- Faithfulness: Measures if the answer is grounded in the context
- Answer Relevancy: Measures how relevant the answer is to the question
- Context Precision: Measures how precise the retrieved context is
- Context Recall: Measures how much of the relevant context was retrieved
"""

import os
from dotenv import load_dotenv
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()


def get_evaluator_llm():
    """Initialize and return the evaluator LLM"""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return LangchainLLMWrapper(llm)

def create_sample_dataset():
    """Create a sample dataset for RAG evaluation"""
    data_samples = {
        "question": [
            "What is the capital of France?",
            "Who wrote Romeo and Juliet?",
            "What is the largest planet in our solar system?",
        ],
        "answer": [
            "The capital of France is Paris, a city known for its art, culture, and history.",
            "Romeo and Juliet was written by William Shakespeare, the famous English playwright.",
            "Jupiter is the largest planet in our solar system, with a mass greater than all other planets combined.",
        ],
        "contexts": [
            [
                "Paris is the capital and most populous city of France.",
                "France is a country in Western Europe.",
                "The Eiffel Tower is located in Paris.",
            ],
            [
                "William Shakespeare was an English playwright and poet.",
                "Romeo and Juliet is a tragedy written by Shakespeare.",
                "Shakespeare wrote many famous plays including Hamlet and Macbeth.",
            ],
            [
                "Jupiter is the fifth planet from the Sun and the largest in the Solar System.",
                "Jupiter has a mass one-thousandth that of the Sun.",
                "The solar system consists of eight planets orbiting the Sun.",
            ],
        ],
        "ground_truth": [
            "The capital of France is Paris.",
            "Romeo and Juliet was written by William Shakespeare.",
            "Jupiter is the largest planet in our solar system.",
        ],
    }
    return Dataset.from_dict(data_samples)


def run_basic_evaluation():
    """Run basic RAG evaluation with core metrics"""
    print("=" * 60)
    print("Basic RAG Evaluation Demo")
    print("=" * 60)
    
    # Create sample dataset
    dataset = create_sample_dataset()
    
    print("\nSample Dataset:")
    print(dataset.to_pandas())
    
    # Initialize evaluator LLM
    evaluator_llm = get_evaluator_llm()
    
    # Define metrics
    metrics = [
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    ]
    
    print("\n" + "=" * 60)
    print("Running Evaluation...")
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
    
    run_basic_evaluation()

