from blog.data import models
from fastapi import APIRouter, status, Depends, HTTPException
from blog.data import schemas
from blog.utils import hashing
from blog.data.database import get_db
from sqlalchemy.orm import Session
from blog.utils.JWTtoken import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from blog.data.schemas import Token
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
    responses={404: {"description": "Not found"}}
)

@router.post("/login")
# def login(request: schemas.Login, db: Session = Depends(get_db)):
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    # Check if user exists
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    # Verify password
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Password OR Invalid credentials")
    # Here you would typically create a session or token for the user
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/logout")
def logout():
    return {"message": "Logout endpoint is not implemented yet."}

@router.post("/register")
def register():
    return {"message": "Register endpoint is not implemented yet."}

