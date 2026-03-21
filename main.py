import asyncio
from core.orchestrator import JarvisOrchestrator

def main():
    print("Initializing Jarvis-V...")
    jarvis = JarvisOrchestrator()
    try:
        asyncio.run(jarvis.run())
    except KeyboardInterrupt:
        print("\nShutting down Jarvis-V...")

if __name__ == "__main__":
    main()
