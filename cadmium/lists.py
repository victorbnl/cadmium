"""Access and manage word lists database items."""

from peewee import CharField, Model, SqliteDatabase


db = SqliteDatabase('data/words.db')


class Word(Model):
    word = CharField()

    @classmethod
    def items(cls):
        """Get all the items of the list."""

        return [x.word for x in cls.select()]

    @classmethod
    def add(cls, word):
        """Add a word to the list."""

        cls.create(word=word)

    @classmethod
    def remove(cls, word):
        """Remove a word from the list."""

        cls.delete().where(cls.word == word).execute()

    @classmethod
    def update(cls, word):
        """
        Adds a word to the list if it doesn't exist, delete it if it does.
        """

        res = list(cls.select().where(cls.word == word))

        if len(res) > 0:
            res[0].delete_instance()
        else:
            cls.create(word=word)

    class Meta:
        database = db


class Noun(Word):
    pass


class Adjective(Word):
    pass


class Verb(Word):
    pass


class Adverb(Word):
    pass


db.create_tables([Noun, Adjective, Verb, Adverb])


noun = Noun
adjective = Adjective
verb = Verb
adverb = Adverb
