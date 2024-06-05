from pydantic import BaseModel, Field
from src.models.task_model import TaskModel

class User(BaseModel):
    user_id: str = Field(alias="user_id", max_length=2000, min_length=6)
    name: str
    task: list[TaskModel] = []


class UserIdModel(BaseModel):
    user_id: str = Field(alias="user_id", max_length=2000, min_length=6)
