from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4

class TaskModel(BaseModel):
    task_id: str = Field(alias="task_id", max_length=2000, min_length=6)
    title: str
    description: str
    time_to_complete: datetime
    is_complete: bool

class CreateTaskModel(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid4()), alias="task_id")
    user_id: str
    title: str
    description: str
    time_to_complete: datetime
    is_complete: bool = False

class GetTasksForUserModel(BaseModel):
    user_id: str
