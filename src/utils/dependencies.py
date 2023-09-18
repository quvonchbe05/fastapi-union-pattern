from src.repositories.users import UsersRepository
from src.services.users import UserService


def users_service():
    return UserService(UsersRepository)