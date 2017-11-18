#! /usr/bin/env python3

from PIL import Image, ImageDraw, ImageColor, ImageFont
import sys
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
	FONT = ImageFont.truetype('arial.ttf', 20)

	out = Image.new('RGB', (HEIGHT, WIDTH), color=(255, 255, 255))
	d = ImageDraw.Draw(out)

	d.height = HEIGHT
	d.textFont = FONT
	d.width = WIDTH
	draw_all(d)

	out.save(sys.stdout.buffer, 'PNG')


if __name__ == '__main__':
	main()
