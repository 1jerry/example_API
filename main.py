from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, EmailStr
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND
from starlette_prometheus import metrics, PrometheusMiddleware
from starlette.responses import HTMLResponse


class User(BaseModel):
    first_name: str
    last_name: str
    zip: int = None
    phone: int = None
    email: EmailStr = None


class UserUpdate(User):
    first_name: str = None
    last_name: str = None


app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route('/metrics/', metrics)

fake_users_db = [
    {"user_id": 1, "first_name": "bob"},
    {"user_id": 2, "first_name": "carl"},
    {"user_id": 3, "first_name": "abe"},
]


def get_user(rid, response=None):
    result = next((o for o in fake_users_db if o["user_id"] == rid), {})
    if response and not result:
        response.status_code = HTTP_404_NOT_FOUND
    return result


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head><title>Example API</title></head>
    <body>
    <h2>Example API using Python and asynchronous, static typed library <i>FastAPI</i></h2>
    <p>Primary API is at <a href="users">users</a></p>
    <p>See <a href="redoc">documentation</a></p>
    </body>
    </html>
    """


@app.get("/users/me")
async def read_users_me(response: Response):
    return get_user(1, response)


@app.get("/users/{user_id}")
async def read_user(
        response: Response,
        user_id: int = Path(..., title="The ID of the user you want to get.", ge=1, le=1000)
):
    # in Path(), None signifies optional, ... signifies required
    return get_user(user_id, response)


@app.delete("/users/{user_id}")
async def read_user(
        response: Response,
        user_id: int = Path(..., title="The ID of the user you want to DELETE.", ge=1, le=1000)
):
    result = get_user(user_id, response)
    if result:
        try:
            fake_users_db.remove(result)
        except ValueError:
            result = {}
    return result


@app.get("/users/")
async def read_users(skip: int = 0, limit: int = 10):
    result = fake_users_db[skip:skip + limit]
    return result


@app.post('/users/', status_code=201)
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
async def update_user(
        *,
        user: UserUpdate = Body(
            None,
            example={
                "first_name": "bob",
                "last_name": "Peterson",
                "zip": 98665,
                "phone": 8005551212,
                "email": "bad@a.com"
            }
        ),
        user_id: int,
        response: Response,
        q: str = Query(None, max_length=50, min_length=3)
):
    result = get_user(user_id, response)
    if user:
        result.update(**user.dict(exclude_unset=True))
    if q:
        result.update({"q": q})
    return result
