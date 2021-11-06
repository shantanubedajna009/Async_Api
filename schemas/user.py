from pydantic import EmailStr, BaseModel
from typing import Optional





class User(BaseModel):
    name: str
    email: EmailStr
    password: str