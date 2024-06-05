import json
from fastapi import APIRouter
from src.logger import logger
from src.db.connect import Database
from src.models.user_model import UserIdModel
from src.models.task_model import TaskModel, CreateTaskModel, GetTasksForUserModel
from src.services.User.user_services import get_user_details, get_all_users
from src.services.Tasks.create_task import create_task
from src.services.Tasks.get_task_service import get_task_for_user
from src.exceptions.exception_decorators import handle_exceptions_decorator
task_router: APIRouter = APIRouter()



@task_router.post("/create_new_task")
@handle_exceptions_decorator
async def create_task_for_user_route(
    params: CreateTaskModel
):
    return await create_task(params)



@task_router.post("/get_tasks_for_user")
@handle_exceptions_decorator
async def get_task_for_user_route(
    params: GetTasksForUserModel
):
    return await get_task_for_user(params)

