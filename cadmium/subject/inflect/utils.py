"""Some useful functions to access specific dictionary elements."""

from loguru import logger

from cadmium.subject.inflect.dictionary import Entry, Inflection


def get_inflection(word):
    """Get noun gender and number."""

    res = (
        Inflection.select(Inflection.gender, Inflection.number)
        .where(Inflection.form == word)
        .get()
    )

    gender = res.gender
    number = res.number
    inflection = {'gender': gender, 'number': number}

    logger.debug(f"Getting inflection of word {word}: ({gender}, {number})")

    return inflection


def inflect_adjective(adjective, gender, number):
    """Inflect adjective according to gender and number."""

    adjective_entry_id = (
        Inflection.select(Inflection.entry_id)
        .where(Inflection.form == adjective)
        .get()
        .entry_id
    )

    inflected_adjective = (
        Inflection.select(Inflection.form)
        .where(
            (Inflection.entry_id == adjective_entry_id)
            & (Inflection.gender == gender)
            & (Inflection.number == number)
        )
        .get()
        .form
    )

    logger.debug(f"Inflecting adjective {adjective} ({gender}, {number}): {inflected_adjective}")

    return inflected_adjective
