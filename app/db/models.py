from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.db.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True) # Unique to prevent duplicates
    source = Column(String)
    
    # Content fields
    summary = Column(Text, nullable=True) # AI generated summary
    relevance_score = Column(Integer, nullable=True) # AI score (1-10)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_emailed = Column(Boolean, default=False) # Track if we sent this to user
