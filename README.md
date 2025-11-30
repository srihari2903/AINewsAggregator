# AI News Aggregator 🤖📰

A Python-based automated news pipeline that scrapes tech news, summarizes it using Google Gemini AI, and delivers a daily curated email digest.

## 🚀 Features
- **Automated Scraping**: Fetches latest news from Hacker News (extensible to other sources).
- **AI Summarization**: Uses LLMs to generate concise summaries and relevance scores.
- **Data Persistence**: Stores history in a SQLite database to prevent duplicates.
- **Email Delivery**: Sends a beautifully formatted HTML email digest.
- **Scheduling**: Runs automatically at scheduled intervals.

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Web Framework**: FastAPI
- **AI/LLM**: Google Gemini (Generative AI)
- **Database**: SQLite + SQLAlchemy
- **Scheduler**: APScheduler

## 🏗️ Architecture
The project follows **Clean Architecture** principles:
- `app/core`: Configuration and settings.
- `app/services`: Business logic (Scrapers, AI Service, Email Service).
- `app/db`: Database models and repositories.
- `app/api`: API endpoints.

## 🚦 Getting Started

### Prerequisites
- Python 3.10+
- A Google Gemini API Key

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```
4. Run the application:
   ```bash
   python main.py
   ```
