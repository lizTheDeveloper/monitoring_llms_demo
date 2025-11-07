#!/bin/bash
# Setup script for RAGAs demo

set -e  # Exit on error

echo "Setting up RAGAs demo environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "Creating .env file template..."
    echo "OPENAI_API_KEY=your_api_key_here" > .env
    echo "Please edit .env and add your OPENAI_API_KEY"
else
    echo ".env file already exists"
fi

echo ""
echo "Setup complete!"
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "Then you can run the demo scripts:"
echo "  python basic_rag_evaluation.py"
echo "  python advanced_metrics.py"
echo "  python multi_turn_evaluation.py"

