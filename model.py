from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):
    # TODO: Add model fields here

    class Meta:
        database = db


class Task(Model):
    # TODO: Add model fields here

    class Meta:
        database = db
