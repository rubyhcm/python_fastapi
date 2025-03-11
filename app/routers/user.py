from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, utils
from uuid import UUID

# Config swagger
router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: UUID, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")
    return user

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: UUID, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")
    user.delete(synchronize_session=False)
    db.commit()

@router.put('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def update_user(id: UUID, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    user_to_update = db.query(models.User).filter(models.User.id == id)
    if not user_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")
    if user.password:
        user_to_update.first().password = utils.hash(user.password)
    
    user_to_update.update(user.dict(), synchronize_session=False)
    db.commit()
    return user_to_update.first()