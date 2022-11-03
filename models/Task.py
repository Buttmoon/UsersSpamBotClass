from datetime import datetime
from peewee import Model, AutoField, ForeignKeyField, DateField,IntegerField
from .Types import TaskStatus, TaskType
from .db import db


class Task(Model):
    id = AutoField()
    status_id = ForeignKeyField(TaskStatus)
    type_id = ForeignKeyField(TaskType)
    date_start = DateField(default=datetime.now)
    date_finish = DateField()
    user_settings_id = IntegerField()
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
