from accounts.models import Users
from core.repositories import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users
