# 📚 Jarvis-V Comprehensive Guide

This guide describes how to extend Jarvis-V with new skills, adjust its memory, and customize the TTS/STT pipelines.

## 1. Adding a New Skill

Jarvis-V connects Python functions to Ollama natively via the `core/tool_registry.py`.

### Step 1: Create the Python Function
Create a file inside the `skills/` directory, for example, `skills/weather.py`.

```python
# skills/weather.py
def get_weather(location: str) -> str:
    """Returns the weather for a given city."""
    # In a real app, you would make an API request here.
    return f"The weather in {location} is highly likely to be sunny."
```

### Step 2: Register the Tool in `tool_registry.py`
Open `core/tool_registry.py` and import your function. 
Add it to the mapping tuple, and expose its JSON schema to Ollama so Llama3 knows it exists.

```python
from skills.weather import get_weather

class ToolRegistry:
    def __init__(self):
        self.tool_map = {
            "get_current_time": get_current_time,
            "get_weather": get_weather,
        }
    
    def get_ollama_tools(self) -> list:
        return [
            # ... existing tools
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a specific location.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city or location to check."
                            }
                        },
                        "required": ["location"]
                    }
                }
            }
        ]
```

### Step 3: Run Jarvis
When you ask *"Hey Jarvis, what is the weather in Mumbai?"*, Ollama recognizes the intent, calls `get_weather("Mumbai")`, and Jarvis speaks out the result.

## 2. Configuration Settings (`config/settings.yaml`)

You can alter the entire personality of Jarvis, as well as the text-to-speech rendering speed and LLM engine via the configuration YAML.

```yaml
assistant:
  mode: "casual" # formal, casual, or sarcastic
  
voice:
  mac_voice: "Samantha" # Or 'Rishi' for Indian accent.
  speed: 180

llm:
  model: "llama3" # Recommend keeping > 8B parameter models if you have 16GB RAM.
```

## 3. Memory Restraints
Currently, `memory/session_memory.py` sets a hard stop at 20 message pairs. You can increase `self.max_history` inside that class, but note that the LLM may begin to hallucinate or slow down heavily as the context window exceeds raw system capabilities.
