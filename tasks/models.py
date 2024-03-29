from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base
from tasks.schemas import TaskSchema


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[int]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            author_id=self.author_id,
            assignee_id=self.assignee_id,
        )
