import asyncio
from core.listener import Listener
from core.speech_to_text import SpeechToText
from core.llm_engine import LLMEngine
from core.text_to_speech import TextToSpeech
from memory.session_memory import SessionMemory
from core.tool_registry import ToolRegistry
from core.config_loader import load_config

class JarvisOrchestrator:
    def __init__(self):
        print("[Orchestrator] Booting Jarvis subsystems...")
        self.config = load_config()
        self.mode = self.config.get("assistant", {}).get("mode", "formal")
        self.debug = self.config.get("assistant", {}).get("debug_mode", False)
        llm_model = self.config.get("llm", {}).get("model", "llama3")
        voice = self.config.get("voice", {}).get("mac_voice", "Rishi")
        
        self.listener = Listener()
        self.stt = SpeechToText()
        self.llm = LLMEngine(model_name=llm_model)
        self.tts = TextToSpeech(voice=voice)  
        self.tools = ToolRegistry()
        
        # Load personality prompt
        personalities = self.config.get("personalities", {})
        system_prompt = personalities.get(self.mode, personalities.get("formal"))
        
        self.memory = SessionMemory(system_prompt=system_prompt)

        
    async def run(self):
        """Main loop: Listen -> STT -> LLM -> TTS"""
        self.tts.speak("Systems online. At your service.")
        
        while True:
            try:
                # 1. Listen for audio
                print("\n等待音频 Wait for audio...") # Bilingual flavor
                audio_bytes = self.listener.listen_for_audio()
                
                # 2. STT pipeline
                print("[Process] Transcribing...")
                text = self.stt.transcribe(audio_bytes)
                if not text:
                    continue
                    
                print(f"[User] {text}")
                
                # Command interceptions (Phase 4 early peek)
                if text.lower() in ["clear memory", "forget everything", "reset session"]:
                    self.memory.reset()
                    self.tts.speak("Memory cleared, sir.")
                    continue
                
                # Simple wake word check (if "jarvis" is in the transcription)
                text_lower = text.lower()
                if "jarvis" not in text_lower and len(self.memory.get_context()) <= 1: # Require wake word for initial prompt
                   continue 

                # 3. LLM Pipeline
                print("[Process] Thinking...")
                self.memory.add_user_message(text)
                
                # We iteratively handle tool calls
                content, tool_calls = self.llm.generate_response(
                    text=None, # Already in memory via add_user_message
                    context=self.memory.get_context(), 
                    tools=self.tools.get_ollama_tools()
                )
                
                # Execute tools if any were called
                if tool_calls:
                    print(f"[Process] Executing {len(tool_calls)} tools...")
                    # Add AI's tool call intent to memory
                    self.memory.messages.append({"role": "assistant", "content": "", "tool_calls": tool_calls})
                    
                    for tool in tool_calls:
                        tool_name = tool['function']['name']
                        tool_args = tool['function'].get('arguments', {})
                        print(f"        -> {tool_name}")
                        
                        tool_result = self.tools.execute_tool(tool_name, tool_args)
                        # Add tool result back to memory
                        self.memory.messages.append({"role": "tool", "name": tool_name, "content": str(tool_result)})
                        
                    # Re-prompt LLM with the tool results
                    print("[Process] Analyzing tool results...")
                    content, _ = self.llm.generate_response(
                        text=None,
                        context=self.memory.get_context(),
                        tools=self.tools.get_ollama_tools()
                    )
                
                # Save final text response to memory
                if content:
                    self.memory.add_assistant_message(content)
                    # 4. TTS Pipeline
                    self.tts.speak(content)
                
            except Exception as e:
                print(f"Error in main loop: {e}")
                await asyncio.sleep(1)
