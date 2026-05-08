# TAHER: Autonomous General Intelligence for Windows 11

TAHER is a local-first, persistent, and self-improving AGI system designed to operate as an autonomous agent on Windows 11. It controls your system, learns new skills, researches independently, and manages its own code growth safely.

## 🚀 Key Features

- **Autonomous Research:** Continuously learns and researches in the background when you are idle.
- **Self-Modification Engine:** Safely updates its own source code via Git and a Linux VM sandbox.
- **Multi-Modal Brain:** Uses local models for Vision (Moondream/Florence-2), Speech (Faster-Whisper/Piper), and Reasoning (Qwen3).
- **System Control:** Automates Windows workflows using PyAutoGUI, Playwright, and Win32 APIs.
- **Persistent Memory:** Long-term episodic and semantic memory powered by ChromaDB.
- **Blender Integration:** Generates and iterates on 3D scenes via Python (`bpy`) automation.
- **Native GUI:** A futuristic dark-mode dashboard built with PySide6.

## 🛠️ Architecture

TAHER is built with a modular, plugin-based architecture:
- `core/`: Central Orchestrator, Event Bus, and State Manager.
- `agents/`: Specialized sub-agents (Researcher, Coder, Analyst).
- `memory/`: Vector-based memory retrieval.
- `planner/`: Hierarchical goal decomposition and reasoning.
- `tools/`: OS, Browser, and Notification integrations.
- `sandbox/`: SSH-based Linux VM testing bridge.

## 💻 Hardware Requirements

- **OS:** Windows 11
- **GPU:** NVIDIA RTX 4060 (8GB VRAM minimum)
- **RAM:** 16GB+

## ⚙️ Installation

### 1. Prerequisites
- **Python 3.10+**
- **Ollama:** [Download Ollama](https://ollama.com/) and pull the models:
  ```bash
  ollama pull qwen3:8b
  ollama pull moondream
  ```
- **Git:** Installed and configured.

### 2. Automatic Setup
Run the included PowerShell script as Administrator:
```powershell
.\setup.ps1
```

### 3. Manual Setup
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## 🏃 Usage

1. **Start the AGI:**
   ```bash
   python gui/dashboard.py
   ```
2. **Autonomous Mode:** TAHER will automatically pick up tasks from its background queue (defined in `configs/config.yaml`) when the user is inactive.
3. **Notifications:** You will receive native Windows toast notifications when background research or code updates are complete.

## 🛡️ Safety & Security

TAHER operates under a strict safety protocol:
- **Git Flow:** Every self-modification is performed on a new branch.
- **VM Sandboxing:** Code is automatically tested in a Linux VM via the SSH bridge before merging.
- **Human-in-the-loop:** Critical system changes or code updates require user approval via the GUI.

## 📄 License
This project is for private AGI research and development.
