"""Load configuration into Config object."""

import dataclasses

import yaml

from cadmium.config.classes import Config


CONFIG_FILE = 'data/config.yml'


def load() -> Config:
    """Read config file and returns Config object."""

    try:
        with open(CONFIG_FILE, 'r') as file_:
            config_dict = yaml.safe_load(file_) or {}

    except FileNotFoundError:
        config_dict = {}

    return Config(**config_dict)


def write(config: Config):
    """Write Config object to file."""

    with open(CONFIG_FILE, 'w') as file_:
        file_.write(
            yaml.dump(
                dataclasses.asdict(config),
                allow_unicode=True
            )
        )
