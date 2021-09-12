import time
from typing import Dict
import jwt
from app.config import ConfigFile


JWT_SECRET = ConfigFile.get_secret_key()['SECRET_KEY']
JWT_ALGORITHM = ConfigFile.get_secret_key()['ALGO']


def token_response(token: str):
    return {
        "access_token": token
    }


def sing_in(email: str) -> Dict[str, str]:
    payload = {
        "email": email,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_token(token: str) -> dict:
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decoded if decoded["expires"] >= time.time() else None
    except Exception:
        return {}
