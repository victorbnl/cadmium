#-*- coding: utf-8 -*-

import yaml
import random
from PyProbs import Probability as pr

import utils.inflect as inflect

verb_prob = 0.3

def get(type):
    """Get a random item of a given type"""

    with open("data/lists/{}s.yml".format(type), "r") as file_:
        items = yaml.safe_load(file_)
    return random.choice(items)

def get_subject():
    """Generate a random subject"""

    global verb_prob

    subject = []

    is_verb = pr.Prob(verb_prob)

    # Verb
    if (is_verb):
        verb_prob -= 0.2
        subject.append(get("verb"))

        # Adverb
        add_adverb = pr.Prob(0.75)
        if (add_adverb):
            subject.append(get("adverb"))

    # Noun
    else:
        verb_prob += 0.2
        
        noun = get("noun")
        subject.append(noun)
        
        # Adjective
        add_adjective = pr.Prob(0.8)
        if (add_adjective):
            noun_inf = inflect.get_word_inf(noun)
            gender = noun_inf["gender"]
            number = noun_inf["number"]

            adjective = get("adjective")
            subject.append(inflect.inflect(adjective, gender, number))

            # Second adjective
            add_second_adjective = pr.Prob(0.25)
            if (add_second_adjective):
                second_adjective = get("adjective")
                subject.append(inflect.inflect(second_adjective, gender, number))
    
    return " ".join(subject)

if __name__ == "__main__":
    print(get_subject())
