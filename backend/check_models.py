import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=== Available models that support embedContent ===\n")
for model in client.models.list():
    actions = getattr(model, "supported_actions", []) or []
    if "embedContent" in actions:
        print(f"  NAME: {model.name}")
        print(f"  DISPLAY: {model.display_name}")
        print()
