from PIL import ImageDraw

from cadmium.artwork.utils import *


class Write:
    def __init__(self, image):
        self.draw = ImageDraw.Draw(image)

    def write_lines(self, lines, x, start_y, color):
        """Write multiple lines of text at x starting from start_y."""

        current_y = start_y
        for line in lines:

            # Calculate font size according to scale
            font_size = int(147 * line.size)
            fl_font_size = int(1.5 * font_size)

            # Get font objects
            fl_font, font = get_fonts(line.size)

            # Get first letter size
            fl_width, fl_height = get_text_dimensions(line.content[0], fl_font)

            # Move up by the line height
            current_y -= fl_height

            # Draw first letter of the line
            self.draw.text((x, current_y), line.content[0], color, fl_font)

            # Draw the rest of the content
            self.draw.text(
                (x + fl_width, current_y + (fl_font_size - font_size)),
                line.content[1:],
                color,
                font,
            )

            # Move up for gap between lines
            current_y += -10
