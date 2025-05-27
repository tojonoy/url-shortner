from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 
from dotenv import load_dotenv
load_dotenv()
Database_url=os.getenv("DATABASE_URL")
if not Database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")
Base = declarative_base()
engine = create_engine(Database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()