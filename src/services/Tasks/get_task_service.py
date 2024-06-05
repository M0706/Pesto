from datetime import timezone, datetime
from src.db.connect import Database
from src.db.query import Query
from src.logger import logger
from src.db.transaction import Transaction


async def get_task_for_user(task_object):
    db_instance = await Database.get_instance()
    tasks_for_user = await db_instance.fetch(Query.get_task_for_user_query, task_object.user_id)
    return tasks_for_user

