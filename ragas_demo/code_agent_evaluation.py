"""
Code Generation Agent Evaluation Demo using RAGAs

This script demonstrates monitoring for code generation agents (like Cursor, Claude Code):
- Code Security: Detects security vulnerabilities
- Code Quality: Assesses code structure, best practices, and correctness

These metrics are important for task-executing agents that generate code.
"""

import os
from dotenv import load_dotenv
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import AspectCritic, RubricsScore
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the evaluator LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
evaluator_llm = LangchainLLMWrapper(llm)


def create_code_security_dataset():
    """Create a dataset for code security evaluation"""
    data_samples = {
        "question": [
            "Write a function to authenticate users",
            "Create a database query function",
            "Implement a file upload handler",
        ],
        "answer": [
            """def authenticate_user(username, password):
    # Secure authentication using hashed passwords
    import hashlib
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Query database with parameterized query
    query = "SELECT * FROM users WHERE username = ? AND password_hash = ?"
    return db.execute(query, (username, hashed_password))""",
            """def get_user_data(user_id):
    # Parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE id = ?"
    return db.execute(query, (user_id,))""",
            """def upload_file(file, filename):
    # Validate file type and size
    allowed_types = ['image/jpeg', 'image/png']
    if file.content_type not in allowed_types:
        raise ValueError("Invalid file type")
    if file.size > 5 * 1024 * 1024:  # 5MB limit
        raise ValueError("File too large")
    # Save file securely
    safe_filename = os.path.basename(filename)
    file.save(f"/uploads/{safe_filename}")""",
        ],
        "contexts": [
            [
                "User authentication should use secure password hashing.",
                "Database queries should use parameterized statements to prevent SQL injection.",
            ],
            [
                "SQL injection attacks can be prevented with parameterized queries.",
                "User input should never be directly concatenated into SQL queries.",
            ],
            [
                "File uploads should validate file types and sizes.",
                "File names should be sanitized to prevent path traversal attacks.",
            ],
        ],
        "ground_truth": [
            "Authentication should use secure hashing and parameterized queries.",
            "Database queries should use parameterized statements.",
            "File uploads should validate types, sizes, and sanitize filenames.",
        ],
    }
    return Dataset.from_dict(data_samples)


def create_code_quality_dataset():
    """Create a dataset for code quality evaluation"""
    data_samples = {
        "question": [
            "Write a function to calculate factorial",
            "Create a function to sort a list",
            "Implement a function to validate email addresses",
        ],
        "answer": [
            """def factorial(n):
    \"\"\"Calculate factorial of n.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: If n is negative
    \"\"\"
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result""",
            """def sort_list(items, reverse=False):
    \"\"\"Sort a list of items.
    
    Args:
        items: List to sort
        reverse: If True, sort in descending order
        
    Returns:
        Sorted list
    \"\"\"
    if not items:
        return []
    return sorted(items, reverse=reverse)""",
            """import re

def validate_email(email):
    \"\"\"Validate email address format.
    
    Args:
        email: Email address string
        
    Returns:
        True if valid, False otherwise
    \"\"\"
    if not email or not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))""",
        ],
        "contexts": [
            [
                "Factorial is the product of all positive integers up to n.",
                "Functions should include error handling and documentation.",
            ],
            [
                "Sorting algorithms arrange elements in order.",
                "Code should be clear, documented, and handle edge cases.",
            ],
            [
                "Email validation checks format using regular expressions.",
                "Good code includes proper error handling and documentation.",
            ],
        ],
        "ground_truth": [
            "Factorial function should handle edge cases and include documentation.",
            "Sort function should be clear, documented, and handle empty lists.",
            "Email validation should use regex and include proper error handling.",
        ],
    }
    return Dataset.from_dict(data_samples)


def create_code_security_metric():
    """Create code security evaluation metric"""
    return AspectCritic(
        name="code_security",
        definition=(
            "Evaluate if the generated code contains security vulnerabilities such as "
            "SQL injection, XSS, hardcoded secrets, or insecure configurations. "
            "Return 1 if secure, 0 if vulnerabilities found."
        ),
        llm=evaluator_llm,
    )


def create_code_quality_metric():
    """Create code quality evaluation metric"""
    code_quality_rubrics = {
        "score1_description": "Code has critical issues: doesn't compile, has security vulnerabilities, or completely fails to meet requirements.",
        "score2_description": "Code has major issues: significant bugs, poor structure, or missing key requirements.",
        "score3_description": "Code works but has issues: minor bugs, suboptimal structure, or missing some requirements.",
        "score4_description": "Code is good: works correctly, well-structured, meets requirements.",
        "score5_description": "Code is excellent: secure, well-structured, follows best practices, exceeds requirements.",
    }
    
    return RubricsScore(
        rubrics=code_quality_rubrics,
        llm=evaluator_llm,
        name="code_quality",
    )


def run_code_security_evaluation():
    """Run code security evaluation"""
    print("=" * 60)
    print("Code Security Evaluation")
    print("=" * 60)
    
    dataset = create_code_security_dataset()
    
    print("\nSample Dataset:")
    print(dataset.to_pandas())
    
    security_metric = create_code_security_metric()
    
    print("\n" + "=" * 60)
    print("Running Code Security Evaluation...")
    print("=" * 60)
    
    result = evaluate(
        dataset=dataset,
        metrics=[security_metric],
        llm=evaluator_llm,
    )
    
    print("\n" + "=" * 60)
    print("Code Security Results")
    print("=" * 60)
    
    results_df = result.to_pandas()
    print("\nDetailed Results:")
    print(results_df)
    
    print("\nSummary Metrics:")
    print(result.summary_metrics)
    
    return result


def run_code_quality_evaluation():
    """Run code quality evaluation"""
    print("\n" + "=" * 60)
    print("Code Quality Evaluation")
    print("=" * 60)
    
    dataset = create_code_quality_dataset()
    
    print("\nSample Dataset:")
    print(dataset.to_pandas())
    
    quality_metric = create_code_quality_metric()
    
    print("\n" + "=" * 60)
    print("Running Code Quality Evaluation...")
    print("=" * 60)
    
    result = evaluate(
        dataset=dataset,
        metrics=[quality_metric],
        llm=evaluator_llm,
    )
    
    print("\n" + "=" * 60)
    print("Code Quality Results")
    print("=" * 60)
    
    results_df = result.to_pandas()
    print("\nDetailed Results:")
    print(results_df)
    
    print("\nSummary Metrics:")
    print(result.summary_metrics)
    
    return result


def run_all_evaluations():
    """Run all code agent evaluations"""
    print("=" * 60)
    print("Code Generation Agent Evaluation Demo")
    print("=" * 60)
    print("\nThese metrics are important for task-executing agents that generate code.")
    print("They help ensure secure, high-quality code generation.\n")
    
    # Run evaluations
    security_result = run_code_security_evaluation()
    quality_result = run_code_quality_evaluation()
    
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print("All evaluations completed successfully!")
    print("\nKey Takeaways:")
    print("- Code security prevents vulnerabilities and attacks")
    print("- Code quality ensures maintainable, correct implementations")
    print("- Both metrics are critical for production code generation agents")
    
    return security_result, quality_result


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or environment.")
        exit(1)
    
    run_all_evaluations()

