import xml.etree.ElementTree as ET
import sys

tree = ET.parse(sys.argv[1])

# print("Normalizing file", sys.argv[1])
doc = tree.getroot().find("document")
if doc is None:
    tree._setroot(ET.Element("facts"))
else:
    tree._setroot(doc.find("facts"))

    for i in tree.getroot():
        attribs = [(j.tag, j.get("val")) for j in i]
        i.clear()
        for k, j in attribs:
            i.set(k, j)

tree.write(sys.argv[2], 'unicode', True)
# print("Normalized file", sys.argv[1])
# print()
