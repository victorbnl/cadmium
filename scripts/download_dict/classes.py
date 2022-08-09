from dataclasses import dataclass

from typing import *


@dataclass
class Inflected:
    form: str
    gender: Optional[Literal["masculine", "feminine"]]
    tense: Optional[Literal["ind", "cond"]]
    person: Optional[Literal["1", "2", "3", "4", "5", "6"]]
    number: Optional[Literal["singular", "plural"]]


@dataclass
class Entry:
    lemma: str
    pos: Literal["noun", "adj", "adverb", "verb"]
    compound: Optional[Literal["comp"]]
    inflections: List[Inflected]


@dataclass
class Dict:
    entries: List[Entry]
