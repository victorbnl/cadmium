from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from cadmium.subject.inflect import dictionary
from cadmium.subject.inflect.download_dictionary import parse_xml


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
