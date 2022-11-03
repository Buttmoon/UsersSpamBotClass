from peewee import PostgresqlDatabase, SqliteDatabase

DATABASE = "Users_DB.sqlite3"

db = SqliteDatabase(DATABASE)


# db = PostgresqlDatabase(
#     database="spam_bot_db",
#     host="127.0.0.1",
#     user="postgres",
#     password="Adsd3WWsdas_suk",
#     port="5432"
# )