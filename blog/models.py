from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    published = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey('users.id')) # Assuming a user can create blogs
    creator = relationship("User", back_populates="blogs") 


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    blogs = relationship("Blog", back_populates="creator")  # Relationship to blogs created by the user
# This code defines the SQLAlchemy models for the Blog and User entities.