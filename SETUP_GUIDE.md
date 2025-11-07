# Setup Guide

## Prerequisites
- Python 3.8+
- OpenAI API key

## Quick Setup

1. **Set API key**: `export OPENAI_API_KEY=your_key` (or create `.env` file)
2. **Navigate to demo**: `cd deepeval_demo/` (or `ragas_demo/`, `deepchecks/`)
3. **Create venv**: `python3 -m venv venv` (macOS/Linux) or `python -m venv venv` (Windows)
4. **Activate**: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
5. **Install**: `pip install -r requirements.txt`
6. **Run**: `python <script_name>.py`

## Detailed Setup by Demo

Each demo follows the same pattern:

```bash
# Navigate to demo directory
cd <demo_directory>

# Create and activate virtual environment  
python3 -m venv venv              # macOS/Linux
python -m venv venv               # Windows

source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# Install dependencies
pip install -r requirements.txt

# Run demos
python <script_name>.py
```

**Available demos**:
- `deepeval_demo/` - LLM evaluation (8 scripts)
- `ragas_demo/` - RAG evaluation (6 scripts)
- `deepchecks/` - Data validation (5 scripts)

See each directory's README for script descriptions.

## Troubleshooting

**Python not found**:
- macOS/Linux: Check `python3 --version`
- Windows: Try `py --version` or add Python to PATH

**Virtual environment activation fails**:
- macOS/Linux: Ensure using `source venv/bin/activate`
- Windows: Try `.\venv\Scripts\activate`

**API key not working**:
- Check `.env` file in correct directory
- Or set environment variable: `export OPENAI_API_KEY=your_key` (macOS/Linux) or `set OPENAI_API_KEY=your_key` (Windows)

**Import errors**:
1. Verify venv is activated
2. Run `pip install -r requirements.txt`
3. Check using correct Python interpreter

## Next Steps

1. Run demos in each directory
2. Read [ALIGNMENT_METRICS.md](ALIGNMENT_METRICS.md) for metric details
3. See [IMPLEMENTING_METRICS.md](IMPLEMENTING_METRICS.md) for code examples
4. Review [PRODUCTION_MONITORING.md](PRODUCTION_MONITORING.md) for production guidance

