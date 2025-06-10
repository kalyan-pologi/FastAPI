from fastapi import APIRouter, Depends, HTTPException
from blog import schemas, models
from blog.database import get_db
from sqlalchemy.orm import Session
from typing import List
from blog.repository import user_repo

router = APIRouter()

# create User model and schema
# response_model is used to specify the response schema not to show the password and return the user details not the dict
@router.post("/user", response_model=schemas.ShowUser, status_code=201, tags=["users"])
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_repo.create_user(request, db)

# Get all users
@router.get("/user", response_model=List[schemas.ShowUser], status_code=200, tags=["users"])
def get_all_users(db: Session = Depends(get_db)):
    return user_repo.get_all_users(db)

# Get user by ID
@router.get("/user/{id}", response_model=schemas.ShowUser, status_code=200, tags=["users"])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_repo.get_user_by_id(id, db)

# Update user by ID
@router.put("/user/{id}", response_model=schemas.ShowUser, status_code=200, tags=["users"])
def update_user(id: int, request: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_repo.update_user(id, request, db)

# Delete user by ID
@router.delete("/user/{id}", status_code=204, tags=["users"])
def delete_user(id: int, db: Session = Depends(get_db)):
    return user_repo.delete_user(id, db)

# Note: The hashing of the password should be done in the router or in a service layer before saving to the database.
# This ensures that the password is not stored in plain text.
