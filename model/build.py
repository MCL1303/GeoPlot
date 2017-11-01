#! /usr/bin/env python3

from xml.dom import minidom
import sys
import json
import re
from random import uniform

MAX_Y = 10
MAX_X = 20


def as_json(obj):
    if type(obj) == frozenset:
        return list(obj)
    a = obj.__dict__.copy()
    del a['unnamed_instances']
    for k in list(a.keys()):
        if k.startswith('_'):
            del a[k]
    return a


class __geomobj:
    @classmethod
    def add(cls, identifier=None, *args):
        if identifier is not None:
            if identifier in cls.instances:
                return cls.instances[identifier].update(*args)
            else:
                obj = cls(identifier, *args)
                cls.instances[identifier] = obj
                return obj
        else:
            obj = cls(identifier, *args)
            cls.unnamed_instances.append(obj)
            return obj

    def __init__(self):
        self.__resolved = False

    def update(self):
        pass

    def resolve_one(self):
        if not self.__resolved:
            self.proceed()
            self.__resolved = True

    @classmethod
    def resolve(cls):
        for i in list(cls.instances.values()):
            i.resolve_one()
        for i in cls.unnamed_instances:
            i.resolve_one()

def resolve_all():
    for cls in __geomobj.__subclasses__():
        cls.resolve()

class Point(__geomobj):
    def namesGeneratorFactory(letter='A', start=0):
        i = start
        while True:
            name = letter + str(i)
            if name not in Point.instances:
                yield name
            i += 1

    namesGenerator = namesGeneratorFactory()
    instances = {}
    unnamed_instances = []

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.x, self.y = None, None

    @staticmethod
    def load(node):
        try:
            name = node.attributes["Name"].value
        except KeyError:
            name = None
        Point.add(name)

    def proceed(self):
        coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        while coords in Point.instances.values():
            coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        self.x, self.y = coords
        if self.name is None:
            self.name = next(Point.namesGenerator)
            self.instances[self.name] = self


class Segment(__geomobj):
    instances = {}
    unnamed_instances = []

    def __init__(self, ends):
        super().__init__()
        self.ends = ends

    @staticmethod
    def load(node):
        try:
            a, b = re.match(
                '([A-Z][0-9]*)([A-Z][0-9]*)',
                node.attributes["EndPoints"].value
            ).group(1, 2)
            # TODO: add case then just one end is unknown
        except KeyError:
            a, b = None, None
        Segment.add(frozenset({ Point.add(a), Point.add(b) }))

    def proceed(self):
        for i in self.ends:
            i.resolve_one()

    def update(self, length):
        # TODO: implement
        pass

classes = {
    "Point": Point,
    "Segment": Segment
}


def main():
    doc = minidom.parse(sys.stdin.buffer)
    for node in doc.documentElement.childNodes:
        if node.nodeType == node.TEXT_NODE:
            continue
        try:
            classes[node.tagName].load(node)
        except KeyError:
            raise TypeError("Warning: Unknown tag '" + node.tagName + "'!")
    resolve_all()
    json.dump(
        { k: list(v.instances.values()) for k, v in classes.items() if v.instances },
        sys.stdout,
        default=lambda o: as_json(o),
        indent=4
    )


if __name__ == '__main__':
    main()
