#!/usr/bin/env bash
# Setup script for TAHER (Linux/WSL/Sandbox)
# On Windows, use a similar PowerShell script.

echo "Setting up TAHER environment..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Please install it."
    exit 1
fi

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

echo "Setup complete. Use 'source venv/bin/activate' to start."
