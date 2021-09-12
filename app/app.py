import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import database
from app.routes import UserRouter, AuthRouter

# Define tags URL Swagger
tags_metadata = [
    {
        "name": "Auth",
        "description": "Authentication access token",
    },
    {
        "name": "User",
        "description": "CRUD users",
    },
]

app = FastAPI(
    title="API Exemple",
    description="Perform user CRUD and JWT authentication",
    version="1.0.0",
    openapi_tags=tags_metadata,
    openapi_url='/swagger.json',
    redoc_url=None
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.on_event('startup')
async def startup():
    logging.warning('Connect database')
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    logging.warning('Disconnect database')
    await database.disconnect()


app.include_router(UserRouter, tags=['User'], prefix='/user')
app.include_router(AuthRouter, tags=['Auth'], prefix='/auth')
