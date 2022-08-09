from cadmium.utils import config
from cadmium import subject
from cadmium import inflect
from cadmium import artwork


def get_subject():
    """Returns the final form of the subject: a banner image."""

    # Get message
    message = config.get("message")

    # Get subject object
    todays_subject = subject.get_subject()

    # Inflections
    todays_subject = inflect.inflect_subject(todays_subject)

    # Format it
    todays_subject = todays_subject.to_string()

    # Generate artwork
    image = artwork.subject_banner(message, todays_subject)

    return image
