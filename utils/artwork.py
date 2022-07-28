#!/usr/bin/env python3

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def subject_to_artwork(subject):
    """Generate artwork from subject"""

    message = "Le sujet du jour est".upper()
    subject = subject.upper()

    im = Image.open("assets/background.jpg")
    width, height = im.size

    draw = ImageDraw.Draw(im)
    message_font = ImageFont.truetype("assets/Poppins/Poppins-Regular.ttf", 20)
    subject_font = ImageFont.truetype("assets/Poppins/Poppins-Bold.ttf", 40)

    space = 20

    message_width, message_height = get_text_dimensions(message, message_font)
    subject_width, subject_height = get_text_dimensions(subject, subject_font)

    text_height = message_height + subject_height

    draw.text((width/2-message_width/2, height/2-text_height/2), message, (255, 255, 255), font=message_font)
    draw.text((width/2-subject_width/2, height/2-text_height/2 + message_height), subject, (255, 255, 255), font=subject_font)

    print(f"text_height: {text_height}\nsubject_height: {subject_height}")

    image = BytesIO()
    im.save(image, "JPEG")
    image.seek(0)

    return image
