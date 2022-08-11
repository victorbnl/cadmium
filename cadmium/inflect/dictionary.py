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


def get_inflection(word):
    """Get noun gender and number."""

    res = (
        Inflection.select(Inflection.gender, Inflection.number)
        .where(Inflection.form == word)
        .get()
    )

    return {"gender": res.gender, "number": res.number}


def inflect_adjective(adjective, gender, number):
    """Inflect adjective according to gender and number."""

    adjective_entry_id = (
        Inflection.select(Inflection.entry_id)
        .where(Inflection.form == adjective)
        .get()
        .entry_id
    )

    return (
        Inflection.select(Inflection.form)
        .where(
            (Inflection.entry_id == adjective_entry_id)
            & (Inflection.gender == gender)
            & (Inflection.number == number)
        )
        .get()
        .form
    )


db.create_tables([Entry, Inflection])
