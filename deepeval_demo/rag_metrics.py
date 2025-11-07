"""
RAG (Retrieval-Augmented Generation) Metrics Demo

This script demonstrates RAG-specific evaluation metrics:
- Contextual Relevancy
- Contextual Recall
- Contextual Precision
- Faithfulness
"""

import os
from dotenv import load_dotenv
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRelevancyMetric,
    ContextualRecallMetric,
    ContextualPrecisionMetric,
    FaithfulnessMetric,
    AnswerRelevancyMetric
)

# Load environment variables
load_dotenv()

def demo_rag_triad():
    """Demonstrate the RAG Triad: Relevancy, Recall, Precision"""
    print("\n" + "="*60)
    print("Demo: RAG Triad Metrics")
    print("="*60)
    
    # Initialize metrics
    contextual_relevancy = ContextualRelevancyMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    contextual_recall = ContextualRecallMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    contextual_precision = ContextualPrecisionMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    # Example RAG test case
    test_case = LLMTestCase(
        input="What are the benefits of exercise?",
        actual_output="Exercise provides numerous health benefits including improved cardiovascular health, stronger muscles, better mental health, and increased energy levels. Regular physical activity can also help with weight management and reduce the risk of chronic diseases.",
        retrieval_context=[
            "Exercise improves cardiovascular health by strengthening the heart and improving circulation.",
            "Regular physical activity helps build and maintain strong muscles and bones.",
            "Exercise releases endorphins which can improve mood and reduce stress.",
            "Physical activity increases energy levels and can help with better sleep.",
            "Regular exercise is important for maintaining a healthy weight.",
            "Exercise can reduce the risk of developing chronic diseases like diabetes and heart disease."
        ]
    )
    
    evaluate(
        test_cases=[test_case],
        metrics=[contextual_relevancy, contextual_recall, contextual_precision]
    )
    print("\n")


def demo_faithfulness():
    """Demonstrate Faithfulness metric (checks if output is grounded in context)"""
    print("\n" + "="*60)
    print("Demo: Faithfulness Metric")
    print("="*60)
    
    faithfulness_metric = FaithfulnessMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_cases = [
        # Faithful response
        LLMTestCase(
            input="What is the capital of France?",
            actual_output="Paris is the capital of France.",
            retrieval_context=["Paris is the capital and largest city of France."]
        ),
        # Unfaithful response (contains information not in context)
        LLMTestCase(
            input="What is the capital of France?",
            actual_output="Paris is the capital of France, and it has a population of 2.1 million people.",
            retrieval_context=["Paris is the capital and largest city of France."]
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[faithfulness_metric])
    print("\n")


def demo_enhanced_hallucination_detection():
    """Enhanced hallucination detection with various types of hallucinations"""
    print("\n" + "="*60)
    print("Demo: Enhanced Hallucination Detection")
    print("="*60)
    
    faithfulness_metric = FaithfulnessMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_cases = [
        # Grounded response (no hallucination)
        LLMTestCase(
            input="What is machine learning?",
            actual_output="Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
            retrieval_context=[
                "Machine learning is a subset of artificial intelligence.",
                "It enables systems to learn and improve from experience without being explicitly programmed.",
                "Machine learning algorithms use data to identify patterns and make predictions."
            ]
        ),
        # Fabricated facts (hallucination)
        LLMTestCase(
            input="When was the first computer invented?",
            actual_output="The first computer was invented in 1943 by John Smith at MIT.",
            retrieval_context=[
                "Early computing devices date back to the 1940s.",
                "The ENIAC computer was completed in 1945."
            ]
        ),
        # Invented citations (hallucination)
        LLMTestCase(
            input="What does research say about exercise?",
            actual_output="According to a 2023 study published in Nature (Smith et al., 2023), exercise significantly improves cognitive function.",
            retrieval_context=[
                "Research shows that regular exercise has numerous health benefits.",
                "Studies indicate exercise can improve mental health and cognitive function."
            ]
        ),
        # Unsupported claims (hallucination)
        LLMTestCase(
            input="What are the side effects of this medication?",
            actual_output="This medication has no side effects and is completely safe for all patients.",
            retrieval_context=[
                "This medication is generally well-tolerated.",
                "Common side effects may include mild nausea or dizziness."
            ]
        ),
        # Contradictory information (hallucination)
        LLMTestCase(
            input="What is the company's return policy?",
            actual_output="We offer a 60-day return policy with no questions asked.",
            retrieval_context=[
                "Our return policy allows returns within 30 days of purchase.",
                "Items must be in original condition with receipt."
            ]
        ),
        # Partial hallucination (some facts correct, some fabricated)
        LLMTestCase(
            input="Tell me about the solar system",
            actual_output="The solar system has 8 planets, and Jupiter is the largest planet. The sun is approximately 4.6 billion years old and contains 99.8% of the solar system's mass. Pluto was reclassified as a dwarf planet in 2006, and there are currently 15 known dwarf planets in the solar system.",
            retrieval_context=[
                "The solar system consists of 8 planets.",
                "Jupiter is the largest planet in our solar system.",
                "The sun is approximately 4.6 billion years old.",
                "The sun contains about 99.8% of the solar system's total mass.",
                "Pluto was reclassified as a dwarf planet in 2006."
            ]
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[faithfulness_metric])
    print("\n")
    print("Note: Hallucinations can take various forms:")
    print("- Fabricated facts not in the context")
    print("- Invented citations or references")
    print("- Unsupported claims")
    print("- Contradictory information")
    print("- Partial hallucinations (mix of true and false)")
    print("\n")


def demo_comprehensive_rag():
    """Comprehensive RAG evaluation with multiple metrics"""
    print("\n" + "="*60)
    print("Demo: Comprehensive RAG Evaluation")
    print("="*60)
    
    # Initialize all RAG metrics
    answer_relevancy = AnswerRelevancyMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    faithfulness = FaithfulnessMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    contextual_relevancy = ContextualRelevancyMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_case = LLMTestCase(
        input="How does photosynthesis work?",
        actual_output="Photosynthesis is the process by which plants convert light energy into chemical energy. During this process, plants use sunlight, water, and carbon dioxide to produce glucose and oxygen. The process occurs in chloroplasts and involves two main stages: light-dependent reactions and light-independent reactions (Calvin cycle).",
        retrieval_context=[
            "Photosynthesis is a process used by plants to convert light energy into chemical energy.",
            "The process requires sunlight, water, and carbon dioxide as inputs.",
            "The outputs of photosynthesis are glucose (sugar) and oxygen.",
            "Photosynthesis occurs in the chloroplasts of plant cells.",
            "The process has two main stages: light-dependent reactions and the Calvin cycle."
        ]
    )
    
    evaluate(
        test_cases=[test_case],
        metrics=[answer_relevancy, faithfulness, contextual_relevancy]
    )
    print("\n")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or export it.")
        exit(1)
    
    print("\n" + "="*60)
    print("DeepEval RAG Metrics Demo")
    print("="*60)
    
    demo_rag_triad()
    demo_faithfulness()
    demo_enhanced_hallucination_detection()
    demo_comprehensive_rag()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\nKey Takeaways:")
    print("- Faithfulness metric detects hallucinations")
    print("- Hallucinations can be fabricated facts, invented citations, or unsupported claims")
    print("- Partial hallucinations mix true and false information")
    print("- Use threshold >= 0.7 for hallucination detection")
    print("="*60 + "\n")

