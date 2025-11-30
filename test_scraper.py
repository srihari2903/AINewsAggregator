from app.services.scrapers.hacker_news import HackerNewsScraper
from app.services.scrapers.techcrunch import TechCrunchScraper
from app.services.news_service import NewsService
from app.db.database import SessionLocal

def main():
    # 1. Initialize the Database Session
    db = SessionLocal()
    news_service = NewsService(db)
    
    # 2. Define our scrapers
    scrapers = [
        HackerNewsScraper(),
        TechCrunchScraper()
    ]
    
    print("🚀 Starting Extraction Pipeline...")
    
    try:
        # 3. Run the Service (Scrape -> Deduplicate -> Save)
        new_articles_count = news_service.scrape_and_save(scrapers)
        
        print(f"\n✅ Pipeline Finished!")
        print(f"📦 New Articles Saved to DB: {new_articles_count}")
        
        # 4. Verify by reading back from DB
        print("\n👀 Reading back recent articles from Database:")
        recent = news_service.get_recent_articles(limit=5)
        for article in recent:
            print(f"- [{article.source}] {article.title}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
