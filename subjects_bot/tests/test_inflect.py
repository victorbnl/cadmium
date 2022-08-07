from inflect import Inflect
from exceptions import *

inflect = Inflect()


def test_attrs_ms():
    assert inflect.get_word_attrs("garage") == "ms"


def test_attrs_mp():
    assert inflect.get_word_attrs("cadeaux") == "mp"


def test_attrs_fs():
    assert inflect.get_word_attrs("voiture") == "fs"


def test_attrs_fp():
    assert inflect.get_word_attrs("vidéos") == "fp"


def test_attrs_uk():
    try:
        inflect.get_word_attrs("squfhzq")
    except WordNotInDictionaryError:
        assert True


def test_adj_ms_ms():
    assert inflect.inflect_word("sacré", "ms") == "sacré"


def test_adj_ms_mp():
    assert inflect.inflect_word("forestier", "mp") == "forestiers"


def test_adj_ms_fs():
    assert inflect.inflect_word("creux", "fs") == "creuse"


def test_adj_ms_fp():
    assert inflect.inflect_word("abandonné", "fp") == "abandonnées"


def test_adj_mp_ms():
    assert inflect.inflect_word("festifs", "ms") == "festif"


def test_adj_mp_mp():
    assert inflect.inflect_word("robotiques", "mp") == "robotiques"


def test_adj_mp_fs():
    assert inflect.inflect_word("minéraux", "fs") == "minérale"


def test_adj_mp_fp():
    assert inflect.inflect_word("neigeux", "fp") == "neigeuses"


def test_adj_fs_ms():
    assert inflect.inflect_word("motorisée", "ms") == "motorisé"


def test_adj_fs_mp():
    assert inflect.inflect_word("abyssale", "mp") == "abyssaux"


def test_adj_fs_fs():
    assert inflect.inflect_word("sombre", "fs") == "sombre"


def test_adj_fs_fp():
    assert inflect.inflect_word("grande", "fp") == "grandes"


def test_adj_fp_ms():
    assert inflect.inflect_word("mystérieuses", "ms") == "mystérieux"


def test_adj_fp_mp():
    assert inflect.inflect_word("tortueuses", "mp") == "tortueux"


def test_adj_fp_fs():
    assert inflect.inflect_word("soyeuses", "fs") == "soyeuse"


def test_adj_fp_fp():
    assert inflect.inflect_word("féeriques", "fp") == "féeriques"


def test_adj_uk_ms():
    try:
        inflect.inflect_word("qefsd", "ms")
    except WordNotInDictionaryError:
        assert True


def test_adj_uk_mp():
    try:
        inflect.inflect_word("fhdfqdf", "mp")
    except WordNotInDictionaryError:
        assert True


def test_adj_uk_fs():
    try:
        inflect.inflect_word("dyhfgpj", "fs")
    except WordNotInDictionaryError:
        assert True


def test_adj_uk_fp():
    try:
        inflect.inflect_word("opfisj", "fp")
    except WordNotInDictionaryError:
        assert True
