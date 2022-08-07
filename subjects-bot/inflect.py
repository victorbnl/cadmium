"""French inflection engine, makes adjectives agree with nouns."""

from lxml import etree

from exceptions import WordNotInDictionaryError

class Inflect():
    """French inflection engine."""

    def __init__(self):
        self.dictionary = []

        context = etree.iterparse("dict.xml", events=("end",), encoding="utf-8")

        entry = {}
        pos = ""
        for _, elem in context:

            if elem.tag == "pos":
                pos = elem.get("name")

            if pos in ("noun", "adj", "verb"):

                if elem.tag == "form":
                    form = elem.text

                if elem.tag == "feat":

                    if elem.get("name") == "tense":
                        tense = elem.get("value")

                    elif elem.get("name") == "gender":
                        gender = elem.get("value")[0]
                    
                    elif elem.get("name") == "number":
                        number = elem.get("value")[0]

                if elem.tag == "inflected":
                    if pos in ("noun", "adj") or (pos == "verb" and tense == "ppast"):
                        entry[f"{gender}{number}"] = form

                if elem.tag == "entry":
                    self.dictionary.append(entry)
                    entry = {}

    def get_word_attrs(self, word):
        """Get noun gender and number."""

        for entry in self.dictionary:
            for form in entry:
                if entry[form] == word:
                    return form
        raise WordNotInDictionaryError


    def inflect_word(self, word, form):
        """Get adjective in a specific form."""

        for entry in self.dictionary:
            for form_ in entry:
                if entry[form_] == word:
                    return entry[form]
        raise WordNotInDictionaryError

if __name__ == "__main__":
    inflect = Inflect()
    # print(inflect.get_word_attrs("maison"))
