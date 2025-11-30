from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseScraper(ABC):
    """
    Abstract Base Class that defines the interface for all news scrapers.
    
    Why use this?
    - Consistency: Every scraper MUST implement the fetch_articles() method.
    - Extensibility: Adding a new source (e.g., TechCrunch) is easy; just inherit from this.
    """

    @abstractmethod
    def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Fetches articles from the source.
        
        Returns:
            A list of dictionaries, where each dictionary represents an article.
            Example: [{'title': '...', 'url': '...', 'content': '...'}]
        """
        pass
