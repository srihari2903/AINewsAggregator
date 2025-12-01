# AI News Aggregator 🤖📰

A robust, automated data pipeline that scrapes tech news from multiple sources, uses **Google Gemini AI** to summarize and score articles, stores them in a **PostgreSQL** database, and delivers a curated daily email digest.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)

## 🚀 Features

-   **Multi-Source Scraping**: Fetches news from **Hacker News** and **TechCrunch** (AI Section).
-   **AI-Powered Analysis**: Uses **Google Gemini 2.0 Flash** to:
    -   Generate concise 1-sentence summaries.
    -   Assign relevance scores (1-10) to filter noise.
-   **Smart Deduplication**: Checks the database to ensure you never see the same article twice.
-   **Robust Storage**: Persists data in a **PostgreSQL** database running in Docker.
-   **Beautiful Emails**: Sends a daily HTML newsletter via SMTP (Gmail).
-   **Automated Scheduling**: Runs the entire pipeline automatically every day at 8:00 AM.

## 🛠️ Tech Stack

-   **Language**: Python 3.12
-   **Web Framework**: FastAPI (for the application runner)
-   **Database**: PostgreSQL (via Docker) + SQLAlchemy (ORM)
-   **AI Model**: Google Gemini 2.0 Flash
-   **Scheduling**: APScheduler
-   **Containerization**: Docker & Docker Compose

## 🏗️ Architecture

The project follows **Clean Architecture** principles:

-   `app/services/scrapers`: Polymorphic scraper modules (BaseScraper pattern).
-   `app/services/llm_service.py`: AI integration logic.
-   `app/services/news_service.py`: Core business logic (ETL pipeline).
-   `app/services/email_service.py`: Notification system with Jinja2 templates.
-   `app/db`: Database models and connection logic.

## 🚦 Getting Started

### Prerequisites

-   Docker & Docker Compose
-   Python 3.10+
-   A Google Gemini API Key
-   A Gmail App Password

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/AINewsAggregator.git
    cd AINewsAggregator
    ```

2.  **Set up Environment Variables**:
    ```bash
    cp .env.example .env
    ```
    Edit `.env` and fill in your details:
    ```ini
    GEMINI_API_KEY=your_key_here
    DATABASE_URL=postgresql://user:password@localhost:5432/newsdb
    EMAIL_SENDER=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password
    EMAIL_RECIPIENT=your_email@gmail.com
    ```

3.  **Start the Database (Docker)**:
    ```bash
    docker-compose up -d db
    ```

4.  **Install Python Dependencies**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

5.  **Initialize the Database**:
    ```bash
    python -m app.db.init_db
    ```

### ▶️ Usage

**Run the Automated Scheduler**:
```bash
python main.py
```
The application will start and schedule the pipeline to run daily at 8:00 AM.

**Run Manually (for testing)**:
```bash
python -m test_scraper
```

## 🧪 Testing

-   **Test Scraper**: `python -m test_scraper`
-   **Test AI**: `python -m test_llm`
-   **Test Email**: `python -m test_email`
