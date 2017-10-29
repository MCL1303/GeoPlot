#! /usr/bin/env python3

from xml.dom import minidom
import sys
import json
import re
from random import uniform

MAX_Y = 10
MAX_X = 20

class Point:
    def namesGeneratorFactory(letters=None, start=10):
        if letters is None:
            letters = ['F']
        for letter in letters:
            i = start
            while True:
                yield letter + str(i)
                i += 1

    namesGenerator = namesGeneratorFactory()
    instances = {}

    @staticmethod
    def add(name):
        if name in Point.instances:
            return Point.instances[name]
        coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        while coords in Point.instances.values():
            coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        Point.instances[name] = coords
        return Point.instances[name]

    @staticmethod
    def load(node):
        try:
            name = node.attributes["Name"].value
        except KeyError:
            name = next(Point.namesGenerator)
        if name in Point.instances:
            return
        Point.add(name)


class Segment:
    def namesGeneratorFactory(
        first_end_letters=None,
        second_end_letters=None,
        start=10):
        if first_end_letters is None:
            first_end_letters = ['F']
        if second_end_letters is None:
            second_end_letters = first_end_letters
        for first_end in Point.namesGeneratorFactory(
            first_end_letters,
            start):
            for second_end in Point.namesGeneratorFactory(
                    second_end_letters,
                    start):
                if first_end + second_end in Segment.instances or\
                    second_end + first_end in Segment.instances:
                    continue
                yield first_end, second_end

    namesGenerator = namesGeneratorFactory()
    instances = {}

    @staticmethod
    def add(both_ends, first_end, second_end):
        if both_ends in Segment.instances:
            return Segment.instances[both_ends]
        a, b = Point.add(first_end), Point.add(second_end)
        Segment.instances[both_ends] = {
            first_end: a,
            second_end: b
        }

    @staticmethod
    def load(node):
        try:
            both_ends = node.attributes["EndPoints"].value
        except KeyError:
            both_ends = next(Segment.namesGenerator)
        ends = re.match(
            '([A-Z][0-9]*)([A-Z][0-9]*)', both_ends
        ).group(1, 2)
        # TODO: get Length
        both_ends = ''.join(sorted(ends)) # C1C2 same as C2C1
        Segment.add(both_ends, *ends)


def main():
    doc = minidom.parse(sys.stdin.buffer)
    for node in doc.documentElement.childNodes:
        if node.nodeType == node.TEXT_NODE:
            continue
        elif node.tagName == "Point":
            Point.load(node)
        elif node.tagName == "Segment":
            Segment.load(node)
    json.dump(
        {
            "Points": Point.instances,
            "Segment": Segment.instances
        },
        sys.stdout,
        indent=4
    )


if __name__ == '__main__':
    main()
