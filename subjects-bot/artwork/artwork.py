"""Generates a banner for a subject."""

import os
from io import BytesIO
from PIL import Image, ImageDraw

from artwork.utils import *
from artwork.wrap import *


def draw_lines(lines, x, start_y, color):
    """Draw multiple lines of text at x starting from start_y."""

    current_y = start_y
    for line in lines:

        font_size = int(147 * line["size"])
        fl_font_size = int(1.5 * font_size)

        fl_font, font = get_fonts(line["size"])

        fl_width, fl_height = get_text_dimensions(line["content"][0], fl_font)

        # Move up by the line height
        current_y -= fl_height

        # Draw first letter of the line
        draw.text((x, current_y), line["content"][0], color, fl_font)

        # Draw the rest of the content
        draw.text(
            (x + fl_width, current_y + (fl_font_size - font_size)),
            line["content"][1:],
            color,
            font,
        )

        current_y += -10


def subject_banner(message, subject):
    """Generate artwork from subject"""

    global draw

    # Format subject
    subject = subject.title()

    # Get background image to write text on
    path = os.path.join(os.path.dirname(__file__), "assets/img/background.jpg")
    im = Image.open(path)
    width, height = im.size
    # Draw object
    draw = ImageDraw.Draw(im)

    # Set variables
    color = (239, 158, 30)
    x = width * 0.104
    start_y = height - 0.25 * height

    lines = []

    # Cut the subject into two lines if necessary
    for subject_line in subject_lines(subject, 1, 1500, 1000):
        lines.append(subject_line)

    # Add the message line
    lines.append({"content": message, "size": 0.4})

    # Draw the lines
    draw_lines(lines, x, start_y, color)

    # Return the PNG image in a BytesIO
    image = BytesIO()
    im.save(image, "PNG")
    image.seek(0)
    return image
