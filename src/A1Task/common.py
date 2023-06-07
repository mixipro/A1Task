from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseSettings

from sqlmodel import create_engine, SQLModel, Session, select
from starlette import status
import A1Task
from A1Task import PACKAGE_ROOT


# from A1Task.api.models import Users, TokenPurpose, User

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    db_host: str
    db_port: int

    class Config:
        env_file = '../../.env'
        env_file_encoding = 'utf-8'


def main():
    settings = get_database_url()
    print(settings)


def get_settings(env_path=None):
    if env_path is None:
        env_path = PACKAGE_ROOT / ".env"
    settings = Settings(_env_file=env_path, _env_file_encoding='utf-8')
    return settings


def get_database_url(env_path=None) -> str:
    if env_path is None:
        env_path = PACKAGE_ROOT / ".env"
    print(env_path)
    settings = Settings(_env_file=env_path, _env_file_encoding='utf-8')
    url = f'postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.db_host}:{settings.db_port}/{settings.postgres_db}'
    return url


engine = create_engine(get_database_url())


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session(env_path=None) -> Session:
    # engine = create_engine(get_database_url(env_path=env_path))
    # SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
