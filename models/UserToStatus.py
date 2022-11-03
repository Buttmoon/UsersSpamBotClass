from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime
from .User import UserStatus,User,UserSettings


class UserToStatus(Model):
    id = AutoField()
    status_id = ForeignKeyField(UserStatus)
    user_id = ForeignKeyField(User)

    class Meta:
        database = db


class UserToSettings(Model):
    id = AutoField()
    settings_id = ForeignKeyField(UserSettings)
    user_id = ForeignKeyField(User)

    class Meta:
        database = db
