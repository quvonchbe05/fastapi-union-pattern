from fastapi import APIRouter, Depends
from src.services.users import UserService
from src.utils.dependencies import users_service
from src.schemas.users import UserListSchema


router = APIRouter(tags=["Users"], prefix="/api/users")


@router.get("/list", response_model=list[UserListSchema])
async def user_list(users_service: UserService = Depends(users_service)):
    users = await users_service.find_all()
    return users.all()
