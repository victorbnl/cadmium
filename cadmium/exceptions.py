"""The custom exceptions."""

class WordNotInDictionaryError(Exception):
    """Word not found in the inflections dictionnary."""

    pass

class InvalidConfigKeyError(Exception):
    """Key not found in the config."""

    pass

class MissingUpdateScriptError(Exception):
    """Missing update script (update command)."""

    pass
