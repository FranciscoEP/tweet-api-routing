from uuid import UUID
from datetime import date
from typing import Optional
# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class User_Base(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(User_Base):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
    )

class User(User_Base):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        )
    birth_date: Optional[date] = Field(default=None)

