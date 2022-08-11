import os

import yaml


class I18n():

    def __init__(self):

        # Hardcoded for now as this bot is used on only one server for the
        # moment and it's french
        # Meant to be edited and set dynamically if the bot grows
        self.lang = "fr"

        # Get strings
        with open(
            os.path.join(os.path.dirname(__file__), f"strings/{self.lang}.yml")
        ) as file_:
            self.strings = yaml.safe_load(file_)

    def i18n(self, string, vars={}):
        """Get i18n string."""

        def get(keys, dict_=self.strings):
            if "." in keys:
                key, rest = keys.split(".", 1)
                return get(rest, dict_[key])
            else:
                return dict_[keys]

        return get(string).format_map(vars)


_inst = I18n()
i18n = _inst.i18n
