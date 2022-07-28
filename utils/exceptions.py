#-*- coding: utf-8 -*-

class WordNotInDictionaryError(Exception):
    pass

class InvalidConfigKeyError(Exception):
    pass

class MissingUpdateScriptError(Exception):
    pass
