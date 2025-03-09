import time
from typing import Union
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

app = FastAPI()

# Validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Union[int, None] = None
    created_at: datetime = datetime.now()

# Connect to database
while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="12052311",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

# Root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create post
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published, created_at) VALUES (%s, %s, %s, %s) RETURNING * """, (post.title, post.content, post.published, post.created_at))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}

# Get posts
@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts_data = cursor.fetchall()
    return {"data": posts_data}

# Get post
@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"data": post}

# Delete post
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update post
@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s, created_at = %s WHERE id = %s RETURNING * """,
    (post.title, post.content, post.published, post.created_at, id))
    updated_post = cursor.fetchone()
    conn.commit()
    return {"data": updated_post}

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
