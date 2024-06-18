from fastapi import FastAPI
from auth import auth_router
from pydantic import BaseModel

from product import product_router
from comment import comment_router
from blog import blog_router
from fastapi_jwt_auth import AuthJWT
from schemas import JwtModel
from database import session, ENGINE

session = session(bind=ENGINE)
app = FastAPI()


@AuthJWT.load_config
def config():
    return JwtModel()


app.include_router(auth_router)
app.include_router(comment_router)
app.include_router(blog_router)
app.include_router(product_router)


@app.get("/")
async def test_1():
    return {
        "message": "My first easy example with fastapi"
    }


class UserRequest(BaseModel):
    name: str
    email: str


@app.get("/users")
async def users_g():
    return {
        "users": "Users who have"
    }


@app.post("/users")
async def p_user(request: UserRequest):
    return {
        "message": f"User {request.name} with email {request.email} has been created"
    }


@app.get("/users/{id}")
async def user_by_id(id: int):
    return {
        "message": f"user - {id}"
    }

