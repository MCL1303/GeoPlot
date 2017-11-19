from ._geomobj import _geomobj
import random

random.seed(23142351)


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

    @classmethod
    def static_as_json(cls):
        return list(i[1] for i in sorted(cls.instances.items()))

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
        coords = random.random(), random.random()
        while coords in Point.instances.values():
            coords = random.random(), random.random()
        self.x, self.y = coords
        if self.name is None:
            self.name = next(Point.namesGenerator)
            self.instances[self.name] = self
