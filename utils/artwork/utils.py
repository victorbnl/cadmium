from PIL import ImageFont

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761

    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def get_font(scale, variant):
    return ImageFont.truetype(
        f"assets/fonts/Alegreya/Alegreya-{variant}.ttf",
        int(147 * scale)
    )

def get_fonts(scale):
    return (get_font(1.5 * scale, "Regular"), get_font(scale, "Medium"))

def get_line_dimensions(content, size):
    fl_font, font = get_fonts(size)
    if content != "":
        width = get_text_dimensions(content[0], fl_font)[0] + (get_text_dimensions(content[1:], font)[0] if len(content) > 1 else 0)
        height = get_text_dimensions(content[0], fl_font)[1]
    else:
        width, height = 0, 0
    return width, height

def subject_lines(subject, size, first_line_max_width, second_line_max_width):

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
