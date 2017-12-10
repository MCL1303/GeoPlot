#! /usr/bin/env python3

from PIL import Image, ImageDraw, ImageColor, ImageFont
import sys
import os
import json

from geometry import *


def main():
    model = json.load(sys.stdin)
    for k, v in model.items():
        try:
            cls = classes()[k]
            for item in v:
                cls.load(item)
        except KeyError:
            raise TypeError("Error: Unknown object name '" + k + "'!")

    HEIGHT = 1024
    WIDTH = 1024
    POINT_SIZE = 2

    FONT_SIZE = 30
    if not sys.platform.startswith("win32"):
        font_destination = os.path.join(
            "usr", "share", "fonts",
            "truetype", "freefont", "FreeMono.ttf"
        )
    else:
        font_destination = 'arial.ttf'
    FONT = ImageFont.truetype(font_destination, FONT_SIZE)

    out = Image.new('RGB', (HEIGHT, WIDTH), color=(255, 255, 255))
    d = ImageDraw.Draw(out)

    d.height = HEIGHT
    d.textFont = FONT
    d.fontSize = FONT_SIZE
    d.width = WIDTH
    draw_all(d)

    out.save(sys.stdout.buffer, 'PNG')


if __name__ == '__main__':
    main()
