from datetime import datetime
from peewee import Model, AutoField, DateField, TextField
from .db import db


class Message(Model):
    id = AutoField()
    content = TextField()
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
