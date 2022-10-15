"""Load i18n strings from file."""

from os import path

import yaml

from cadmium.i18n.classes import I18n


def load(lang: str):
    """Load lang strings into I18n object."""

    file_path = f'strings/{lang}.yml'

    with open(path.join(path.dirname(__file__), file_path), 'r') as file_:
        strings = yaml.safe_load(file_)

    return I18n(strings)
