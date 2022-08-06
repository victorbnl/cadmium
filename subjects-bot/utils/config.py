"""Utilities for accessing and setting config parameters."""

import yaml
from functools import reduce

from exceptions import *

with open("data/config.yml", "r") as file_:
    config = yaml.safe_load(file_) or {}

def get_config():
    return config

def get(keys, dict_=config):
    """Get config item"""

    if "." in keys:
        key, rest = keys.split(".", 1)
        return get(rest, dict_[key])
    else:
        return dict_[keys]

def set(keys, item, dict_=config):
    """Set config item"""

    if "." in keys:
        key, rest = keys.split(".", 1)
        if key not in dict_:
            raise InvalidConfigKeyError
        set(rest, item, dict_[key])
    else:
        if keys not in dict_:
            raise InvalidConfigKeyError
        else:
            dict_[keys] = item

    with open("data/config.yml", "w") as file_:
        file_.write(yaml.dump(config, allow_unicode=True))
