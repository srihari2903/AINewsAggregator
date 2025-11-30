import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from app.services.scrapers.base import BaseScraper

class TechCrunchScraper(BaseScraper):
    """
    Scraper for TechCrunch AI section.
    """

    def fetch_articles(self) -> List[Dict[str, Any]]:
        print("Fetching articles from TechCrunch (AI Section)...")
        url = "https://techcrunch.com/category/artificial-intelligence/"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            articles = []
            
            # TechCrunch structure changes often, but usually titles are in <h3> or <h2> tags
            # We look for the loop-card__title class
            titles = soup.select('.loop-card__title > a')
            
            for link in titles:
                title = link.get_text(strip=True)
                url = link.get('href')
                
                articles.append({
                    "source": "TechCrunch",
                    "title": title,
                    "url": url
                })
                
            print(f"Found {len(articles)} articles from TechCrunch.")
            return articles

        except requests.RequestException as e:
            print(f"Error fetching TechCrunch: {e}")
            return []
