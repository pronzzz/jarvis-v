<div align="center">

# 🎙️ JARVIS-V
**The Fully Voice-Driven, Local-First Multilingual AI Assistant**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 📖 Overview
Jarvis-V is a local-first, privacy-respecting voice assistant powered purely by local LLMs via `Ollama` (`llama3`) and lightning fast transcribing via `faster-whisper`. Built to simulate natural ambient computing, Jarvis natively understands code-switched Hindi and English ("Hinglish") and operates entirely offline. 

### Why Jarvis-V?
Current voice assistants suffer from heavy cloud dependence, rigid structures, and poor Indian localization context. Jarvis-V runs on *your* hardware, parses intents securely through an extensible Tool Registry, and operates continuously over a terminal.

---

## 🏗️ Architecture & Features

### 1. Robust Core Voice Loop 
- **`core/listener.py`**: Captures microphone threshold energy and triggers on spoken audio. Auto-adapts dynamically to ambient noise.
- **`core/speech_to_text.py`**: Utilizes offline `faster-whisper` (`tiny.en` variant) running on your CPU for lightning fast transcriptions.
- **`core/llm_engine.py`**: Leverages the local Ollama Python client, natively hooked into Tool calls.
- **`core/text_to_speech.py`**: Wraps the native macOS `say` subprocess. Synthesizing voices like `Rishi` (Indian English) handles heavy Hinglish code-switching smoothly.

### 2. Intelligent Components
- **Short Term Session Memory (`memory/session_memory.py`)**: Wraps short term conversations in a constrained LRU token window to prevent endless history dumps to the LLM.
- **Bilingual Personality Engine (`config/settings.yaml`)**: Dynamically injected system prompts allowing Jarvis to adopt `formal`, `sarcastic`, or `casual` tones.
- **Extensible Tool Registry (`core/tool_registry.py`)**: Seamless JSON Object mapping for Python functions. Currently supports `.skills/time.py` & `.skills/system.py` natively via Ollama Tooling! If you ask Jarvis "What time is it?", it literally calls python to fetch the clock instead of hallucinating.

---

## 🚀 Getting Started

### Prerequisites
- macOS (built for `portaudio` and the native `say` TTS engine).
- [`Ollama`](https://ollama.com) installed and active.

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/pronzzz/jarvis-v.git
cd jarvis-v
```

2. **Boot Virtual Environment and Install Dependencies**
```bash
# macOS requires Portaudio for PyAudio internals
brew install portaudio

python3 -m venv venv
source venv/bin/activate

# Optional: Add compiler flags if PyAudio struggles
# LDFLAGS="-L$(brew --prefix portaudio)/lib" CFLAGS="-I$(brew --prefix portaudio)/include" pip install -r requirements.txt
pip install -r requirements.txt
```

3. **Verify Ollama Model**
Make sure the background runner has pulled the proper Llama 3 parameters.
```bash
ollama pull llama3
```

### Usage

Start the main orchestration loop:
```bash
python main.py
```

It will immediately boot, vocalize "Systems online. At your service.", and listen. Try testing it:
> *"Hey Jarvis, please check the system battery status and tell me the current time."*

---

## 🤝 Community
- Follow the [GUIDE.md](GUIDE.md) to learn how to add your own Python skills!
- See [CONTRIBUTING.md](CONTRIBUTING.md) to help add cross-platform Windows/Linux TTS hooks.
- Please adhere to the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 📄 License
This application is distributed under the [MIT License](LICENSE).
