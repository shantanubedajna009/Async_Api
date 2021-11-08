from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from schemas.user import UserCreate
from ..models.users import User
from core.hasher import Hasher



def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.name,
        email=user.email,
        hashed_password=Hasher.hash_pwd(user.password),
        is_active=True,
        is_superuser=False
        
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user