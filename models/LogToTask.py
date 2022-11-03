from .db import db
from peewee import Model, AutoField, ForeignKeyField
from .Task import Task
from .LogData import LogData


class LogToTask(Model):
    id = AutoField()
    log_id = ForeignKeyField(LogData)
    task_id = ForeignKeyField(Task)

    class Meta:
        database = db

