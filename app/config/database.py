import sqlalchemy
from databases import Database
from sqlalchemy.sql import func
from app.config.config import get_config_db

SQLALCHEMY_DATABASE_URL = get_config_db()['SQLITE']

database = Database(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()

access = sqlalchemy.Table(
    'access',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('description', sqlalchemy.String(50)),
)
users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(50)),
    sqlalchemy.Column('password', sqlalchemy.String(50)),
    sqlalchemy.Column('email', sqlalchemy.String(50)),
    sqlalchemy.Column('create_at', sqlalchemy.DateTime(timezone=True), server_default=func.now()),
    sqlalchemy.Column('update_at', sqlalchemy.DateTime(timezone=True), onupdate=func.now()),
    sqlalchemy.Column('level_access', sqlalchemy.Integer, sqlalchemy.ForeignKey('access.id'))
)

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
