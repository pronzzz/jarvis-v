import yaml
import os

def load_config(config_path="config/settings.yaml") -> dict:
    if not os.path.exists(config_path):
        print(f"[Warning] Config file not found at {config_path}. Using safe defaults.")
        return {}
        
    with open(config_path, "r") as f:
        try:
            return yaml.safe_load(f)
        except Exception as e:
            print(f"[Error] Failed to parse config YAML: {e}")
            return {}
