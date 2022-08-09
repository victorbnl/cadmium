from peewee import *

import random

db = SqliteDatabase("data/words.db")

class Word(Model):
    word = CharField()

    @classmethod
    def items(cls):
        """Get all the items of the list."""

        return [x.word for x in cls.select()]

    @classmethod
    def get_random(cls):
        """Get a random word from the list."""

        return random.choice(list(
            cls.select()
        )).word
    
    @classmethod
    def add(cls, word):
        """Add a word to the list."""

        cls.create(word=word)
    
    @classmethod
    def remove(cls, word):
        """Remove a word from the list."""

        cls.delete().where(cls.word == word).execute()
    
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

lists = {
    "nouns": Noun,
    "adjectives": Adjective,
    "verbs": Verb,
    "adverbs": Adverb
}
