#!/usr/bin/env python3

from xml.dom import minidom
import sys


def main():
    doc = minidom.parse(sys.stdin.buffer)
    outdoc = minidom.getDOMImplementation().createDocument(None, 'facts', None)
    if doc.documentElement.hasChildNodes():
        for node in (
           doc.documentElement.firstChild
           .firstChild.childNodes):
            newnode = outdoc.createElement(node.tagName)
            for subnode in node.childNodes:
                newnode.setAttribute(
                    subnode.tagName,
                    subnode.attributes["val"].value
                )
            outdoc.documentElement.appendChild(newnode)

    outdoc.writexml(sys.stdout, addindent='  ', newl='\n', encoding="UTF-8")


if __name__ == '__main__':
    main()
