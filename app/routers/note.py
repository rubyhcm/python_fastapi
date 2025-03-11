from typing import Optional
from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas, oauth2
from uuid import UUID

router = APIRouter()

# Create note
# using serializer
@router.post('/notes', status_code=status.HTTP_201_CREATED,response_model=schemas.Note)
def create_note(note: schemas.CreateNote, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # login before create note, current_user: UUID = Depends(oauth2.get_current_user)
    new_note = models.Note(user_id=current_user.id, **note.dict())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# Get notes
@router.get("/notes", response_model=list[schemas.Note])
def get_notes(
                db: Session = Depends(get_db), 
                current_user = Depends(oauth2.get_current_user), 
                limit: int = 10, 
                skip: int = 0, 
                search: Optional[str] = ""):
    notes = db.query(models.Note).filter(models.Note.content.contains(search)).limit(limit).offset(skip).all()
    return notes

# Get note
@router.get('/notes/{id}')
def get_note(id: UUID, db: Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
    return {"data": note}

# Delete note
@router.delete('/notes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: UUID, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    note = db.query(models.Note).filter(models.Note.id == id)
    if not note.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
    
    if note.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    
    note.delete(synchronize_session=False)
    db.commit()

# Update note
@router.put('/notes/{id}')
def update_post(id: UUID, note: schemas.UpdateNote, db: Session = Depends(get_db),current_user = Depends(oauth2.get_current_user)):
    note_to_update = db.query(models.Note).filter(models.Note.id == id)
    if not note_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
    
    if note_to_update.first().user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    
    note_to_update.update(note.dict(), synchronize_session=False)
    db.commit()
    return {"data": note_to_update.first()}

