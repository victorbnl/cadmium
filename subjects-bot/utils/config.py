"""Utilities for accessing and setting config parameters."""

import yaml

from exceptions import *

# Read config file
with open("data/config.yml", "r") as file_:
    config = yaml.safe_load(file_) or {}


def get_config():
    """Get the full configuration."""
    return config


def get(keys, dict_=config):
    """Get a config item."""

    # Reach the parameter
    if "." in keys:
        key, rest = keys.split(".", 1)
        return get(rest, dict_[key])

    # Get it
    else:
        return dict_[keys]


def set(keys, item, dict_=config):
    """Set a config item."""

    # Reach the parameter
    if "." in keys:
        key, rest = keys.split(".", 1)
        if key not in dict_:
            raise InvalidConfigKeyError
        set(rest, item, dict_[key])

    # Set it
    else:
        if keys not in dict_:
            raise InvalidConfigKeyError
        else:
            dict_[keys] = item

    # Write config
    with open("data/config.yml", "w") as file_:
        file_.write(yaml.dump(config, allow_unicode=True))
