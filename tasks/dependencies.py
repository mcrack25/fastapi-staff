from tasks.repositories import TasksRepository
from tasks.services import TasksService


def tasks_service():
    return TasksService(TasksRepository)
