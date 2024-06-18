from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
load_dotenv()


class JwtModel(BaseModel):
    authjwt_secret_key: str = os.getenv('AUTHJWT_SECRET_KEY', 'default_secret_key')


class Registration(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_staff: bool

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Ali",
                "last_name": "Aliyev",
                "username": "Aliyev123",
                "email": "aliyev@gmail.com",
                "password": "****"

            }
        }


class Login(BaseModel):
    username: str
    password: str


class ProductM(BaseModel):
    id: int
    image: str
    name: str
    description: str
    price: int
    price_type: str
    slug: str
    count: int


class CommentM(BaseModel):
    id: int
    image: str
    name: str
    product_id: int
    slug: str
    comment: str


class BlogM(BaseModel):
    id: int
    image: str
    name: str
    slug: str
    who: str


class TeamM(BaseModel):
    id: int
    image: str
    name: str
    slug: str
    staff_type: str
    title: str







