from datetime import datetime
from pydantic import EmailStr
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel


class CreateUser(SQLModel):
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


class User(CreateUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
