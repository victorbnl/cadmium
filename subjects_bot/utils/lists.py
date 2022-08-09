from peewee import *

import random

db = SqliteDatabase("data/words.db")

class Word(Model):
    word = CharField()

    @classmethod
    def get_random(cls):
        return random.choice(list(
            cls.select()
        )).word
    
    @classmethod
    def add(cls, word):
        cls.create(word=word)
    
    @classmethod
    def remove(cls, word):
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

if __name__ == "__main__":
    print(Noun.get_random())
