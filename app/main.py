from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, crud, schemas, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow calls from the frontend (Svelte)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/articles", response_model=list[schemas.ArticleResponse])
def list_articles(db: Session = Depends(get_db)):
    return crud.get_all_articles(db)

@app.get("/api/articles/{article_id}", response_model=schemas.ArticleResponse)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.get_article_by_id(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.post("/api/articles", response_model=schemas.ArticleResponse)
def create_article(
    article: schemas.ArticleCreate,
    db: Session = Depends(get_db),
    user: str = Depends(auth.verify_user),
):
    return crud.create_article(db, article.title, article.content)

@app.put("/api/articles/{article_id}", response_model=schemas.ArticleResponse)
def update_article(
    article_id: int,
    update_data: schemas.ArticleCreate,
    db: Session = Depends(get_db),
    user: str = Depends(auth.verify_user),
):
    return crud.update_article(db, article_id, update_data)

@app.delete("/api/articles/{article_id}")
def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(auth.verify_user),
):
    crud.delete_article(db, article_id)
    return {"message": "Article deleted"}
