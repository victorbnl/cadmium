from cadmium import subject, lists, config, artwork
from cadmium.utils import subject_utils


def change_verb_prob(factor):
    """Increment or decrement verbs probabilities."""

    verb_prob = float(config.get('probs_verb'))
    step = float(config.get('probs_verb_step'))

    new_verb_prob = round(verb_prob + factor * step, 1)

    if new_verb_prob < 0:
        new_verb_prob = 0
    elif new_verb_prob > 1:
        new_verb_prob = 1

    config.set('probs_verb', new_verb_prob)


def get_subject():

    # Get the subject
    the_subject = subject.get_subject(
        words=subject.Words(
            noun=lists.noun.items(),
            verb=lists.verb.items(),
            adverb=lists.adverb.items(),
            adjective=lists.adjective.items()
        ),
        probs=subject.Probs(
            verb=config.get('probs_verb'),
            adverb=config.get('probs_adverb'),
            adjective=config.get('probs_adjective'),
            second_adjective=config.get('probs_second_adjective')
        )
    )

    # Change verb prob
    if the_subject.verb and not the_subject.noun:
        change_verb_prob(-1)
    elif the_subject.noun and not the_subject.verb:
        change_verb_prob(+1)

    # Format it
    the_subject = subject_utils.format_subject(the_subject)

    # Generate a banner
    banner = artwork.subject_banner(config.get('message'), the_subject)

    return banner
