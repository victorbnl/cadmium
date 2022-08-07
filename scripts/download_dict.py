from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

url = "http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/dela-fr-public-u8-xml.zip"

resp = urlopen(url)

zipfile = ZipFile(BytesIO(resp.read()), 'r')

with open("dict.xml", "wb") as file_:
    file_.write(zipfile.open("dela-fr-public-u8.dic.xml").read())
