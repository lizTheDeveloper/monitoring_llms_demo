#!/bin/bash
# Setup script for DeepEval demo

set -e  # Exit on error

echo "Setting up DeepEval demo environment..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  WARNING: .env file not found!"
    echo "Please create a .env file with your OPENAI_API_KEY:"
    echo "  echo 'OPENAI_API_KEY=your_key_here' > .env"
    echo ""
else
    echo "✓ .env file found"
fi

echo ""
echo "Setup complete! To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""

