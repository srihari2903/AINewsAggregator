from sqlalchemy.orm import Session
from typing import List
from app.db.models import Article
from app.services.scrapers.base import BaseScraper

class NewsService:
    def __init__(self, db: Session):
        self.db = db

    def scrape_and_save(self, scrapers: List[BaseScraper]):
        """
        Runs the given scrapers and saves new articles to the DB.
        """
        total_new = 0
        
        for scraper in scrapers:
            print(f"Running {scraper.__class__.__name__}...")
            articles_data = scraper.fetch_articles()
            
            for article_data in articles_data:
                # Check if URL already exists
                exists = self.db.query(Article).filter(Article.url == article_data['url']).first()
                
                if not exists:
                    # Create new Article object
                    new_article = Article(
                        title=article_data['title'],
                        url=article_data['url'],
                        source=article_data['source']
                    )
                    self.db.add(new_article)
                    total_new += 1
            
            # Commit changes for this scraper
            self.db.commit()
            
        return total_new

    def get_recent_articles(self, limit: int = 10):
        return self.db.query(Article).order_by(Article.created_at.desc()).limit(limit).all()
