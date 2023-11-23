from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="Go pick up the finished laundry")
    done: bool = Field(False, description="Completion flag")
