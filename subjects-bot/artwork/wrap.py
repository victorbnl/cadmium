"""Wraps the subject into two lines if it's too wide."""

from artwork.utils import *

def subject_lines(subject, size, first_line_max_width, second_line_max_width):
    """Wrap a subject into two lines if needed."""

    nsize = 0.8 * size
    
    width = get_line_dimensions(subject, size)[0]

    if (width > first_line_max_width):
        first_line = subject.split(" ")
        second_line = []

        first_line_width = width
        second_line_width = 0

        while first_line_width > first_line_max_width and second_line_width < second_line_max_width:

            second_line.append(first_line.pop(0))

            first_line_width = get_line_dimensions(" ".join(first_line), nsize)[0]
            second_line_width = get_line_dimensions(" ".join(second_line), nsize)[0]
    
        return [{ "content": " ".join(l), "size": nsize } for l in [first_line, second_line]]
    
    else:
        return [{ "content": subject, "size": size }]
