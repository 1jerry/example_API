from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    zip: int = None
    phone: int = None
    email: str = None


app = FastAPI()

fake_users_db = [
    {"user_id": 1, "first_name": "bob"},
    {"user_id": 2, "first_name": "carl"},
    {"user_id": 3, "first_name": "abe"},
]


@app.get("/")
async def root():
    return {"message": "Hello World...."}


@app.get("/users/me")
async def read_users_me():
    return {"id": 1}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"id": user_id}


@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    result = fake_users_db[skip:skip + limit]
    return result


@app.post('/users/')
async def create_user(user: User):
    item_dict = user.dict()
    item_dict.update({"full_name": user.first_name + " " + user.last_name})
    fake_users_db.append(item_dict)
    return item_dict


@app.put('/users/{user_id}')
async def update_user(user: User, user_id: int, q: str = None):
    result = {"id": user_id, **user.dict()}
    # no partial - must pass all
    if q:
        result.update({"q": q})
    return result
