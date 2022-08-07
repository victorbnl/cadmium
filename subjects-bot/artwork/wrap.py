"""Wraps the subject into two lines if it's too wide."""

from artwork.utils import *


def subject_lines(subject, size, first_line_max_width, second_line_max_width):
    """Wrap a subject into two lines if needed."""

    # Reduce text size if two lines of subject
    nsize = 0.8 * size

    # Get subject width
    width = get_line_dimensions(subject, size)[0]

    # If subject too large
    if width > first_line_max_width:

        first_line = subject.split(" ")
        second_line = []
        first_line_width = width
        second_line_width = 0

        # While the first line is too large and the second line didn't reach its max width
        while (
            first_line_width > first_line_max_width
            and second_line_width < second_line_max_width
        ):

            # Move the first word of the first line to the second line
            second_line.append(first_line.pop(0))

            # Recalculate widths
            first_line_width = get_line_dimensions(" ".join(first_line), nsize)[0]
            second_line_width = get_line_dimensions(" ".join(second_line), nsize)[0]

        # Return formatted lines with new text size
        return [
            {"content": " ".join(l), "size": nsize} for l in [first_line, second_line]
        ]

    # If subject is not too large
    else:
        # Just return it with its original size
        return [{"content": subject, "size": size}]
