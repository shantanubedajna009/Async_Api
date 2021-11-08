from fastapi import APIRouter
from .routes.route_users import router as user_router

main_router = APIRouter()

main_router.include_router(user_router, prefix='/user', tags=['users'])