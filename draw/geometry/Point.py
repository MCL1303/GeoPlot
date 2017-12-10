from ._geomobj import _geomobj


class Point(_geomobj):
    POINT_SIZE = 2

    instances = {}

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    @staticmethod
    def load(dictionary):
        return Point.add(dictionary["name"], dictionary["x"], dictionary["y"])

    def render(self, d):
        self.x *= d.width
        self.y *= d.height

        d.arc(
            (self.x - self.POINT_SIZE, self.y - self.POINT_SIZE,
                self.x + self.POINT_SIZE, self.y + self.POINT_SIZE),
            0, 360, (0, 0, 0)
        )
        d.text(
            (self.x - d.fontSize / 2,
            self.y - d.fontSize / 2),
            self.name, (0, 0, 0), d.textFont
        )
