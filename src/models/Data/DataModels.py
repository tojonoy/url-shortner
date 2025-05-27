from sqlalchemy import Column, Integer, String, DateTime,func
from Database.database import Base

class Url(Base):
    __tablename__ = 'url'
    
    id = Column(Integer, primary_key=True,index=True)
    original = Column(String(50), nullable=False)
    short_code= Column(String(10), unique=True, index=True)
    created_at = Column(DateTime, default=func.now())
class UrlHit(Base):
    __tablename__ = 'url_hits'
    id = Column(Integer, primary_key=True, index=True)
    url_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=func.now())
