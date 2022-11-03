from datetime import datetime
from peewee import Model, AutoField, DateField, IntegerField, CharField
from models import db


class Chat(Model):
    id = AutoField()
    url = CharField()
    count_users = IntegerField()
    title = CharField()
    chat_id = IntegerField(null=False, unique=True)
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
