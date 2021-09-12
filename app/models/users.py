from pydantic import BaseModel
from datetime import datetime


class UserIn(BaseModel):
    username: str
    password: str
    email: str
    level_access: int

    class Config:
        schema_extra = {
            'example': {
                'username': 'user1',
                'password': '1234',
                'email': 'email@gmail.com',
                'level_access': 1
            }
        }


class User(BaseModel):
    id: int
    username: str
    email: str
    create_at: datetime
    update_at: datetime
    level_access: int


class UserUpdate(BaseModel):
    password: str
    email: str

    class Config:
        schema_extra = {
            'example': {
                'password': 'new_pwd',
                'email': 'new_email'
            }
        }


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'email': 'email@gmail.com',
                'password': '1234'
            }
        }
