import google.generativeai as genai
import os
import json
from typing import Dict, Any

class LLMService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        # Using gemini-2.0-flash as it is available and fast
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def analyze_article(self, title: str, url: str) -> Dict[str, Any]:
        """
        Analyzes an article title/url to generate a summary and relevance score.
        Returns a JSON dictionary.
        """
        prompt = f"""
        You are an expert tech news curator. Analyze the following article:
        Title: {title}
        URL: {url}

        Task:
        1. Write a concise 1-sentence summary of what this article is likely about.
        2. Assign a relevance score (1-10) based on how important it is for a tech enthusiast.
        
        Output format: JSON with keys 'summary' and 'score'.
        Example: {{"summary": "Google releases new AI model.", "score": 9}}
        """
        
        try:
            response = self.model.generate_content(prompt)
            # Clean up the response to ensure it's valid JSON
            text = response.text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "")
            
            return json.loads(text)
        except Exception as e:
            print(f"Error analyzing article '{title}': {e}")
            return {"summary": "Could not generate summary.", "score": 0}
