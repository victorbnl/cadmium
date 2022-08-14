from cadmium import subject, lists, config, subject_utils, artwork


def get_subject():

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

    the_subject = subject_utils.format_subject(the_subject)

    banner = artwork.subject_banner(config.get('message'), the_subject)

    return banner
