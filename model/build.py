#! /usr/bin/env python3

from xml.dom import minidom
import sys
import json
import re

from geometry import *


def main():
    doc = minidom.parse(sys.stdin.buffer)
    for node in doc.documentElement.childNodes:
        if node.nodeType == node.TEXT_NODE:
            continue
        try:
            classes()[node.tagName].load(node)
        except KeyError:
            raise TypeError("Error: Unknown tag '" + node.tagName + "'!")
    resolve_all()
    json.dump(
        { k: list(v.instances.values()) for k, v in classes().items() if v.instances },
        sys.stdout,
        default=lambda o: as_json(o),
        indent=4
    )


if __name__ == '__main__':
    main()
