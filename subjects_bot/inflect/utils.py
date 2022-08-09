from subjects_bot.inflect.load import load_dict

from subjects_bot.inflect.exceptions import *

dictionary = load_dict()

def get_entry(word):
    """Get word entry object."""

    for entry in dictionary.entries:
        
        if entry.lemma == word:
            return entry
        
        for inflected in entry.inflections:

            if inflected.form == word:
                return entry
    
    raise WordNotFound

def get_pos(word):
    """Get word nature."""

    entry = get_entry(word)

    return entry.pos

def get_inflection(form):
    """Get word inflection."""

    for entry in dictionary.entries:

        for inflected in entry.inflections:

            if inflected.form == form:

                return inflected

def inflect_adjective(adjective, gender, number):
    """Get specific inflection of an adjective."""

    entry = get_entry(adjective)

    for inflected in entry.inflections:
        if inflected.gender == gender and inflected.number == number:
            return inflected.form
    
    raise InflectionNotFound

if __name__ == "__main__":
    print(inflect_adjective("lent", "feminine", "plural"))
