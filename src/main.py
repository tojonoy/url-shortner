from fastapi import FastAPI, HTTPException,Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from Database.database import engine, Base
from models.Data.DataCrud import create_url, get_url_by_short_code
from models.Data.DataModels import Url
from Dto.DataDto import UrlDto,UrlCodeDto
from Database.database import get_db
from sqlalchemy.orm import Session
Base.metadata.create_all(bind=engine)
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/create-url", response_model=UrlCodeDto)
def create_url_endpoint(url: str, db: Session=Depends(get_db)):
    return UrlCodeDto.from_orm(create_url(db, url))
@app.get("/{code}")
def redirect(code:str,db:Session=Depends(get_db)):
    url=get_url_by_short_code(db,code)
    if not url:
        raise HTTPException(status_code=401,detail="Invalid Short Code")
    print(url.original)
    return RedirectResponse(url=url.original)
