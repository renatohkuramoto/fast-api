from fastapi import APIRouter, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from app.models import UserLogin
from app.controllers import UserController
from app.auth import JWTHandler
import logging

router = APIRouter()


@router.post('/login', response_description='Get access token', name='Authentication')
async def login(user: UserLogin = Body(...)):
    user = jsonable_encoder(user)
    try:
        user_db = await UserController.get_user_by_email(user['email'])
        if user_db:
            password_db = user_db['password']
            if UserController.verify_password(user['password'], password_db):
                return JWTHandler.sing_in(user['email'])
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={'status': False, 'message': 'Invalid credentials'})
    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail={'status': False, 'message': 'Invalid credentials'})
