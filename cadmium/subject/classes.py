from dataclasses import dataclass
from typing import List


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
class Subject():
    noun: str
    adjective: str
    second_adjective: str
    verb: str
    adverb: str
