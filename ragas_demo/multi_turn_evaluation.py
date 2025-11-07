"""
Multi-Turn Conversation Evaluation Demo using RAGAs

This script demonstrates evaluation of multi-turn conversations:
- Agent Goal Accuracy: Measures if the agent achieved the user's goal
- Tool Call Accuracy: Evaluates correct tool usage
- Conversation quality metrics
"""

import os
from dotenv import load_dotenv
from ragas.dataset_schema import MultiTurnSample
from ragas.messages import HumanMessage, AIMessage, ToolMessage, ToolCall
from ragas.metrics import (
    AgentGoalAccuracyWithoutReference,
    AgentGoalAccuracyWithReference,
    ToolCallAccuracy,
)
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the evaluator LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
evaluator_llm = LangchainLLMWrapper(llm)


def create_restaurant_booking_sample():
    """Create a sample multi-turn conversation for restaurant booking"""
    return MultiTurnSample(
        user_input=[
            HumanMessage(content="Hey, book a table at the nearest best Chinese restaurant for 8:00pm"),
            AIMessage(
                content="Sure, let me find the best options for you.",
                tool_calls=[
                    ToolCall(
                        name="restaurant_search",
                        args={"cuisine": "Chinese", "time": "8:00pm"}
                    )
                ]
            ),
            ToolMessage(content="Found a few options: 1. Golden Dragon, 2. Jade Palace"),
            AIMessage(
                content="I found some great options: Golden Dragon and Jade Palace. Which one would you prefer?"
            ),
            HumanMessage(content="Let's go with Golden Dragon."),
            AIMessage(
                content="Great choice! I'll book a table for 8:00pm at Golden Dragon.",
                tool_calls=[
                    ToolCall(
                        name="restaurant_book",
                        args={"name": "Golden Dragon", "time": "8:00pm"}
                    )
                ]
            ),
            ToolMessage(content="Table booked at Golden Dragon for 8:00pm."),
            AIMessage(content="Your table at Golden Dragon is booked for 8:00pm. Enjoy your meal!"),
            HumanMessage(content="thanks"),
        ],
        reference="Table booked at one of the Chinese restaurants at 8 pm"
    )


def create_weather_sample():
    """Create a sample multi-turn conversation for weather queries"""
    return MultiTurnSample(
        user_input=[
            HumanMessage(content="What's the weather like in New York right now?"),
            AIMessage(
                content="Let me check the current weather in New York for you.",
                tool_calls=[
                    ToolCall(
                        name="weather_check",
                        args={"location": "New York"}
                    )
                ]
            ),
            ToolMessage(content="Current temperature in New York is 75°F and it's partly cloudy."),
            AIMessage(content="The current temperature in New York is 75°F and it's partly cloudy."),
            HumanMessage(content="Can you convert that to Celsius?"),
            AIMessage(
                content="Let me convert that to Celsius for you.",
                tool_calls=[
                    ToolCall(
                        name="temperature_conversion",
                        args={"temperature_fahrenheit": 75}
                    )
                ]
            ),
            ToolMessage(content="75°F is approximately 23.9°C."),
            AIMessage(content="75°F is approximately 23.9°C."),
        ],
        reference_tool_calls=[
            ToolCall(name="weather_check", args={"location": "New York"}),
            ToolCall(name="temperature_conversion", args={"temperature_fahrenheit": 75})
        ]
    )


async def evaluate_agent_goal_accuracy():
    """Evaluate agent goal accuracy with and without reference"""
    print("=" * 60)
    print("Agent Goal Accuracy Evaluation")
    print("=" * 60)
    
    sample = create_restaurant_booking_sample()
    
    print("\nConversation Sample:")
    for message in sample.user_input:
        print(f"  {type(message).__name__}: {message.content}")
    
    # Evaluate with reference
    scorer_with_ref = AgentGoalAccuracyWithReference(llm=evaluator_llm)
    result_with_ref = await scorer_with_ref.multi_turn_ascore(sample)
    
    print("\n" + "=" * 60)
    print("Agent Goal Accuracy (With Reference)")
    print("=" * 60)
    print(f"Score: {result_with_ref.score}")
    print(f"Reasoning: {result_with_ref.reasoning}")
    
    # Evaluate without reference
    scorer_without_ref = AgentGoalAccuracyWithoutReference(llm=evaluator_llm)
    result_without_ref = await scorer_without_ref.multi_turn_ascore(sample)
    
    print("\n" + "=" * 60)
    print("Agent Goal Accuracy (Without Reference)")
    print("=" * 60)
    print(f"Score: {result_without_ref.score}")
    print(f"Reasoning: {result_without_ref.reasoning}")
    
    return result_with_ref, result_without_ref


async def evaluate_tool_call_accuracy():
    """Evaluate tool call accuracy"""
    print("\n" + "=" * 60)
    print("Tool Call Accuracy Evaluation")
    print("=" * 60)
    
    sample = create_weather_sample()
    
    print("\nConversation Sample:")
    for message in sample.user_input:
        if hasattr(message, 'tool_calls') and message.tool_calls:
            print(f"  {type(message).__name__}: {message.content}")
            print(f"    Tool Calls: {[tc.name for tc in message.tool_calls]}")
        else:
            print(f"  {type(message).__name__}: {message.content}")
    
    scorer = ToolCallAccuracy()
    result = await scorer.multi_turn_ascore(sample)
    
    print("\n" + "=" * 60)
    print("Tool Call Accuracy Results")
    print("=" * 60)
    print(f"Score: {result.score}")
    print(f"Reasoning: {result.reasoning}")
    
    return result


async def run_multi_turn_evaluation():
    """Run all multi-turn evaluations"""
    print("=" * 60)
    print("Multi-Turn Conversation Evaluation Demo")
    print("=" * 60)
    
    # Evaluate agent goal accuracy
    goal_results = await evaluate_agent_goal_accuracy()
    
    # Evaluate tool call accuracy
    tool_results = await evaluate_tool_call_accuracy()
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print("All evaluations completed successfully!")
    
    return goal_results, tool_results


if __name__ == "__main__":
    import asyncio
    
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        exit(1)
    
    asyncio.run(run_multi_turn_evaluation())

