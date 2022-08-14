import pytest

from cadmium import inflect


@pytest.mark.parametrize('word, expected_gender, expected_number', [
    ("jardin", 'masculine', 'singular'),
    ("voiture", 'feminine', 'singular'),
    ("lampadaires", 'masculine', 'plural'),
    ("maisons", 'feminine', 'plural')
])
def test_get_inflection(word, expected_gender, expected_number):

    inf = inflect.get_inflection(word)
    gender = inf['gender']
    number = inf['number']

    assert (
        gender == expected_gender
        and number == expected_number
    )


@pytest.mark.parametrize('adjective, gender, number, expected_adjective', [

    ("grand", 'masculine', 'singular', "grand"),
    ("grand", 'masculine', 'plural', "grands"),
    ("grand", 'feminine', 'singular', "grande"),
    ("grand", 'feminine', 'plural', "grandes"),

    ("grands", 'masculine', 'singular', "grand"),
    ("grands", 'masculine', 'plural', "grands"),
    ("grands", 'feminine', 'singular', "grande"),
    ("grands", 'feminine', 'plural', "grandes"),

    ("grande", 'masculine', 'singular', "grand"),
    ("grande", 'masculine', 'plural', "grands"),
    ("grande", 'feminine', 'singular', "grande"),
    ("grande", 'feminine', 'plural', "grandes"),

    ("grandes", 'masculine', 'singular', "grand"),
    ("grandes", 'masculine', 'plural', "grands"),
    ("grandes", 'feminine', 'singular', "grande"),
    ("grandes", 'feminine', 'plural', "grandes"),

])
def test_inflect_adjective(adjective, gender, number, expected_adjective):

    inflected_adjective = inflect.inflect_adjective(adjective, gender, number)

    assert inflected_adjective == expected_adjective
