from typing import Union

from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()

# Validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Union[int, None] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post('/createposts')
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"message": "Post created"}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    print(post)
    print(post.content)
    print(post.dict())
    return {"data": post}

@app.get('/posts')
def get_posts():
    return {"data": my_posts}

@app.get('/posts/{id}')
def get_post(id: int, response: Response):
    post = None
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
    return {"data": my_posts}

# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
