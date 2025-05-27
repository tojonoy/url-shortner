from sqlalchemy.orm import Session
from models.Data.DataModels import Url, UrlHit
from Service.random import get_random_code

def create_url(db: Session, original_url: str):
    short_code = get_random_code(6)
    new_url = Url(original=original_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url
def get_url_by_short_code(db: Session, short_code: str):
    return db.query(Url.original).filter(Url.short_code == short_code).first()
