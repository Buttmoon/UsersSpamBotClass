from datetime import datetime
from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, DateField, IntegerField
from models import db
from .Types import MemberStatus, Language, Gender


class Member(Model):
    id = AutoField()
    user_id = IntegerField(unique=True, null=False)
    username = CharField(default=255, null=True)
    first_name = CharField(default=255, null=True)
    last_name = CharField(default=255, null=True)
    phone = CharField(default=255, null=True)
    is_avatar = BooleanField(default=True)
    is_bot = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    language = ForeignKeyField(Language)
    gender = ForeignKeyField(Gender)
    status_id = ForeignKeyField(MemberStatus)
    created_at = DateField(default=datetime.now)
    updated_at = DateField()

    class Meta:
        database = db
