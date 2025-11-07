"""
Code Generation Agent Monitoring Demo

This script demonstrates monitoring for code generation agents (like Cursor, Claude Code).
It includes metrics for code security, correctness, and quality.
"""

import os
from dotenv import load_dotenv
from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

# Load environment variables
load_dotenv()

def demo_code_security():
    """Demonstrate code security monitoring"""
    print("\n" + "="*60)
    print("Demo: Code Security Monitoring")
    print("="*60)
    
    code_security_metric = GEval(
        name="Code Security",
        criteria="Evaluate if the generated code contains security vulnerabilities such as SQL injection, XSS, hardcoded secrets, insecure configurations, or other security issues. Return 0 if vulnerabilities found, 1 if secure.",
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT
        ],
        model="gpt-4o-mini",
        threshold=0.95,  # Very high threshold for security
        include_reason=True
    )
    
    test_cases = [
        # Secure code example
        LLMTestCase(
            input="Create a function to query user data by ID",
            actual_output="```python\nimport sqlite3\nfrom typing import Optional\n\ndef get_user_by_id(user_id: int) -> Optional[dict]:\n    conn = sqlite3.connect('database.db')\n    cursor = conn.cursor()\n    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))\n    result = cursor.fetchone()\n    conn.close()\n    return dict(result) if result else None\n```"
        ),
        # Potentially insecure code (for testing)
        LLMTestCase(
            input="Create a login function",
            actual_output="```python\ndef login(username, password):\n    # Use parameterized queries and proper authentication\n    # Store passwords with bcrypt hashing\n    # Implement rate limiting\n    # Use secure session management\n    pass\n```"
        ),
        # Secure API key handling
        LLMTestCase(
            input="How should I store API keys?",
            actual_output="```python\nimport os\nfrom dotenv import load_dotenv\n\nload_dotenv()\n\n# Store API keys in environment variables, never in code\napi_key = os.getenv('API_KEY')\nif not api_key:\n    raise ValueError('API_KEY not found in environment')\n```"
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[code_security_metric])
    print("\n")


def demo_code_correctness():
    """Demonstrate code correctness monitoring"""
    print("\n" + "="*60)
    print("Demo: Code Correctness Monitoring")
    print("="*60)
    
    code_correctness_metric = GEval(
        name="Code Correctness",
        criteria="Evaluate if the generated code correctly implements the requested functionality. Consider syntax errors, logical errors, missing requirements, and whether the code would work as intended. Return 1 if correct, 0 if incorrect.",
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT
        ],
        model="gpt-4o-mini",
        threshold=0.8,
        include_reason=True
    )
    
    test_cases = [
        # Correct implementation
        LLMTestCase(
            input="Create a function that calculates the factorial of a number",
            actual_output="```python\ndef factorial(n: int) -> int:\n    if n < 0:\n        raise ValueError('Factorial is not defined for negative numbers')\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\n```",
            expected_output="A function that correctly calculates factorial, handling edge cases"
        ),
        # Correct with error handling
        LLMTestCase(
            input="Create a function to divide two numbers",
            actual_output="```python\ndef divide(a: float, b: float) -> float:\n    if b == 0:\n        raise ZeroDivisionError('Cannot divide by zero')\n    return a / b\n```",
            expected_output="A function that divides two numbers with proper error handling"
        ),
        # Correct implementation with type hints
        LLMTestCase(
            input="Create a function to find the maximum value in a list",
            actual_output="```python\nfrom typing import List\n\ndef find_max(numbers: List[float]) -> float:\n    if not numbers:\n        raise ValueError('List cannot be empty')\n    return max(numbers)\n```",
            expected_output="A function that finds the maximum value in a list"
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[code_correctness_metric])
    print("\n")


def demo_code_quality():
    """Demonstrate code quality monitoring"""
    print("\n" + "="*60)
    print("Demo: Code Quality Monitoring")
    print("="*60)
    
    code_quality_metric = GEval(
        name="Code Quality",
        criteria="Evaluate the quality of the generated code. Consider readability, maintainability, best practices, proper error handling, documentation, and adherence to coding standards. Return 1 if high quality, 0 if low quality.",
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT
        ],
        model="gpt-4o-mini",
        threshold=0.7,
        include_reason=True
    )
    
    test_cases = [
        # High quality code
        LLMTestCase(
            input="Create a function to validate email addresses",
            actual_output="```python\nimport re\nfrom typing import Optional\n\ndef validate_email(email: str) -> bool:\n    \"\"\"\n    Validate an email address format.\n    \n    Args:\n        email: The email address to validate\n    \n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not email or not isinstance(email, str):\n        return False\n    \n    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'\n    return bool(re.match(pattern, email))\n```"
        ),
        # Good quality with error handling
        LLMTestCase(
            input="Create a function to read a JSON file",
            actual_output="```python\nimport json\nfrom pathlib import Path\nfrom typing import Any, Optional\n\ndef read_json_file(file_path: str) -> Optional[dict[str, Any]]:\n    \"\"\"Read and parse a JSON file.\"\"\"\n    try:\n        with open(file_path, 'r', encoding='utf-8') as f:\n            return json.load(f)\n    except FileNotFoundError:\n        raise FileNotFoundError(f'File not found: {file_path}')\n    except json.JSONDecodeError as e:\n        raise ValueError(f'Invalid JSON: {e}')\n```"
        ),
        # Quality code with proper structure
        LLMTestCase(
            input="Create a class to represent a user",
            actual_output="```python\nfrom dataclasses import dataclass\nfrom typing import Optional\nfrom datetime import datetime\n\n@dataclass\nclass User:\n    \"\"\"Represents a user in the system.\"\"\"\n    id: int\n    username: str\n    email: str\n    created_at: datetime\n    is_active: bool = True\n    \n    def __post_init__(self):\n        if not self.username:\n            raise ValueError('Username cannot be empty')\n        if '@' not in self.email:\n            raise ValueError('Invalid email format')\n```"
        )
    ]
    
    evaluate(test_cases=test_cases, metrics=[code_quality_metric])
    print("\n")


def demo_comprehensive_code_evaluation():
    """Comprehensive code evaluation with multiple metrics"""
    print("\n" + "="*60)
    print("Demo: Comprehensive Code Evaluation")
    print("="*60)
    
    security_metric = GEval(
        name="Code Security",
        criteria="Evaluate if the code contains security vulnerabilities. Return 0 if vulnerabilities found, 1 if secure.",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model="gpt-4o-mini",
        threshold=0.95,
        include_reason=True
    )
    
    correctness_metric = GEval(
        name="Code Correctness",
        criteria="Evaluate if the code correctly implements the requested functionality. Return 1 if correct, 0 if incorrect.",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model="gpt-4o-mini",
        threshold=0.8,
        include_reason=True
    )
    
    quality_metric = GEval(
        name="Code Quality",
        criteria="Evaluate code quality including readability, maintainability, and best practices. Return 1 if high quality, 0 if low quality.",
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
        model="gpt-4o-mini",
        threshold=0.7,
        include_reason=True
    )
    
    test_case = LLMTestCase(
        input="Create a secure function to authenticate users",
        actual_output="```python\nimport hashlib\nimport secrets\nfrom typing import Optional, Tuple\n\ndef authenticate_user(username: str, password: str, stored_hash: str, salt: str) -> bool:\n    \"\"\"\n    Authenticate a user by comparing password hash.\n    Uses secure hashing and constant-time comparison.\n    \"\"\"\n    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)\n    stored_hash_bytes = bytes.fromhex(stored_hash)\n    return secrets.compare_digest(password_hash, stored_hash_bytes)\n```"
    )
    
    evaluate(
        test_cases=[test_case],
        metrics=[security_metric, correctness_metric, quality_metric]
    )
    print("\n")


if __name__ == "__main__":
    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not found in environment variables.")
        print("Please set it in your .env file or export it.")
        exit(1)
    
    print("\n" + "="*60)
    print("DeepEval Code Generation Agent Monitoring Demo")
    print("="*60)
    print("Priority: MEDIUM - Important for task-executing agents")
    print("="*60)
    
    demo_code_security()
    demo_code_correctness()
    demo_code_quality()
    demo_comprehensive_code_evaluation()
    
    print("\n" + "="*60)
    print("Demo Complete!")
    print("="*60)
    print("\nKey Takeaways:")
    print("- Use threshold >= 0.95 for security (critical)")
    print("- Use threshold >= 0.8 for correctness")
    print("- Use threshold >= 0.7 for quality")
    print("- Monitor all three aspects for code generation agents")
    print("="*60 + "\n")

