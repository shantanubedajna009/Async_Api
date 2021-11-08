from passlib import context
from passlib.context import CryptContext
from typing import Optional
from passlib.utils.decor import deprecated_method


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hasher(object):

    @staticmethod
    def verify_pwd(plain_pwd, hashed_pwd) -> str:
        return pwd_context.verify(plain_pwd, hashed_pwd)
    
    @staticmethod
    def hash_pwd(plain_pwd) -> str:
        return pwd_context.hash(plain_pwd)