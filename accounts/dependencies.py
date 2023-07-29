from accounts.repositories import UsersRepository
from accounts.services import UsersService


def users_service():
    return UsersService(UsersRepository)
