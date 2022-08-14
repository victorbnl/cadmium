"""I18n class."""

from dataclasses import dataclass
from typing import Dict

@dataclass
class I18n():

    strings: Dict[str, str]

    def get(self, string, vars={}):
        """Get i18n string."""

        def reach(keys, dict_=self.strings):
            if "." in keys:
                key, rest = keys.split(".", 1)
                return reach(rest, dict_[key])
            else:
                return dict_[keys]

        return reach(string).format_map(vars)
