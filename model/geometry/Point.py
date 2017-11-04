from ._geomobj import _geomobj
from random import uniform

MAX_Y = 10
MAX_X = 20

class Point(_geomobj):
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

    def as_json(self):
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y
        }

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
