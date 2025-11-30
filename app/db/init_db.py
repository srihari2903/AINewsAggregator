from app.db.database import engine, Base
from app.db import models

def init_db():
    print("Creating database tables...")
    # This line looks at all classes that inherit from Base (like Article)
    # and creates the tables in the database if they don't exist.
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    init_db()
