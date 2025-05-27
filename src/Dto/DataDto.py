from pydantic import BaseModel,HttpUrl,ConfigDict
from datetime import datetime

class UrlDto(BaseModel):
    url: HttpUrl

class UrlCodeDto(BaseModel):
    original:str
    short_code:str
    created_at:datetime
    model_config = ConfigDict(from_attributes=True)

class UrlHitDto(BaseModel):
    id:int
    url_id:int
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)
