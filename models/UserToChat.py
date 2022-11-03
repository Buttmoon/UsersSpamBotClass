from .User import User
from .Chat import Chat
from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime


class UserToChat(Model):
    id = AutoField()
    chat_id = ForeignKeyField(Chat)
    user_id = ForeignKeyField(User)

    class Meta:
        database = db
