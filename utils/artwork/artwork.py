from io import BytesIO
from PIL import Image, ImageDraw

from utils.artwork.utils import *


def draw_lines(lines, x, start_y, color):

    current_y = start_y
    for line in lines:

        font_size = int(147 * line["size"])
        fl_font_size = int(1.5 * font_size)

        fl_font, font = get_fonts(line["size"])

        fl_width, fl_height = get_text_dimensions(line["content"][0], fl_font)

        current_y -= fl_height

        draw.text((x, current_y), line["content"][0], color, fl_font)

        draw.text(
            (x + fl_width, current_y + (fl_font_size - font_size)),
            line["content"][1:],
            color,
            font,
        )

        current_y += -10


def subject_to_artwork(subject):
    """Generate artwork from subject"""

    global draw

    message = "Le sujet du jour est"

    subject = subject.title()

    im = Image.open("assets/img/background.jpg")
    width, height = im.size

    draw = ImageDraw.Draw(im)

    color = (239, 158, 30)
    x = width * 0.104
    start_y = height - 0.25 * height

    lines = []

    for subject_line in subject_lines(subject, 1, 1500, 1000):
        lines.append(subject_line)

    lines.append({"content": message, "size": 0.4})

    draw_lines(lines, x, start_y, color)

    image = BytesIO()
    im.save(image, "PNG")
    image.seek(0)

    return image
