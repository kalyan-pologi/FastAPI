from passlib.context import CryptContext


# Hash the password before storing it
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
# This function verifies if the provided plain password matches the hashed password
# It returns True if they match, otherwise False