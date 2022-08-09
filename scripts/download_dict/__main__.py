from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

from cadmium.inflect import dictionary

from scripts.download_dict.xml import xml_to_dict


def download():
    """Download dictionary into db"""

    # Message
    print("Downloading and parsing the dictionary. This may take some time...")

    # Download XML file
    url = "http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/dela-fr-public-u8-xml.zip"
    resp = urlopen(url)
    zipfile = ZipFile(BytesIO(resp.read()), "r")
    xmlfile = BytesIO(zipfile.open("dela-fr-public-u8.dic.xml").read())

    # Parse it
    dictObject = xml_to_dict(xmlfile)

    # Populate database
    with dictionary.db.atomic():
        # Add entries
        for entry in dictObject.entries:
            entry_id = dictionary.Entry.add(entry.lemma, entry.pos)
            # Add inflections
            for inflection in entry.inflections:
                dictionary.Inflection.create(
                    entry_id=entry_id,
                    form=inflection.form,
                    gender=inflection.gender or "a",
                    number=inflection.number,
                )


if __name__ == "__main__":
    download()
