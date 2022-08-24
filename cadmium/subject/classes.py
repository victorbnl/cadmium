from dataclasses import dataclass
from typing import List, Literal

from cadmium.subject import inflect


@dataclass
class Words():
    noun: List[str]
    verb: List[str]
    adjective: List[str]
    adverb: List[str]


@dataclass
class Probs():
    verb: int
    adverb: int
    adjective: int
    second_adjective: int


@dataclass
class Token():
    pos: Literal['noun', 'verb', 'adj', 'adverb']
    text: str


@dataclass
class Subject():
    type: Literal['noun', 'verb']
    tokens: List[Token]

    def __str__(self):
        """Format subject as string"""

        # Get noun if there is one
        noun = None
        for token in self.tokens:
            if token.pos == 'noun':
                noun = token.text

        # Get noun gender & number
        gender = number = None
        if noun:
            inf = inflect.get_inflection(noun)
            gender = inf['gender']
            number = inf['number']

        # Inflect all adjectives
        for i, token in enumerate(self.tokens):
            if token.pos == 'adjective':
                inflected_adjective = inflect.inflect_adjective(token.text, gender, number)
                self.tokens[i] = Token('adjective', inflected_adjective)

        string = " ".join(token.text for token in self.tokens)

        return string
