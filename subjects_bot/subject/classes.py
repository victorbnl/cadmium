from dataclasses import dataclass

from typing import *


@dataclass
class Subject:
    type: Literal["noun", "verb"]
    noun: str = None
    verb: str = None
    adverb: str = None
    adjectives: List[str] = None

    def to_string(self):
        """Returns the subject as a string."""

        string = []

        # Noun type
        if self.type == "noun":

            # Append noun
            if self.noun:
                string.append(self.noun)

            # Append adjectives
            if self.adjectives:
                string.extend(self.adjectives)

        # Verb type
        elif self.type == "verb":

            # Append verb
            if self.verb:
                string.append(self.verb)

            # Append adverb
            if self.adverb:
                string.append(self.adverb)

        return " ".join(string)
