from datetime import datetime
from peewee import Model, AutoField, CharField, ForeignKeyField, BooleanField, DateField, IntegerField
from .Types import ProxyType, AccountStatus
from .db import db


class Proxy(Model):
    id = AutoField()
    type = ForeignKeyField(ProxyType)
    address = CharField(max_length=255)
    password = CharField(max_length=255)
    login = CharField(max_length=255)
    is_valid = BooleanField(default=True)
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db


class ConnectionData(Model):
    id = AutoField()
    api_id = IntegerField()
    api_hash = CharField(default=255)

    class Meta:
        database = db


class Account(Model):
    id = AutoField()
    proxy_id = IntegerField(null=True)
    status = ForeignKeyField(AccountStatus)
    phone = CharField(null=False)
    is_valid = BooleanField(default=True)
    connect_id = IntegerField(null=True)
    created_at = DateField(default=datetime.now)

    class Meta:
        database = db
