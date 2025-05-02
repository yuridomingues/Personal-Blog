from sqlalchemy.orm import Session
from app.models import Article
from app.schemas import ArticleCreate
from datetime import datetime

def get_all_articles(db: Session):
    return db.query(Article).order_by(Article.published_at.desc()).all()

def get_article_by_id(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def create_article(db: Session, title: str, content: str):
    article = Article(title=title, content=content, published_at=datetime.utcnow())
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def update_article(db: Session, article_id: int, data: ArticleCreate):
    article = get_article_by_id(db, article_id)
    if not article:
        return None
    article.title = data.title
    article.content = data.content
    db.commit()
    db.refresh(article)
    return article

def delete_article(db: Session, article_id: int):
    article = get_article_by_id(db, article_id)
    if article:
        db.delete(article)
        db.commit()
