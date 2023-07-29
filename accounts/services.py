from accounts.schemas import UserSchemaAdd
from core.repositories import AbstractRepository


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_one(self, user: UserSchemaAdd):
        user_dict = user.model_dump()
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def get_all(self):
        users = await self.users_repo.find_all()
        return users
