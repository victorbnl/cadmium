"""Generates a banner for a subject."""

import os
from io import BytesIO

from PIL import Image

from cadmium.artwork import wrap
from cadmium.artwork.data.line import Line
from cadmium.artwork.write import Write


def subject_banner(message, subject):
    """Generate artwork from subject"""

    # Format subject
    subject = subject.title()

    # Get background image to write text on
    path = os.path.join(os.path.dirname(__file__), "assets/img/background.jpg")
    im = Image.open(path)
    width, height = im.size

    # Get write object
    write = Write(im)

    # Set variables
    color = (239, 158, 30)
    x = width * 0.104
    start_y = height - 0.25 * height

    lines = []

    # Cut the subject into two lines if necessary
    for subject_line in wrap.subject_lines(subject, 1, 1500, 1000):
        lines.append(subject_line)

    # Add the message line
    lines.append(Line(message, 0.4))

    # Draw the lines
    write.write_lines(lines, x, start_y, color)

    # Return the PNG image in a BytesIO
    output = BytesIO()
    im.save(output, "PNG")
    output.seek(0)
    return output
