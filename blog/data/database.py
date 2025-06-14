from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# define the database URL
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

# create a session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()