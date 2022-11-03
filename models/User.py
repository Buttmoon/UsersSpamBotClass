from .Types import Language, Gender, UserStatus
from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime


class UserSettings(Model):
    id = AutoField()
    spam_limit_msg = IntegerField(null=True)
    spam_min_delay_msg = IntegerField(null=True)
    spam_max_delay_msg = IntegerField(null=True)
    is_spam_repeated = BooleanField(default=False)
    cheat_min_delay_view = IntegerField(null=True)
    cheat_max_delay_view = IntegerField(null=True)
    cheat_min_delay_reaction = IntegerField(null=True)
    cheat_max_delay_reaction = IntegerField(null=True)
    cheat_min_delay_follow = IntegerField(null=True)
    cheat_max_delay_follow = IntegerField(null=True)
    cheat_min_delay_comment = IntegerField(null=True)
    cheat_max_delay_comment = IntegerField(null=True)

    class Meta:
        database = db


class User(Model):
    id = AutoField()
    first_name = CharField(max_length=64, null=True)
    last_name = CharField(max_length=64, null=True)
    username = CharField(max_length=33, null=True)
    language_code = CharField(null=True)
    user_id = IntegerField(null=False, unique=True)
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
