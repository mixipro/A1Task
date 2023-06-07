from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    gender: str
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str
    birthday: datetime
    nationality: str
    cell: str
    location_street: str
    location_street_number: int
    location_city: str
    location_state: str
    location_country: str
    location_postcode: str


class CreateUser(BaseModel):
    gender: str
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str
    birthday: datetime
    nationality: str
    cell: str
    location_street: str
    location_street_number: int
    location_city: str
    location_state: str
    location_country: str
    location_postcode: str
