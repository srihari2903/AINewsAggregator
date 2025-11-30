from sqlalchemy.orm import Session
from typing import List
from app.db.models import Article
from app.services.scrapers.base import BaseScraper
from app.services.llm_service import LLMService

class NewsService:
    def __init__(self, db: Session):
        self.db = db
        self.llm = LLMService()

    def scrape_and_save(self, scrapers: List[BaseScraper]):
        """
        Runs the given scrapers, summarizes new articles with AI, and saves to DB.
        """
        total_new = 0
        
        for scraper in scrapers:
            print(f"Running {scraper.__class__.__name__}...")
            articles_data = scraper.fetch_articles()
            
            for article_data in articles_data:
                # Check if URL already exists
                exists = self.db.query(Article).filter(Article.url == article_data['url']).first()
                
                if not exists:
                    print(f"🤖 Analyzing: {article_data['title'][:50]}...")
                    # AI Analysis
                    analysis = self.llm.analyze_article(article_data['title'], article_data['url'])
                    
                    # Create new Article object with AI data
                    new_article = Article(
                        title=article_data['title'],
                        url=article_data['url'],
                        source=article_data['source'],
                        summary=analysis.get('summary'),
                        relevance_score=analysis.get('score', 0)
                    )
                    self.db.add(new_article)
                    total_new += 1
            
            # Commit changes for this scraper
            self.db.commit()
            
        return total_new

    def get_recent_articles(self, limit: int = 10):
        return self.db.query(Article).order_by(Article.created_at.desc()).limit(limit).all()
