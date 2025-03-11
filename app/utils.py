from passlib.context import CryptContext

# Encrypt password
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd.hash(password)

def verify(plain_password, hashed_password):
    return pwd.verify(plain_password, hashed_password)
