from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()

@router.post('/users')
def creat_user(user: UserCreate, db: Session=Depends(get_db)):
    user = create_new_user(user, db)

    return user


