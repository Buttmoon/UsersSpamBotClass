from .Account import Account
from .db import db
from peewee import CharField, Model, AutoField, DateField, IntegerField
from datetime import datetime


class AccountGroup(Model):
    id = AutoField()
    title = CharField(max_length=255)
    created_at = DateField(default=datetime.now())
    group_owner = IntegerField()

    class Meta:
        database = db


class AccountToGroup(Model):
    id = AutoField()
    account_id = IntegerField()
    group_id = IntegerField()

    class Meta:
        database = db
