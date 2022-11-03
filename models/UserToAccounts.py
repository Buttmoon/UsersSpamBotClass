from .db import db
from peewee import Model, AutoField, IntegerField


class UserToAccounts(Model):
    id = AutoField()
    user_id = IntegerField()
    account_id = IntegerField()

    class Meta:
        database = db
