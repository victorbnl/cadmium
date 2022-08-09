from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

from subjects_bot.inflect.dictionary import Dictionary

from scripts.download_dict.xml import xml_to_dict


def download():
    """Download dictionary into db"""

    # Message
    print("Download and parsing the dictionary. This may take some time...")

    # Download XML file
    url = "http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/dela-fr-public-u8-xml.zip"
    resp = urlopen(url)
    zipfile = ZipFile(BytesIO(resp.read()), "r")
    xmlfile = BytesIO(zipfile.open("dela-fr-public-u8.dic.xml").read())

    # Parse it
    dictionary = xml_to_dict(xmlfile)

    # Setup database
    db = Dictionary()
    db.create_tables()

    # Add entries
    for entry in dictionary.entries:
        entry_id = db.add_entry(entry.lemma, entry.pos)

        # Add inflections
        for inflection in entry.inflections:
            db.add_inflection(
                entry_id=entry_id,
                form=inflection.form,
                gender=inflection.gender,
                number=inflection.number,
            )

    # Commit changes
    db.commit()


if __name__ == "__main__":
    download()
