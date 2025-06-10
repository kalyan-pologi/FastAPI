from fastapi import APIRouter, Depends, HTTPException, status, Response
from blog import schemas, models
from blog.database import get_db
from blog.repository import blog_repo
from sqlalchemy.orm import Session
from typing import List
from blog.utils import OAuth2

router = APIRouter(
    # prefix="/api",  # Prefix for all routes in this router
    # tags=["blogs"],  # Tags for grouping in the documentation
    # responses={404: {"description": "Not found"}},  # Default response for 404 errors
)

# Root endpoint
# tags is used to group the endpoints in the documentation
@router.get("/", tags=["blogs"])
def read_root():
    return {"message": "Welcome to the Blog API"}

@router.get("/blog", response_model= List[schemas.ShowBlog], status_code=200, tags=["blogs"])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(OAuth2.get_current_user)):
    return blog_repo.get_all_blogs(db)

# Get a single blog by ID
@router.get("/blog/{id}", response_model=schemas.ShowBlog, status_code=200, tags=["blogs"])
def get_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(OAuth2.get_current_user)):
    return blog_repo.get_blog_by_id(id, db)

# Create a new blog
# request is a BlogCreate schema
# db is a Session object
# models.Blog is the SQLAlchemy model for the blog
# http status is used to set the response status code
# response_model is used to specify the response schema
@router.post("/blog", response_model=schemas.ShowBlog, status_code=201, tags=["blogs"])
def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(OAuth2.get_current_user)):
    return blog_repo.create_blog(request, db)

# Update an existing blog
@router.put("/blog/{id}", status_code=202, tags=["blogs"])
def update_blog(id: int, request: schemas.BlogCreate, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(OAuth2.get_current_user)):
    return blog_repo.update_blog(id, request, db)

# Delete a blog
@router.delete("/blog/{id}", tags=["blogs"])
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(OAuth2.get_current_user)):
    return blog_repo.delete_blog(id, db)


