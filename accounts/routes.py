from typing import Annotated

from fastapi import APIRouter, Depends

from accounts.dependencies import users_service
from accounts.schemas import UserSchemaAdd
from accounts.services import UsersService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(
    user: UserSchemaAdd,
    users_service: Annotated[UsersService, Depends(users_service)],
):
    user_id = await users_service.add_one(user)
    return {"user_id": user_id}


@router.get("")
async def get_users(
    users_service: Annotated[UsersService, Depends(users_service)],
):
    users = await users_service.get_all()
    return users
