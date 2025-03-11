from fastapi import FastAPI
from .database import Engine
from . import models
from .routers import note, user, auth

# Set logging
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind=Engine)

app = FastAPI()

# Params and Validation
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Union[int, None] = None
#     created_at: datetime = datetime.now()

# Include routers
app.include_router(note.router)
app.include_router(user.router)
app.include_router(auth.router)

# Root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create post
# @app.post('/posts', status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     cursor.execute("""INSERT INTO posts (title, content, published, created_at) VALUES (%s, %s, %s, %s) RETURNING * """, (post.title, post.content, post.published, post.created_at))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}

# using serializer
# @app.post('/notes', status_code=status.HTTP_201_CREATED,response_model=schemas.Note)
# def create_note(note: schemas.CreateNote, db: Session = Depends(get_db)):
#     new_note = models.Note(**note.dict())
#     db.add(new_note)
#     db.commit()
#     db.refresh(new_note)
#     return new_note

# Get posts
# @app.get('/posts')
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     posts_data = cursor.fetchall()
#     return {"data": posts_data}

# @app.get("/notes", response_model=list[schemas.Note])
# def get_notes(db: Session = Depends(get_db)):
#     notes = db.query(models.Note).all()
#     return notes

# Get post
# @app.get('/posts/{id}')
# def get_post(id: int, response: Response):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id: {id} was not found"}
#     return {"data": post}

# @app.get('/notes/{id}')
# def get_note(id: UUID, db: Session = Depends(get_db)):
#     note = db.query(models.Note).filter(models.Note.id == id).first()
#     if not note:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
#     return {"data": note}

# Delete post
# @app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")

# @app.delete('/notes/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: UUID, db: Session = Depends(get_db)):
#     note = db.query(models.Note).filter(models.Note.id == id)
#     if not note.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
#     note.delete(synchronize_session=False)
#     db.commit()

# Update post
# @app.put('/posts/{id}')
# def update_post(id: int, post: Post):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s, created_at = %s WHERE id = %s RETURNING * """,
#     (post.title, post.content, post.published, post.created_at, id))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     return {"data": updated_post}

# @app.put('/notes/{id}')
# def update_post(id: UUID, note: schemas.UpdateNote, db: Session = Depends(get_db)):
#     note_to_update = db.query(models.Note).filter(models.Note.id == id)
#     if not note_to_update.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"note with id: {id} was not found")
#     note_to_update.update(note.dict(), synchronize_session=False)
#     db.commit()
#     return {"data": note_to_update.first()}

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

