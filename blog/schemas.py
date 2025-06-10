from pydantic import BaseModel
from typing import List, Optional

# create a user schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

# create a blog schema
class BlogCreate(BaseModel):
    title: str
    content: str
    published: bool = True
    
    class Config:
        orm_mode = True
        
class BlogSample(BaseModel):
    id: int
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True

# create a user response schema
class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[BlogSample] = []

    class Config:
        orm_mode = True

# # to show the all blog details in the response
# class showBlog(BlogCreate):
#     id: int
#     title: str

#     class Config:
#         orm_mode = True\


# to show the what blog details in the response
class ShowBlog(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    creator: ShowUser  # must match your SQLAlchemy relationship

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: Optional[str] = None

    class Config:
        orm_mode = True

