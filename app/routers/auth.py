from fastapi import HTTPException, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, utils, oauth2

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# @router.post("/login", status_code=status.HTTP_200_OK)
# def login(db: Session = Depends(get_db), user_credentials: schemas.UserLogin = Body(...)):
#     # def login(db: Session = Depends(get_db), user_credentials: schemas.UserLogin): will be not work. We must use
#     # def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

#     user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#     if not utils.verify(user_credentials.password, user.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
#     token = oauth2.create_access_token(data = {"user_id": user.id})
#     print(token)
#     return {"token": token, "token_type": "bearer"}

@router.post("/login", status_code=status.HTTP_200_OK)
def login(db: Session = Depends(get_db), user_credentials: OAuth2PasswordRequestForm = Depends()):
    # def login(db: Session = Depends(get_db), user_credentials: schemas.UserLogin): will be not work. We must use
    # def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"token": token, "token_type": "bearer"}
    # We can use OAuth2PasswordRequestForm, but we need use username instead of email

# curl -X POST "http://your-api-url/auth/login" \
# -H "Content-Type: application/json" \
# -d '{"email": "user@example.com", "password": "yourpassword"}'
