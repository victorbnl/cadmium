import os
import yaml

# Hardcoded for now as this bot is used on only one server for the moment and it's french
# Meant to be edited and set dynamically if the bot grows
lang = "fr"

with open(os.path.join(os.path.dirname(__file__), f"strings/{lang}.yml")) as file_:
    strings = yaml.safe_load(file_)

def i18n(string, vars={}):

    def get(keys, dict_=strings):
        if "." in keys:
            key, rest = keys.split(".", 1)
            return get(rest, dict_[key])
        else:
            return dict_[keys]

    return get(string).format_map(vars)
