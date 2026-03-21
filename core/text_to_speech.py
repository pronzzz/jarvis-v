import subprocess
import os

class TextToSpeech:
    def __init__(self, voice="Samantha", speed=175):
        """
        macOS native TTS implementation using the `say` command.
        Voice options: Samantha, Alex, Rishi (Indian English), etc.
        """
        self.voice = voice
        self.speed = str(speed)
        print(f"[TextToSpeech] Initialized macOS built-in TTS (Voice: {self.voice})")
        
    def speak(self, text: str):
        """
        Runs the `say` command synchronously. 
        """
        # We replace double quotes to prevent breaking the subprocess command easily
        safe_text = text.replace('"', '\\"').replace("'", "\\'")
        print(f"[Jarvis] {text}")
        
        try:
            subprocess.run(["say", "-v", self.voice, "-r", self.speed, safe_text], check=True)
        except Exception as e:
            print(f"[TTS Error] {e}")
