"""
Basic DeepEval Demo - Simple LLM Test Cases

This script demonstrates basic evaluation metrics for LLM outputs:
- Answer Relevancy
- GEval (custom evaluation criteria)
"""

import os
from dotenv import load_dotenv
from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric, GEval

# Load environment variables
load_dotenv()

def demo_answer_relevancy():
    """Demonstrate Answer Relevancy Metric"""
    print("\n" + "="*60)
    print("Demo 1: Answer Relevancy Metric")
    print("="*60)
    
    metric = AnswerRelevancyMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_cases = [
        LLMTestCase(
            input="What if these shoes don't fit?",
            actual_output="We offer a 30-day full refund at no extra cost."
        ),
        LLMTestCase(
            input="What is the capital of France?",
            actual_output="The capital of France is Paris, a beautiful city known for its art and culture."
        ),
        LLMTestCase(
            input="How do I return an item?",
            actual_output="The weather today is sunny and warm."
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[metric])
    print("\n")


def demo_geval_correctness():
    """Demonstrate GEval with custom criteria"""
    print("\n" + "="*60)
    print("Demo 2: GEval - Correctness Metric")
    print("="*60)
    
    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine whether the actual output is factually correct based on the expected output.",
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT
        ],
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_cases = [
        LLMTestCase(
            input="What is 2 + 2?",
            actual_output="The answer is 4.",
            expected_output="4"
        ),
        LLMTestCase(
            input="Who wrote Romeo and Juliet?",
            actual_output="Romeo and Juliet was written by William Shakespeare.",
            expected_output="William Shakespeare"
        ),
        LLMTestCase(
            input="What is the capital of Australia?",
            actual_output="The capital of Australia is Sydney.",
            expected_output="Canberra"
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[correctness_metric])
    print("\n")


def demo_geval_helpfulness():
    """Demonstrate GEval with helpfulness criteria"""
    print("\n" + "="*60)
    print("Demo 3: GEval - Helpfulness Metric")
    print("="*60)
    
    helpfulness_metric = GEval(
        name="Helpfulness",
        criteria="Evaluate how helpful and informative the response is to the user's question.",
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT
        ],
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_cases = [
        LLMTestCase(
            input="How do I bake a chocolate cake?",
            actual_output="To bake a chocolate cake, you'll need flour, sugar, cocoa powder, eggs, butter, and baking powder. Mix the dry ingredients, then add wet ingredients. Bake at 350°F for 30-35 minutes."
        ),
        LLMTestCase(
            input="How do I bake a chocolate cake?",
            actual_output="I don't know."
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[helpfulness_metric])
    print("\n")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or export it.")
        exit(1)
    
    print("\n" + "="*60)
    print("DeepEval Basic Metrics Demo")
    print("="*60)
    
    demo_answer_relevancy()
    demo_geval_correctness()
    demo_geval_helpfulness()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60 + "\n")

