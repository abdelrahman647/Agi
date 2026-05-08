# TAHER: Autonomous General Intelligence for Windows 11

## System Architecture

TAHER is designed as a modular, local-first AGI system. The architecture centers around a **Central Orchestrator** that mediates communication between specialized modules and maintains the global state.

### 1. High-Level Diagram
```text
[ GUI (PySide6) ] <---> [ Central Orchestrator ] <---> [ Memory (ChromaDB) ]
                              |      |      |
        ______________________|      |      |______________________
       |              |              |              |              |
[ Planner ]    [ Model Pool ]    [ Toolset ]    [ Self-Upgrade ] [ Multi-Modal ]
       |              |              |              |              |
 (Reasoning)    (Ollama/Local)  (OS/Apps/Web)  (VM Sandbox)    (Vision/Voice)
```

### 2. Core Modules

#### A. Central Orchestrator
- **State Manager:** Tracks active tasks, sub-goals, and environmental context.
- **Dispatcher:** Routes messages between modules (e.g., Vision -> Planner -> Tool).
- **Event Bus:** Async message queue for real-time updates (voice, logs, system events).

#### B. Hierarchical Planner
- **Goal Decomposition:** Breaks complex instructions into actionable sub-tasks.
- **Reflection Loop:** Analyzes tool outputs to verify progress or pivot strategies.
- **Chain-of-Thought:** Internal reasoning trace logged for transparency and self-improvement.

#### C. Memory System (ChromaDB)
- **Semantic Memory:** Knowledge base, documentation, and learned facts.
- **Episodic Memory:** History of previous tasks, successes, and failures.
- **Project Memory:** Context-specific codebases and configurations.
- **Lifestyle Memory:** User preferences and habit tracking.

#### D. Model Strategy (Optimized for RTX 4060 8GB)
- **Primary Brain:** `qwen3:8b` (Quantized for low VRAM overhead).
- **Coding:** `qwen2.5-coder:7b`.
- **Vision:** Florence-2 (compact yet powerful OCR/detection) + Moondream (description).
- **Audio:** Faster-Whisper (Large-v3-distil) for STT; Piper for low-latency TTS.

#### E. Self-Modification Engine
- **Git Flow:** All self-edits occur on branches.
- **Linux VM Bridge:** Uses SSH to transfer code to a Linux VM for testing.
- **Safety Protocol:** Automated regression tests + Manual approval gate.
- **Rollback:** Atomic git resets on any validation failure.

#### F. Multi-Modal Pipeline
- **Vision:** Continuous screenshot analysis + OCR. Uses visual anchors for UI automation.
- **Voice:** VAD (Voice Activity Detection) -> Whisper -> Orchestrator -> Piper.
- **3D (Blender):** Dynamic Python script generation for `bpy`. Visual feedback loop (Render -> Analyze -> Adjust).

### 3. Folder Structure
```
/TAHER
├── core/               # Orchestrator, State, Event Bus
├── models/             # Ollama wrappers, Vision/STT/TTS drivers
├── memory/             # ChromaDB integration, Embedding logic
├── tools/              # PyAutoGUI, Playwright, Win32, Custom APIs
├── agents/             # Specialized sub-agents (e.g., Coder, Researcher)
├── voice/              # Audio streaming, VAD, Wake-word
├── vision/             # Screen capture, OCR, Object detection
├── sandbox/            # SSH Bridge to Linux VM, Test scripts
├── gui/                # PySide6 Components, Glassmorphism Styles
├── blender/            # BPY scripts, Render analysis
├── planner/            # Task decomposition, Reasoning loops
├── self_upgrade/       # Git logic, Diff generator, Safety checks
├── tests/              # System and Unit tests
└── configs/            # YAML/JSON configs for models and tools
```

### 4. Hardware Optimization for RTX 4060
- **VRAM Management:** Use 4-bit/5-bit quantization for Ollama.
- **Async Execution:** Vision and Voice run on separate threads/processes to avoid blocking reasoning.
- **Model Offloading:** Dynamically load/unload Vision models if VRAM exceeds 7.5GB.

### 5. Multi-Agent Coordination
- **Lead Agent:** The main TAHER personality.
- **Sub-Agents:** Specialized instances (e.g., "Developer-Agent", "Analyst-Agent") spawned for concurrent sub-tasks.

### 6. Security & Safety
- **Permission Tiers:** Filesystem access restricted to specific directories by default.
- **Process Isolation:** Sandbox testing for all self-generated code.
- **Approval Gates:** High-risk actions (code deployment, system setting changes) require user confirmation via GUI.
