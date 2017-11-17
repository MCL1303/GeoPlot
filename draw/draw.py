#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageColor, ImageFont
import sys
import json

model = json.load(sys.stdin)
points = model.get("Point", [])

HEIGHT = 1024
WIDTH = 1024
BLUE = (255, 255, 255)
BLACK = (0, 0, 0)
POINT_SIZE = 2
FONT = ImageFont.truetype('arial.ttf', 20)

out = Image.new('RGB', (HEIGHT, WIDTH), color=BLUE)
d = ImageDraw.Draw(out)

for i in points:
	x, y = i["x"] * WIDTH, i["y"] * HEIGHT
	d.arc((x - POINT_SIZE, y - POINT_SIZE, x + POINT_SIZE, y + POINT_SIZE),
		0, 360, BLACK) # d.point((x, y), BLACK)
	d.text((x - 20, y - 20), i["name"], BLACK, FONT)

out.save(sys.stdout.buffer, 'PNG')
