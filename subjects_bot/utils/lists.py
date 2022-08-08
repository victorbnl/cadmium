"""Manage or use lists."""

import yaml
import random

class List():

    def __init__(self, type):
        self.type = type

        with open(f"data/lists/{self.type}.yml", "r") as file_:
            self.items = yaml.safe_load(file_)
    
    def get_random(self):
        """Get a random noun from the list."""

        return random.choice(self.items)

    def add(self, word):
        """Add a noun to the list."""

        if word not in self.items:
            self.items.append(word)
        
        self.write_list()
    
    def remove(self, word):
        """Remove a word from the list."""

        self.items.remove(word)

        self.write_list()

    def write_list(self):
        """Write the list on the disk."""

        with open(f"data/{self.type}.yml", "w") as file_:
            file_.write(yaml.dump(self.items, allow_unicode=True))

lists = {}
for type in ["adjectives", "adverbs", "nouns", "verbs"]:
    lists[type] = List(type)
