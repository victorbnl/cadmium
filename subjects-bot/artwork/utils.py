"""Utility functions for text drawing."""

import os
from PIL import ImageFont


def get_text_dimensions(text_string, font):
    """Returns the width and height of a text."""
    # https://stackoverflow.com/a/46220683/9263761

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


def get_line_dimensions(content, size):
    """Returns the width and height of a line."""

    fl_font, font = get_fonts(size)
    if content != "":
        width = get_text_dimensions(content[0], fl_font)[0] + (
            get_text_dimensions(content[1:], font)[0] if len(content) > 1 else 0
        )
        height = get_text_dimensions(content[0], fl_font)[1]
    else:
        width, height = 0, 0
    return width, height


def get_font(scale, variant):
    """Get ImageFont font object of desired size."""

    path = os.path.join(
        os.path.dirname(__file__), "assets/fonts/Alegreya/Alegreya-{variant}.ttf"
    )
    font = ImageFont.truetype(path.format(variant=variant), int(147 * scale))

    return font


def get_fonts(scale):
    """Get a first-letter font and a normal font."""
    return (get_font(1.5 * scale, "Regular"), get_font(scale, "Medium"))
