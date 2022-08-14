import pytest
import delayed_assert

from cadmium import subject
from cadmium.subject.exceptions import EmptyWordListError


tests = [
    ['verb'],
    ['verb', 'adverb'],
    ['noun'],
    ['noun', 'adjective'],
    ['noun', 'adjective', 'second_adjective'],
]


def util_build_probs(test):

    probs = subject.Probs(
        verb=0,
        adverb=0,
        adjective=0,
        second_adjective=0
    )

    for nature in test:
        setattr(probs, nature, 1)

    return probs


@pytest.mark.parametrize('test', tests)
def test_get_subject(test):

    # Build probabilities dictionary
    probs = util_build_probs(test)

    words = subject.Words(
        noun=["maison", "voiture"],
        verb=["regarder", "écouter"],
        adjective=["beau", "merveilleux"],
        adverb=["rapidement", "somptueusement"]
    )

    # Generate subject
    the_subject = subject.get_subject(probs=probs, words=words)

    # Check if subject is a string longer than 0
    delayed_assert.expect(
        isinstance(the_subject, str)
        and len(the_subject) > 0
    )

    # Check if each word is the right nature
    for word in test:

        if word == 'second_adjective':
            word = 'adjective'

        if getattr(the_subject, word) not in getattr(words, word):
            pytest.fail(f"{getattr(the_subject, word)} not in {word} list")


@pytest.mark.parametrize('test', tests)
def test_get_subject_empty_wordlists(test):

    # Build probabilities dictionary
    probs = util_build_probs(test)

    words = subject.Words(
        noun=[],
        verb=[],
        adjective=[],
        adverb=[]
    )

    with pytest.raises(EmptyWordListError):
        subject.get_subject(probs=probs, words=words)
