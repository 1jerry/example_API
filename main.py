from fastapi import FastAPI, Query, Path
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


def get_user(rid):
    return next((o for o in fake_users_db if o["user_id"] == rid), {})


@app.get("/")
async def root():
    return {"message": "Hello World...."}


@app.get("/users/me")
async def read_users_me():
    return get_user(1)


@app.get("/users/{user_id}")
async def read_user(user_id: int = Path(..., title="The user's ID", ge=1)):
    return get_user(user_id)


@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    result = fake_users_db[skip:skip + limit]
    return result


@app.post('/users/')
async def create_user(user: User):
    item_dict = user.dict()
    new_id = max([i['user_id'] for i in fake_users_db]) + 1
    item_dict.update({
        "full_name": user.first_name + " " + user.last_name,
        "user_id": new_id,
    })
    fake_users_db.append(item_dict)
    return item_dict


@app.put('/users/{user_id}')
async def update_user(user: User, user_id: int, q: str = Query(None, max_length=50, min_length=3)):
    result = {"id": user_id, **user.dict()}
    # no partial - must pass all
    if q:
        result.update({"q": q})
    return result
