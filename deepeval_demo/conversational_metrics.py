"""
Conversational Metrics Demo

This script demonstrates evaluation metrics for conversational AI:
- Role Adherence
- Topic Adherence
- Knowledge Retention
- Goal Accuracy
"""

import os
from dotenv import load_dotenv
from deepeval import evaluate
from deepeval.test_case import Turn, ConversationalTestCase
from deepeval.metrics import (
    RoleAdherenceMetric,
    TopicAdherenceMetric,
    KnowledgeRetentionMetric,
    GoalAccuracyMetric
)

# Load environment variables
load_dotenv()

def demo_role_adherence():
    """Demonstrate Role Adherence metric"""
    print("\n" + "="*60)
    print("Demo: Role Adherence Metric")
    print("="*60)
    
    metric = RoleAdherenceMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    # Professional customer service agent
    test_case = ConversationalTestCase(
        chatbot_role="You are a professional customer service agent for an e-commerce company. Be polite, helpful, and solution-oriented.",
        turns=[
            Turn(role="user", content="I received a damaged item. What should I do?"),
            Turn(role="assistant", content="I'm sorry to hear about the damaged item. We'll send you a replacement right away. Could you please provide your order number?")
        ]
    )
    
    evaluate(test_cases=[test_case], metrics=[metric])
    print("\n")


def demo_topic_adherence():
    """Demonstrate Topic Adherence metric"""
    print("\n" + "="*60)
    print("Demo: Topic Adherence Metric")
    print("="*60)
    
    metric = TopicAdherenceMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    # Conversation about cooking
    test_case = ConversationalTestCase(
        turns=[
            Turn(role="user", content="I want to learn how to make pasta."),
            Turn(role="assistant", content="Great! To make pasta, you'll need flour, eggs, and a bit of salt. Would you like a basic recipe?"),
            Turn(role="user", content="Yes, please share the recipe."),
            Turn(role="assistant", content="Mix 2 cups flour with 3 eggs and a pinch of salt. Knead for 10 minutes, then roll out and cut into your desired shape.")
        ]
    )
    
    evaluate(test_cases=[test_case], metrics=[metric])
    print("\n")


def demo_knowledge_retention():
    """Demonstrate Knowledge Retention metric"""
    print("\n" + "="*60)
    print("Demo: Knowledge Retention Metric")
    print("="*60)
    
    metric = KnowledgeRetentionMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    # Conversation where user information should be retained
    test_case = ConversationalTestCase(
        turns=[
            Turn(role="user", content="My name is Alice and I'm allergic to peanuts."),
            Turn(role="assistant", content="Thank you for letting me know, Alice. I'll make sure to avoid any peanut-containing recommendations."),
            Turn(role="user", content="What desserts can you recommend?"),
            Turn(role="assistant", content="I can recommend chocolate cake, vanilla ice cream, or fruit salad. All of these are peanut-free, which is important given your allergy.")
        ]
    )
    
    evaluate(test_cases=[test_case], metrics=[metric])
    print("\n")


def demo_goal_accuracy():
    """Demonstrate Goal Accuracy metric"""
    print("\n" + "="*60)
    print("Demo: Goal Accuracy Metric")
    print("="*60)
    
    metric = GoalAccuracyMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    # Conversation with a clear goal (booking a flight)
    test_case = ConversationalTestCase(
        turns=[
            Turn(role="user", content="I need to book a flight from New York to London."),
            Turn(role="assistant", content="I can help you with that. What date would you like to travel?"),
            Turn(role="user", content="Next Friday, preferably in the morning."),
            Turn(role="assistant", content="I found a flight departing JFK at 8:00 AM on Friday. Would you like me to book it?")
        ]
    )
    
    evaluate(test_cases=[test_case], metrics=[metric])
    print("\n")


def demo_multi_turn_conversation():
    """Comprehensive multi-turn conversation evaluation"""
    print("\n" + "="*60)
    print("Demo: Multi-Turn Conversation Evaluation")
    print("="*60)
    
    role_adherence = RoleAdherenceMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    topic_adherence = TopicAdherenceMetric(
        threshold=0.7,
        model="gpt-4o-mini",
        include_reason=True
    )
    
    test_case = ConversationalTestCase(
        chatbot_role="You are a helpful travel assistant. Provide accurate information and be friendly.",
        turns=[
            Turn(role="user", content="I'm planning a trip to Japan. What should I know?"),
            Turn(role="assistant", content="Japan is a wonderful destination! The best times to visit are spring (cherry blossoms) and autumn (fall foliage). You'll need to check visa requirements based on your nationality."),
            Turn(role="user", content="What about the language barrier?"),
            Turn(role="assistant", content="While Japanese is the primary language, many signs in tourist areas have English translations. Learning basic phrases like 'hello' (konnichiwa) and 'thank you' (arigatou) is helpful.")
        ]
    )
    
    evaluate(
        test_cases=[test_case],
        metrics=[role_adherence, topic_adherence]
    )
    print("\n")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or export it.")
        exit(1)
    
    print("\n" + "="*60)
    print("DeepEval Conversational Metrics Demo")
    print("="*60)
    
    demo_role_adherence()
    demo_topic_adherence()
    demo_knowledge_retention()
    demo_goal_accuracy()
    demo_multi_turn_conversation()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60 + "\n")

