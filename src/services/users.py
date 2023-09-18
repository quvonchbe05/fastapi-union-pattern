from src.utils.repository import AbstractRepository


class UserService:
    def __init__(self, users_repository: AbstractRepository):
        self.users_repository = users_repository

    async def find_all(self):
        users = await self.users_repository().find_all()
        return users
