import databases
from app.config import database, users
import app.utils as Utils
import bcrypt


async def list_all_users() -> dict:
    query = users.select()
    return await database.fetch_all(query)


async def create_new_user(user) -> int:
    query = users.select().where(users.c.username == user.username)
    user_db = await database.fetch_one(query)
    if user_db:
        return None
    query = users.insert().values(
        username=user.username,
        password=hash_password(user.password),
        email=user.email,
        level_access=user.level_access
    )
    return await database.execute(query)


async def update_user(user: str, username: str) -> int:
    query = users.update().where(users.c.username == username).values(
        password=hash_password(user.password),
        email=user.email
    )
    return await database.execute(query)


async def delete_user(username: str) -> int:
    query = users.delete().where(users.c.username == username)
    return await database.execute(query)


async def get_user_by_email(email: str) -> dict:
    query = users.select().where(users.c.email == email)
    return await database.fetch_one(query)


def verify_password(password_send: str, password_db: str) -> bool:
    if bcrypt.checkpw(Utils.encode_utf(password_send), password_db):
        return True
    return None


def hash_password(password: str) -> str:
    return bcrypt.hashpw(Utils.encode_utf(password), bcrypt.gensalt())
