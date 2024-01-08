from peewee import *

db = SqliteDatabase('database.db')


class Person(Model):
    name = CharField()
    phone = CharField()

    class Meta:
        database = db
