from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime
from .User import User
from .Task import Task


class UserToTask(Model):
    id = AutoField()
    user_id = ForeignKeyField(User)
    task_id = ForeignKeyField(Task)

    class Meta:
        database = db
        