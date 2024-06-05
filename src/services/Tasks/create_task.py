from datetime import timezone, datetime
from src.db.connect import Database
from src.db.query import Query
from src.logger import logger
from src.db.transaction import Transaction


async def create_task(task_object):
    db_instance = await Database.get_instance()
    print (task_object.time_to_complete, type(task_object.time_to_complete))
    create_task = await db_instance.fetch(Query.create_task_query,
                                      task_object.task_id,
                                      task_object.user_id,
                                      task_object.title,
                                      task_object.description,
                                      task_object.time_to_complete,
                                      task_object.is_complete)


    if(create_task):
        return {
            "task_added": True
        }

async def update_task(task_object):
    db_instance = await Database.get_instance()

    create_task = await db_instance.fetch(Query.update_task_query,
                                      task_object.title,
                                      task_object.description,
                                      task_object.time_to_complete,
                                      task_object.is_complete,
                                      task_object.task_id)


    if(create_task):
        return {
            "task_updated": True
        }
