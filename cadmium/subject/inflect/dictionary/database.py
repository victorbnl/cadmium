"""Access and manage inflections dictionary database."""

from peewee import CharField, ForeignKeyField, Model, SqliteDatabase

db = SqliteDatabase("data/dictionary.db")


class BaseModel(Model):
    class Meta:
        database = db


class Entry(BaseModel):
    lemma = CharField()
    pos = CharField()

    @classmethod
    def add(cls, lemma, pos):
        return cls.insert(lemma=lemma, pos=pos).execute()


class Inflection(BaseModel):
    entry_id = ForeignKeyField(Entry)
    form = CharField()
    gender = CharField(null=True)
    number = CharField(null=True)


db.create_tables([Entry, Inflection])
