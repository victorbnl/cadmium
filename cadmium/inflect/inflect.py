from cadmium.inflect import dictionary


def inflect_subject(subject):
    """Make correct inflections on a subject."""

    if subject.type == "noun":

        noun_inflection = dictionary.get_inflection(subject.noun)
        gender = noun_inflection["gender"]
        number = noun_inflection["number"]

        for i in range(len(subject.adjectives)):
            adjective = subject.adjectives[i]

            if subject.adjectives[i]:
                subject.adjectives[i] = dictionary.inflect_adjective(
                    adjective, gender, number
                )

    return subject
