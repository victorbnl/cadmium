"""Get subject."""

from typing import Dict, List
import random

from PyProbs import Probability
from loguru import logger

from cadmium.subject.classes import Subject, Token
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

        prob = float(getattr(self.probs, nature))
        result = Probability.Prob(prob)

        logger.debug(f"{'Getting' if result else 'Not getting'} {nature} (probs were {prob})")

        return result

    def get_word(self, nature: str) -> str:
        """Get a random word with the given nature."""

        # List not empty
        if len(getattr(self.words, nature)) > 0:
            return random.choice(getattr(self.words, nature))

        # List empty
        else:
            raise EmptyWordListError(f"Empty word list: {nature}")

    def get_subject(self) -> str:
        """Generate a random subject."""

        logger.info("Getting a subject")

        tokens = []

        # Verb
        if self.prob('verb'):
            type = 'verb'

            verb = self.get_word('verb')
            logger.debug(f"Adding verb: {verb}")
            tokens.append(Token('verb', verb))

            # Adverb
            if self.prob('adverb'):
                adverb = self.get_word('adverb')
                logger.debug(f"Adding adverb: {adverb}")
                tokens.append(Token('adverb', adverb))

        # Noun
        else:
            type = 'noun'

            noun = self.get_word('noun')
            logger.debug(f"Adding noun: {noun}")
            tokens.append(Token('noun', noun))

            # Adjective
            if self.prob('adjective'):
                adjective = self.get_word('adjective')
                logger.debug(f"Adding adjective: {adjective}")
                tokens.append(Token('adjective', adjective))

                # Second adjective
                if self.prob('second_adjective'):
                    second_adjective = self.get_word('adjective')
                    logger.debug(f"Adding adjective: {second_adjective}")
                    tokens.append(Token('adjective', second_adjective))

        subject = Subject(type=type, tokens=tokens)

        logger.info(f"Got subject {[token.text for token in tokens]}")

        return subject


def get_subject(words: Dict[str, List[str]], probs: Dict[str, int]):
    """Get a random subject."""

    return SubjectGenerator(words=words, probs=probs).get_subject()
