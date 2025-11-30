import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from app.services.scrapers.base import BaseScraper

class HackerNewsScraper(BaseScraper):
    """
    Concrete implementation of BaseScraper for Hacker News (news.ycombinator.com).
    """

    def fetch_articles(self) -> List[Dict[str, Any]]:
        print("Fetching articles from Hacker News...")
        
        # 1. The URL we want to visit
        url = "https://news.ycombinator.com/"
        
        try:
            # 2. Make the HTTP request (Act like a browser)
            # timeout=10 means "give up if it takes longer than 10 seconds"
            response = requests.get(url, timeout=10)
            
            # Check if the request was successful (Status Code 200)
            response.raise_for_status()
            
            # 3. Parse the HTML content
            # BeautifulSoup takes the raw HTML text and turns it into a tree we can search
            soup = BeautifulSoup(response.text, 'html.parser')
            
            articles = []
            
            # 4. Find the elements we want
            # On Hacker News, titles are inside a <span> with class "titleline"
            # We look for the <a> tag inside that span
            # CSS Selector: .titleline > a
            links = soup.select('.titleline > a')
            
            for link in links:
                title = link.get_text()
                url = link.get('href')
                
                # Filter out internal HN links (like "item?id=...") if you only want external news
                # For now, we keep everything.
                
                articles.append({
                    "source": "Hacker News",
                    "title": title,
                    "url": url
                })
                
            print(f"Found {len(articles)} articles.")
            return articles

        except requests.RequestException as e:
            print(f"Error fetching Hacker News: {e}")
            return []
