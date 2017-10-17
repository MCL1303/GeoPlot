import sys

'''
sys.argv[1] -- xml file to plot
sys.argv[2] (optional) -- name of png file to write (default $(basename sys.argv[1]).png)
'''

import xml.etree.ElementTree as ET
facts = ET.parse(sys.argv[1]).getroot().find('document').find('facts')

from geometry import *

for i in facts:
    print(i.tag, end="")
    for j in i:
        print(globals()[i.tag](i))
    print()

print(Geometry.points)

#from PIL import Image, ImageDraw

#out = Image.new()
#d = ImageDraw.Draw(out)

#d.point(Geometry.points.itervalues())
