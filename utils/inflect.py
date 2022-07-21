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

def get_word_inf(word):
    """Get word inflection (gender and number)"""

    entry, inflection = find(word)

    return {
        "gender": inflection.find("feat[@name='gender']").get("value"),
        "number": inflection.find("feat[@name='number']").get("value")
    }

def inflect(word, gender, number):
    """Inflect adjective according to given gender and number"""

    entry, _ = find(word)

    for inflection in entry.findall("inflected"):
        inf_gender = inflection.find("feat[@name='gender']").get("value")
        inf_number = inflection.find("feat[@name='number']").get("value")

        if inf_gender == gender and inf_number == number:
            return inflection.find("form").text

if __name__ == "__main__":
    print(inflect("outrecuidant", "feminine", "singular"))
