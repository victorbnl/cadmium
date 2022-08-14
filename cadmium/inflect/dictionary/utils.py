"""Some useful functions to access specific dictionary elements."""

from cadmium.inflect.dictionary.database import Entry, Inflection


def get_inflection(word):
    """Get noun gender and number."""

    res = (
        Inflection.select(Inflection.gender, Inflection.number)
        .where(Inflection.form == word)
        .get()
    )

    return {'gender': res.gender, 'number': res.number}


def inflect_adjective(adjective, gender, number):
    """Inflect adjective according to gender and number."""

    adjective_entry_id = (
        Inflection.select(Inflection.entry_id)
        .where(Inflection.form == adjective)
        .get()
        .entry_id
    )

    return (
        Inflection.select(Inflection.form)
        .where(
            (Inflection.entry_id == adjective_entry_id)
            & (Inflection.gender == gender)
            & (Inflection.number == number)
        )
        .get()
        .form
    )
