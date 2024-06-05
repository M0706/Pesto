Add an environment file. In that add posgres connection string:
POSTGRES_DB_STRING = "postgresql://postgres:postgres@localhost:5432/postgres"

Once that is done, in the database add two tables: User and tasks.
Please follow the model for both the tables as mentioned the models folder

Error handling is done using the decorator design pattern in fastapi

For running the code: after installing the virtual environment and doing the package install:

python3 main.py
