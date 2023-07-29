from tasks.models import Tasks
from core.repositories import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Tasks
