# Contributing to Jarvis-V

We welcome contributions to make Jarvis-V a better, faster, and more robust offline AI assistant! 

## 💡 How you can help
- **Cross-Platform TTS/STT Support**: Currently leaning heavily on macOS `say`. Implementing `edge-tts` or `pyttsx3` formally would be massive.
- **New Skills**: Contribute generic plugins (e.g., controlling Spotify, smart home IoT, fetching stock data).
- **Wake-Word Efficiency**: Integrations for `pvporcupine` or similar low-power wait-loops.

## 🛠️ Local Development Setup

1. Fork the repository and install dependencies inside a newly activated `venv`.
2. Keep edits localized to their relevant subsystems inside `core/`.
3. Test your voice commands manually before pushing!

## 🔄 Pull Request Rules
Please submit a descriptive PR detailing what subsystem you modified. We enforce Python PEP8 style where applicable.

Please see the [Issue Tracker](https://github.com/pronzzz/jarvis-v/issues) for planned roadmap items.
