class Query:
    user_select_query = 'SELECT * FROM public."users" WHERE userid = $1'
    update_user_balance = 'UPDATE public."users" SET balance=$1 WHERE userid=$2'
    get_all_users_query = 'Select * from public."users"'

    task_select_query = 'SELECT * FROM tasks WHERE task_id = $1'
    create_task_query = '''
        INSERT INTO tasks (task_id, user_id, title, description, time_to_complete, is_complete)
        VALUES ($1, $2, $3, $4, $5, $6)
        RETURNING task_id, user_id, title, description, time_to_complete, is_complete
    '''
    update_task_query = '''
        UPDATE tasks
        SET title=$1, description=$2, time_to_complete=$3, is_complete=$4
        WHERE task_id=$5
        RETURNING task_id, user_id, title, description, time_to_complete, is_complete
    '''
    get_all_tasks_query = 'SELECT * FROM tasks'

    get_task_for_user_query = 'SELECT * FROM tasks WHERE user_id=$1'

