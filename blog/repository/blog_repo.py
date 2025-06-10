from sqlalchemy.orm import Session
from blog import schemas, models
from blog.database import get_db    
from fastapi import Depends, HTTPException
from typing import List

def get_all_blogs(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs

def get_blog_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

def create_blog(request: schemas.BlogCreate, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.title == request.title, models.Blog.user_id == 1).first()
    if blog:
        raise HTTPException(status_code=400, detail="Blog with this title already exists")

    new_blog = models.Blog(
        title=request.title,
        content=request.content,
        published=request.published,
        user_id=1  # Replace with actual user ID from auth in real apps
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update_blog(id: int, request: schemas.BlogCreate, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog.title = request.title
    blog.content = request.content
    blog.published = request.published

    db.commit()
    db.refresh(blog)
    return {"data": "Blog updated successfully", "blog": blog}

def delete_blog(id: int, db: Session):
    # db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    # db.commit()
    # return {"data": "Blog deleted successfully"}
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    return {"data": "Blog deleted successfully"}


