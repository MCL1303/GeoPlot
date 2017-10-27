from xml.dom import minidom
import sys

def main():
    root = minidom.parse(sys.stdin.buffer)
    outroot = minidom.getDOMImplementation().createDocument(None, 'facts', None)
    if root.documentElement.hasChildNodes():
        for node in root.documentElement.firstChild.firstChild.childNodes:
            newnode = outroot.createElement(node.tagName)
            for subnode in node.childNodes:
                newnode.setAttribute(subnode.tagName, subnode.attributes["val"].value)
            outroot.documentElement.appendChild(newnode)

    outroot.writexml(sys.stdout, addindent='  ', newl='\n', encoding="UTF-8")

if __name__ == '__main__':
    main()
