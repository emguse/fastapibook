import datetime

from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="Go pick up the finished laundry")
    due_date: datetime.date | None = Field(None, example="2025-12-01")


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="Completion flag")

    class Config:
        orm_mode = True


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
