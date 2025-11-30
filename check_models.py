import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found.")
        return

    genai.configure(api_key=api_key)
    
    print("🔍 Listing available models...")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    except Exception as e:
        print(f"❌ Error listing models: {e}")

if __name__ == "__main__":
    main()
