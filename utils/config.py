#-*- coding: utf-8 -*-

import yaml

with open("data/config.yml", "r") as file_:
    config = yaml.safe_load(file_)

def get(key):
    """Get config item"""

    return config[key]

def set(key, value):
    """Set config item"""

    config[key] = value

    with open("data/config.yml", "w") as file_:
        file_.write(yaml.dump(config, allow_unicode=True))
