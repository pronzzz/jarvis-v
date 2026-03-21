class SessionMemory:
    def __init__(self, system_prompt: str, max_history: int = 20):
        self.system_prompt = system_prompt
        self.max_history = max_history
        self.messages = []
        self.reset()
        
    def reset(self):
        """Clears memory and injects the system prompt."""
        self.messages = [{"role": "system", "content": self.system_prompt}]
        print("[Memory] Session forgotten. Clean slate initialized.")
        
    def add_user_message(self, text: str):
        self.messages.append({"role": "user", "content": text})
        self._trim_history()
        
    def add_assistant_message(self, text: str):
        self.messages.append({"role": "assistant", "content": text})
        self._trim_history()
        
    def get_context(self) -> list:
        return self.messages
        
    def _trim_history(self):
        """Ensures the context window doesn't grow indefinitely."""
        # We always keep the first message (system prompt)
        if len(self.messages) > self.max_history:
            # Drop the oldest user-assistant interaction
            self.messages.pop(1)
            self.messages.pop(1)
