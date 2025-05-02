from pydantic import BaseModel
from datetime import datetime

class ArticleCreate(BaseModel):
    title: str
    content: str

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime

    class Config:
        orm_mode = True
