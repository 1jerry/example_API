from fastapi import FastAPI

app = FastAPI()

fake_users_db = [
    {"user_id": 1, "user_name": "bob"},
    {"user_id": 2, "user_name": "carl"},
    {"user_id": 3, "user_name": "abe"},
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
