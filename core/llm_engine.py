import ollama

class LLMEngine:
    def __init__(self, model_name="llama3"):
        print(f"[LLMEngine] Using local Ollama model: {model_name}")
        self.model_name = model_name
        
    def generate_response(self, text: str = None, context: list = None, tools: list = None) -> (str, list):
        """
        Sends user text to Ollama and receives the string response and/or tool calls.
        Returns a tuple: (assistant_content_string, tool_calls_list)
        If text is None, it means we are just sending the context (e.g. after a tool execution).
        """
        if context is None:
            context = []
            
        messages = context.copy()
        if text:
            messages.append({"role": "user", "content": text})
            
        response = ollama.chat(model=self.model_name, messages=messages, tools=tools)
        
        message = response.get('message', {})
        content = message.get('content', '')
        tool_calls = message.get('tool_calls', [])
        
        return content.strip(), tool_calls
