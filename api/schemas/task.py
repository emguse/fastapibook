from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str | None = Field(None, example="Go pick up the finished laundry")


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="Completion flag")

    class Config:
        orm_mode = True


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
