"""Subjects."""

from PyProbs import Probability

from subjects_bot.utils import config
from subjects_bot.utils import lists

from subjects_bot.subject.classes import Subject

probs = config.get("probs")


def prob(nature):
    """Determine nature and existence of word according to defined probabilities."""

    return Probability.Prob(probs[nature])


def get_word(list_):
    """Get a random word from a list."""

    if list_ == "nouns":
        return lists.Noun.get_random()
    elif list_ == "adjectives":
        return lists.Adjective.get_random()
    elif list_ == "verbs":
        return lists.Verb.get_random()
    elif list_ == "adverbs":
        return lists.Adverb.get_random()


def get_subject():
    """Generate a random subject."""

    verb = adverb = noun = adjective = second_adjective = None

    # Verb
    if prob("verb"):
        type = "verb"
        verb = get_word("verbs")

        # Adverb
        if prob("adverb"):
            adverb = get_word("adverbs")

    # Noun
    else:
        type = "noun"
        noun = get_word("nouns")

        # Adjective
        if prob("adjective"):
            adjective = get_word("adjectives")

            # Second adjective
            if prob("second_adjective"):
                second_adjective = get_word("adjectives")

    return Subject(
        type,
        noun,
        verb,
        adverb,
        adjectives=[adjective, second_adjective]
    )
