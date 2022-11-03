from datetime import datetime
from peewee import Model, AutoField, DateField, TextField, IntegerField
from .db import db


class LogData(Model):
    id = AutoField()
    cur_user_id = IntegerField()
    data = TextField()
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
