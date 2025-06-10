from fastapi import FastAPI
from blog.database import engine
from blog.routers import blog, users
from blog import models
from blog.utils import authentication 


# Initialize FastAPI app
app = FastAPI()

# Create DB tables
models.Base.metadata.create_all(bind=engine)

# Include the router for authentication endpoints
app.include_router(authentication.router) 

# Include the router for blog endpoints
app.include_router(blog.router)  

# Include the router for user endpoints
app.include_router(users.router)

