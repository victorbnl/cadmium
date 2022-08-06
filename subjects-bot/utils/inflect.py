"""Inflection engine, makes adjectives agree with nouns."""

from lxml import etree
import json

from exceptions import WordNotInDictionaryError

dict_ = []

def init():
    """Parse dictionary"""

    global dict_

    context = etree.iterparse("dict.xml", events=("end",), encoding="utf-8")

    entry = {}
    pos = ""
    for _, elem in context:

        if elem.tag == "pos":
            pos = elem.get("name")
        
        if pos in ("noun", "adj"):

            if elem.tag == "form":
                form = elem.text

            if elem.tag == "feat":
                if elem.get("name") == "gender":
                    gender = elem.get("value")[0]
                elif elem.get("name") == "number":
                    number = elem.get("value")[0]
            
            if elem.tag == "inflected":
                entry[f"{gender}{number}"] = form
            
            if elem.tag == "entry":
                dict_.append(entry)
                entry = {}

def get_word_attrs(word):
    """Get noun gender and number"""

    for entry in dict_:
        for form in entry:
            if entry[form] == word:
                return form
    raise WordNotInDictionaryError

def inflect_word(word, form):
    """Get adjective in a specific form"""

    for entry in dict_:
        for form_ in entry:
            if entry[form_] == word:
                return entry[form]
    raise WordNotInDictionaryError

init()
