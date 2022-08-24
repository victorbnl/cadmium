from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from cadmium.subject.inflect.dictionary import database
from cadmium.subject.inflect.dictionary.download import parse_xml


URL = 'http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/dela-fr-public-u8-xml.zip' # noqa


def download():
    """Download dictionary into db"""

    # Download XML file
    resp = urlopen(URL)
    zipfile = ZipFile(BytesIO(resp.read()), "r")
    xmlfile = BytesIO(zipfile.open("dela-fr-public-u8.dic.xml").read())

    # Parse it
    dictObject = parse_xml.parse(xmlfile)

    # Populate database
    with database.db.atomic():
        # Add entries
        for entry in dictObject.entries:
            entry_id = database.Entry.add(entry.lemma, entry.pos)
            # Add inflections
            for inflection in entry.inflections:
                database.Inflection.create(
                    entry_id=entry_id,
                    form=inflection.form,
                    gender=inflection.gender or "a",
                    number=inflection.number,
                )
