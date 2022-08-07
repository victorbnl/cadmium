"""Subjects."""

import yaml
import random
from PyProbs import Probability as pr

from inflect import Inflect
from exceptions import *

from utils import config

inflect = Inflect()

items = {}
for list in ("noun", "adjective", "verb", "adverb"):
    with open(f"data/lists/{list}s.yml", "r") as file_:
        items[list] = yaml.safe_load(file_)


def change_verb_prob(inc):
    """Increment or decrement verb probability"""

    current_verb_prob = float(config.get("probs.verb"))
    step = float(config.get("probs.verb_step"))

    if inc:
        new_verb_prob = current_verb_prob + step
    else:
        new_verb_prob = current_verb_prob - step

    new_verb_prob = round(new_verb_prob, 2)

    if new_verb_prob < 0:
        new_verb_prob = 0
    elif new_verb_prob > 1:
        new_verb_prob = 1

    config.set("probs.verb", new_verb_prob)


def get_subject():
    """Generate a random subject"""

    global verb_prob

    subject = []

    is_verb = pr.Prob(float(config.get("probs.verb")))

    # Verb
    if is_verb:
        change_verb_prob(False)
        subject.append(random.choice(items["verb"]))

        # Adverb
        add_adverb = pr.Prob(float(config.get("probs.adverb")))
        if add_adverb:
            subject.append(random.choice(items["adverb"]))

    # Noun
    else:
        change_verb_prob(True)

        noun = random.choice(items["noun"])
        subject.append(noun)

        # Adjective
        add_adjective = pr.Prob(float(config.get("probs.adjective")))
        if add_adjective:
            try:
                form = inflect.get_word_attrs(noun)
            except WordNotInDictionaryError:
                form = "ms"

            adjectives = items["adjective"]
            adjective = random.choice(adjectives)
            try:
                inflected_adj = inflect.inflect_word(adjective, form)
            except WordNotInDictionaryError:
                inflected_adj = adjective

            subject.append(inflected_adj)

            adjectives.remove(adjective)

            # Second adjective
            add_second_adjective = pr.Prob(float(config.get("probs.second_adjective")))
            if add_second_adjective:

                second_adjective = random.choice(adjectives)
                try:
                    inflected_second_adj = inflect.inflect_word(second_adjective, form)
                except WordNotInDictionaryError:
                    inflected_second_adj = second_adjective

                subject.append(inflected_second_adj)

    return " ".join(subject)


if __name__ == "__main__":
    print(get_subject())
