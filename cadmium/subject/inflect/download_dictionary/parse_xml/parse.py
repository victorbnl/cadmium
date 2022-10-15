from lxml.etree import iterparse
from cadmium.subject.inflect.download_dictionary.parse_xml.classes import Dict, Entry, Inflected


def parse(xml):
    """Get deserialized XML dictionary."""

    # Variables
    entries = []
    inflections = []
    # Inflected variables
    form = tense = gender = number = person = None
    # Entry variables
    lemma = pos = None

    # Walk XML
    context = iterparse(xml, events=("end",))
    for _, elem in context:

        # Lemma
        if elem.tag == "lemma":
            lemma = elem.text

        # Pos
        if elem.tag == "pos":
            pos = elem.get("name")

        # Form
        if elem.tag == "form":
            form = elem.text

        # Feat
        if elem.tag == "feat":

            # Compound
            if elem.get("name") == "compound":
                compound = elem.get("value")

            # Tense
            elif elem.get("name") == "tense":
                tense = elem.get("value")

            # Person
            elif elem.get("name") == "person":
                person = elem.get("value")

            # Gender
            elif elem.get("name") == "gender":
                gender = elem.get("value")

            # Number
            elif elem.get("name") == "number":
                number = elem.get("value")

        # Inflected
        if elem.tag == "inflected":

            # If it's a noun, and adjective or a past participle verb
            if pos in ("noun", "adj") or (pos == "verb" and tense == "ppast"):

                # Add inflection to list
                inflections.append(
                    Inflected(form, gender, tense, person, number)
                )

                # Reset inflected variables
                form = tense = gender = number = person = None

        # Entry
        if elem.tag == "entry":

            # Add entry to list
            entries.append(Entry(lemma, pos, compound, inflections))

            # Reset entry variables
            lemma = pos = None
            inflections = []

    # Resulting dictionary
    dictionary = Dict(entries)

    return dictionary
