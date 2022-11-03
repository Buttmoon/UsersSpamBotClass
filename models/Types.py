from datetime import datetime
from peewee import Model, AutoField, CharField, ForeignKeyField, DateField, ManyToManyField,IntegerField
from .db import db


class TaskType(Model):
    id = AutoField()
    title = CharField()

    class Meta:
        database = db


class TaskStatus(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class ProxyType(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class AccountStatus(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class ChatStatus(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class MemberStatus(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class Language(Model):
    id = AutoField()
    title = CharField(max_length=10)

    class Meta:
        database = db


class Gender(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db


class UserStatus(Model):
    id = AutoField()
    title = CharField(max_length=255)

    class Meta:
        database = db



