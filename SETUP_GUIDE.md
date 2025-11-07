# Setup Guide

This guide provides detailed setup instructions for running the demos on macOS, Linux, and Windows.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (for LLM-based evaluations)
- Virtual environment (recommended)

## Quick Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd monitoring_llms_demo
```

### 2. Set Up Environment Variables

Create a `.env` file in each demo directory (or at the root):

```bash
OPENAI_API_KEY=your_api_key_here
```

**Note**: You can also set this as a system environment variable if you prefer.

### 3. Choose Your Demo

Each demo is in its own directory with its own virtual environment. Follow the instructions below for the demo you want to run.

---

## DeepEval Demo Setup

### macOS/Linux

```bash
cd deepeval_demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```cmd
cd deepeval_demo
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Note**: If `python` doesn't work, try `py` instead.

### Running the Demos

```bash
# macOS/Linux
python basic_metrics.py
python rag_metrics.py
python conversational_metrics.py

# Windows (same commands)
python basic_metrics.py
python rag_metrics.py
python conversational_metrics.py
```

---

## RAGAs Demo Setup

### macOS/Linux

```bash
cd ragas_demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```cmd
cd ragas_demo
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Demos

```bash
python basic_rag_evaluation.py
python advanced_metrics.py
python multi_turn_evaluation.py
```

---

## DeepChecks Demo Setup

### macOS/Linux

```bash
cd deepchecks
python3 -m venv venv  # if creating new venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```cmd
cd deepchecks
python -m venv venv  # if creating new venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Demo

```bash
python example_tabular.py
```

Results will be saved as HTML reports in the `results/` directory.

---

## Troubleshooting

### Python Not Found

**macOS/Linux**: Make sure Python 3 is installed:
```bash
python3 --version
```

**Windows**: Make sure Python is in your PATH, or use the Python Launcher:
```cmd
py --version
```

### Virtual Environment Issues

**macOS/Linux**: If activation fails, make sure you're using the correct path:
```bash
source venv/bin/activate
```

**Windows**: If activation fails, try:
```cmd
.\venv\Scripts\activate
```

### API Key Issues

Make sure your `.env` file is in the correct directory and contains:
```
OPENAI_API_KEY=your_actual_key_here
```

You can also set it as an environment variable:
- **macOS/Linux**: `export OPENAI_API_KEY=your_key`
- **Windows**: `set OPENAI_API_KEY=your_key` (Command Prompt) or `$env:OPENAI_API_KEY="your_key"` (PowerShell)

### Import Errors

If you get import errors, make sure:
1. Your virtual environment is activated
2. You've installed requirements: `pip install -r requirements.txt`
3. You're using the correct Python interpreter

### Path Issues on Windows

If you encounter path issues:
- Use forward slashes in Python code: `path/to/file`
- Or use raw strings: `r"path\to\file"`
- Or use `pathlib.Path` for cross-platform compatibility

---

## Platform-Specific Notes

### macOS
- All demos have been tested on macOS
- Use `python3` command and `source venv/bin/activate` for virtual environments
- Python 3.8+ is required

### Windows
- All demos are compatible with Windows
- Use `python` command (or `py` if `python` isn't in PATH) and `venv\Scripts\activate` for virtual environments
- PowerShell and Command Prompt are both supported
- If you encounter path issues, use forward slashes in Python code or raw strings for file paths

### Linux
- Same instructions as macOS
- Use `python3` command and `source venv/bin/activate`

---

## Next Steps

Once you have everything set up:
1. Run the basic demos to see the frameworks in action
2. Read [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) to understand the metrics
3. Check out [IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md) for code examples
4. Review [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) for production strategies

