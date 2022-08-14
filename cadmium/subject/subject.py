"""Get subject."""

from typing import Dict, List
import random

from PyProbs import Probability

from cadmium.subject.classes import Subject
from cadmium.subject.exceptions import EmptyWordListError


class SubjectGenerator():

    def __init__(
        self,
        words,
        probs
    ):
        self.words = words
        self.probs = probs

    def prob(self, nature: str) -> bool:
        """Choose whether word type is chosen or not according to prob."""

        return Probability.Prob(getattr(self.probs, nature))

    def get_word(self, nature: str) -> str:
        """Get a random word with the given nature."""

        if len(getattr(self.words, nature)) > 0:
            return random.choice(getattr(self.words, nature))

        else:
            raise EmptyWordListError(f"Empty word list: {nature}")

    def get_subject(self) -> str:
        """Generate a random subject."""

        noun = adjective = second_adjective = verb = adverb = None

        # Verb
        if self.prob('verb'):
            verb = self.get_word('verb')

            # Adverb
            if self.prob('adverb'):
                adverb = self.get_word('adverb')

        # Noun
        else:
            noun = self.get_word('noun')

            # Adjective
            if self.prob('adjective'):
                adjective = self.get_word('adjective')

                # Second adjective
                if self.prob('second_adjective'):
                    second_adjective = self.get_word('adjective')

        return Subject(
            verb=verb,
            adverb=adverb,
            noun=noun,
            adjective=adjective,
            second_adjective=second_adjective
        )


def get_subject(words: Dict[str, List[str]], probs: Dict[str, int]):
    """Get a random subject."""

    return SubjectGenerator(words=words, probs=probs).get_subject()
