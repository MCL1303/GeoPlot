#! /usr/bin/env python3

from xml.dom import minidom
import sys
import json
import re
from random import uniform

MAX_Y = 10
MAX_X = 20

class __geomobj:
    @classmethod
    def add(cls, name=None, *args):
        if name is not None and name in cls.instances:
            return cls.instances[name]
        return cls(name, *args)

    @classmethod
    def load(cls, node):
        try:
            res = cls.unpack(node)
            if type(res) == tuple or type(res) == list:
                cls.add(*res)
            else:
                cls.add(res)
        except KeyError:
            cls.add()

    def __init__(self, name):
        self.name = name
        if name is not None:
            self.instances[self.name] = self
        else:
            self.instances[None].append(self)
        self.__resolved = False

    def resolve_one(self):
        if not self.__resolved:
            self.proceed()
            self.__resolved = True

    def __lt__(self, other):
        if type(self) != type(other):
            raise TypeError
        return self.name < other.name

    def as_json(self):
        a = self.__dict__.copy()
        for k in list(a.keys()):
            if k.startswith('_'):
                del a[k]
        return a

    @classmethod
    def resolve(cls):
        for k, v in list(cls.instances.items()):
            if k is not None:
                v.resolve_one()
            else:
                for i in v:
                    i.resolve_one()
                    cls.instances[i.name] = i

def resolve_all():
    for cls in __geomobj.__subclasses__():
        cls.resolve()
    for cls in __geomobj.__subclasses__():
        del cls.instances[None]

class Point(__geomobj):
    def namesGeneratorFactory(letter='A', start=0):
        i = start
        while True:
            name = letter + str(i)
            if name not in Point.instances:
                yield name
            i += 1

    namesGenerator = namesGeneratorFactory()
    instances = {
        None: []
    }

    def __init__(self, name):
        super().__init__(name)
        self.x, self.y = None, None

    @staticmethod
    def unpack(node):
        return node.attributes["Name"].value

    def proceed(self):
        coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        while coords in Point.instances.values():
            coords = uniform(0, MAX_X), uniform(0, MAX_Y)
        self.x, self.y = coords
        if self.name is None:
            self.name = next(Point.namesGenerator)

class Segment(__geomobj):
    instances = {
        None: []
    }

    def __init__(self, name, first_end=None, second_end=None):
        super().__init__(name)
        self.ends = list(
            sorted(
                [Point.add(first_end), Point.add(second_end)]
            )
        )

    @staticmethod
    def unpack(node):
        a, b = sorted(re.match(
            '([A-Z][0-9]*)([A-Z][0-9]*)',
            node.attributes["EndPoints"].value
        ).group(1, 2))
        return a + b, a, b

    def proceed(self):
        self.ends[0].resolve_one()
        self.ends[1].resolve_one()
        if self.name is None:
            self.name = self.ends[0].name + self.ends[1].name

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
        default=lambda o: o.as_json(),
        indent=4
    )


if __name__ == '__main__':
    main()
