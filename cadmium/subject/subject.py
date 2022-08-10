"""Subjects."""

from PyProbs import Probability

from cadmium import config
from cadmium import lists

from cadmium.subject.classes import Subject

def prob(nature):
    """Determine nature and existence of word according to defined probabilities."""

    return Probability.Prob(float(config.get(f"probs_{nature}")))

def get_word(list_):
    """Get a random word from a list."""

    return lists.lists[list_].get_random()

def change_verb_prob(factor):
    """Increment or decrement verbs probabilities."""

    verb_prob = float(config.get("probs_verb"))
    step = float(config.get("probs_verb_step"))

    new_verb_prob = round(verb_prob + factor * step, 1)

    if new_verb_prob < 0:
        new_verb_prob = 0
    elif new_verb_prob > 1:
        new_verb_prob = 1

    config.set("probs_verb", new_verb_prob)

def get_subject():
    """Generate a random subject."""

    verb = adverb = noun = adjective = second_adjective = None

    # Verb
    if prob("verb"):
        type = "verb"
        verb = get_word("verbs")

        # Verb picked ; decrease noun prob
        change_verb_prob(-1)

        # Adverb
        if prob("adverb"):
            adverb = get_word("adverbs")

    # Noun
    else:
        type = "noun"
        noun = get_word("nouns")

        # Noun picked ; decrease verb prob
        change_verb_prob(+1)

        # Adjective
        if prob("adjective"):
            adjective = get_word("adjectives")

            # Second adjective
            if prob("second_adjective"):
                second_adjective = get_word("adjectives")

    return Subject(type, noun, verb, adverb, adjectives=[adjective, second_adjective])
