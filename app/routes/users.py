from fastapi import APIRouter, HTTPException, Depends, status
from app.models import UserIn, UserUpdate
from app.controllers import UserController
from app.auth import JWTBearer
import logging


router = APIRouter()


@router.get('/list-all-users', response_description='List all users', dependencies=[Depends(JWTBearer())])
async def list_users():
    try:
        return await UserController.list_all_users()
    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False})


@router.post('/create-user', response_description='Create new user')
async def create_user(user: UserIn):
    user = await UserController.create_new_user(user)
    if user:
        return {'detail': {'status': True, 'message': 'created'}}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False, 'message': 'username already exists'})


@router.put('/update-user/{username}', response_description='Update registration data', dependencies=[Depends(JWTBearer())])
async def update_user(user: UserUpdate, username):
    try:
        updated_id = await UserController.update_user(user, username)
        if updated_id == 0:
            return {'detail': {'status': False, 'message': 'username not found'}}
    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False})
    return {'detail': {'status': True, 'message': 'updated'}}


@router.delete('/delete-user/{username}', response_description='Delete user in database', dependencies=[Depends(JWTBearer())])
async def delete_user(username):
    try:
        deleted_id = await UserController.delete_user(username)
        if deleted_id == 0:
            return {'detail': {'status': False, 'message': 'username not found'}}
    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'status': False})
    return {'detail': {'status': True, 'message': 'deleted'}}
