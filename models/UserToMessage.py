from .db import db
from peewee import IntegerField, Model, AutoField


class UserToMessage(Model):
    id = AutoField()
    user_id = IntegerField()
    message_id = IntegerField()

    class Meta:
        database = db
