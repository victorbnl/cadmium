#-*- coding: utf-8 -*-

from lxml import etree

from utils.exceptions import *

def find(word):
    """Find word in dictionary and get entry and inflection"""

    context = etree.iterparse("inflections.xml", events=("start",))

    for action, elem in context:

        if elem.tag == "entry":
            current_entry = elem
        if elem.tag == "inflected":
            current_inflection = elem

        if elem.tag == "form" and elem.text == word:
            return (current_entry, current_inflection)

    raise WordNotFoundError

def get_inf_prop(inflection, property, default):
    """Get inflection object property"""

    try:
        return inflection.find(f"feat[@name='{property}']").get("value")
    except AttributeError:
        return default

def get_word_inf(word):
    """Get word inflection (gender and number)"""

    entry, inflection = find(word)

    return {
        "gender": get_inf_prop(inflection, "gender", "masculine"),
        "number": get_inf_prop(inflection, "number", "singular")
    }

def inflect(word, gender, number):
    """Inflect adjective according to given gender and number"""

    entry, _ = find(word)

    for inflection in entry.findall("inflected"):
        inf_gender = get_inf_prop(inflection, "gender", "masculine")
        inf_number = get_inf_prop(inflection, "number", "singular")

        if inf_gender == gender and inf_number == number:
            return inflection.find("form").text

if __name__ == "__main__":
    print(inflect("outrecuidant", "feminine", "singular"))
