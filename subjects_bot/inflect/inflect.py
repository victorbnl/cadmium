from subjects_bot.inflect.exceptions import InflectionNotFound, WordNotFound

from subjects_bot.inflect import dictionary

dictionary = dictionary.Dictionary()

def inflect_subject(subject):
    """Make correct inflections on a subject."""

    if subject.type == "noun":

        noun_inflection = dictionary.get_inflection(subject.noun)
        gender = noun_inflection["gender"]
        number = noun_inflection["number"]

        for i in range(len(subject.adjectives)):
            adjective = subject.adjectives[i]
            
            try:
                subject.adjectives[i] = dictionary.inflect_adjective(adjective, gender, number)
            except (WordNotFound, InflectionNotFound):
                pass

    return subject
