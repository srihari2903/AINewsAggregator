from app.services.llm_service import LLMService
from dotenv import load_dotenv

# Load env vars explicitly for the test script
load_dotenv()

def main():
    print("🤖 Initializing LLM Service...")
    try:
        llm = LLMService()
        
        # Test Data
        title = "Python 3.13 Release: What's New?"
        url = "https://docs.python.org/3.13/whatsnew/3.13.html"
        
        print(f"\n📝 Analyzing Article:\nTitle: {title}\nURL: {url}")
        print("-" * 30)
        
        # Call the API
        result = llm.analyze_article(title, url)
        
        print("✅ Result from Gemini:")
        print(f"Summary: {result.get('summary')}")
        print(f"Score: {result.get('score')}/10")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Tip: Check if GEMINI_API_KEY is set in your .env file.")

if __name__ == "__main__":
    main()
