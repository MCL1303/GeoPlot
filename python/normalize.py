import xml.etree.ElementTree as ET
import sys
from os.path import basename as bn, splitext as sp, dirname as dn, realpath as rp, join

tree = ET.parse(sys.argv[1])

tree._setroot(tree.getroot().find("document").find("facts"))

for i in tree.getroot():
    attribs = [(j.tag, j.get("val")) for j in i]
    i.clear()
    for k, j in attribs:
        i.set(k, j)

tree.write(sys.argv[2], 'unicode', True)
