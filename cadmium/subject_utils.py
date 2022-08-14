from cadmium import inflect
from cadmium.subject.classes import Subject


def inflect_subject_adjectives(subject: Subject):
    """Inflect each adjective of the subject to agree with its noun."""

    if subject.noun and subject.adjective:
        inf = inflect.get_inflection(subject.noun)
        gender = inf['gender']
        number = inf['number']

        subject.adjective = inflect.inflect_adjective(
            subject.adjective, gender, number
        )

        if subject.second_adjective:
            subject.second_adjective = inflect.inflect_adjective(
                subject.second_adjective, gender, number
            )

    return subject


def format_subject(subject: Subject):
    """Format a subject into a string."""

    subject = inflect_subject_adjectives(subject)

    string = []

    if subject.verb:
        string.append(subject.verb)

        if subject.adverb:
            string.append(subject.adverb)

    elif subject.noun:
        string.append(subject.noun)

        if subject.adjective:
            string.append(subject.adjective)

            if subject.second_adjective:
                string.append(subject.second_adjective)

    return ' '.join(string)
