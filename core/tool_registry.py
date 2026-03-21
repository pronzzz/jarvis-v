from skills.time import get_current_time, get_current_date
from skills.system import get_system_info, get_battery_status

class ToolRegistry:
    def __init__(self):
        # Map tool names to actual functions
        self.tool_map = {
            "get_current_time": get_current_time,
            "get_current_date": get_current_date,
            "get_system_info": get_system_info,
            "get_battery_status": get_battery_status
        }
    
    def get_ollama_tools(self) -> list:
        """Returns the JSON schema definitions required for Ollama."""
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_current_time",
                    "description": "Get the current exact time."
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_current_date",
                    "description": "Get today's date."
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_system_info",
                    "description": "Get information about the current operating system."
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_battery_status",
                    "description": "Get current battery percentage and charging status."
                }
            }
        ]
        
    def execute_tool(self, tool_name: str, arguments: dict) -> str:
        """Executes a tool by name and returns the result."""
        func = self.tool_map.get(tool_name)
        if hasattr(func, "__code__") and func.__code__.co_argcount > 0:
             return func(**arguments)
        if func:
            return func()
        return f"Tool {tool_name} not found."
