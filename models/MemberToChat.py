from .Member import Member
from .Chat import Chat
from .db import db
from peewee import Model, AutoField, ForeignKeyField


class MemberToChat(Model):
    id = AutoField()
    chat_id = ForeignKeyField(Chat)
    member_id = ForeignKeyField(Member)

    class Meta:
        database = db
