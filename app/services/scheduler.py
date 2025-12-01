from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.db.database import SessionLocal
from app.services.news_service import NewsService
from app.services.email_service import EmailService
from app.services.scrapers.hacker_news import HackerNewsScraper
from app.services.scrapers.techcrunch import TechCrunchScraper
from datetime import datetime

class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.email_service = EmailService()

    def start(self):
        # Schedule the job to run every day at 8:00 AM
        # For testing, we can change this to run every minute
        trigger = CronTrigger(hour=11, minute=10)
        
        self.scheduler.add_job(
            self.run_pipeline,
            trigger=trigger,
            id='daily_news_pipeline',
            name='Run Daily News Pipeline',
            replace_existing=True
        )
        self.scheduler.start()
        print("⏰ Scheduler started! Job set for 8:00 AM daily.")

    def run_pipeline(self):
        print(f"🚀 Starting Scheduled Pipeline at {datetime.now()}...")
        db = SessionLocal()
        try:
            # 1. Scrape & Save
            news_service = NewsService(db)
            scrapers = [HackerNewsScraper(), TechCrunchScraper()]
            new_count = news_service.scrape_and_save(scrapers)
            print(f"📦 Saved {new_count} new articles.")

            # 2. Send Email (Only if there are new articles, or just send recent ones)
            # For this MVP, let's send the top 5 most recent articles
            recent_articles = news_service.get_recent_articles(limit=5)
            if recent_articles:
                self.email_service.send_daily_digest(recent_articles)
            
        except Exception as e:
            print(f"❌ Error in scheduled job: {e}")
        finally:
            db.close()
