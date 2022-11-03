from .db import db
from peewee import CharField, IntegerField, Model, AutoField, ForeignKeyField, BooleanField, DateField, ManyToManyField
from datetime import datetime
from .Types import Gender
from .User import User


class UserToGender(Model):
    id = AutoField()
    gender_id = ForeignKeyField(Gender)
    user_id = ForeignKeyField(User)

    class Meta:
        database = db
