from pydantic import EmailStr, BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str