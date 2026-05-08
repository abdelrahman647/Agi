# Setup script for TAHER on Windows 11

Write-Host "Setting up TAHER environment..." -ForegroundColor Cyan

# Check for Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python not found. Please install it from python.org" -ForegroundColor Red
    exit
}

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Check for Ollama
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama not found. Please install it from ollama.com" -ForegroundColor Yellow
} else {
    Write-Host "Pulling models..." -ForegroundColor Green
    ollama pull qwen3:8b
    ollama pull qwen2.5-coder:7b
    ollama pull moondream
}

Write-Host "Setup complete. Run '.\venv\Scripts\Activate.ps1' and then 'python main.py' to start." -ForegroundColor Green
