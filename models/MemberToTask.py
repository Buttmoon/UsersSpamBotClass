from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime
from .Task import Task
from .Member import Member


class MemberToTask(Model):
    id = AutoField()
    member_id = ForeignKeyField(Member)
    task_id = ForeignKeyField(Task)

    class Meta:
        database = db
