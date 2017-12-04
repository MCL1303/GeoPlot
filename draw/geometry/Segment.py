from ._geomobj import _geomobj
from .Point import Point


class Segment(_geomobj):
    def __init__(self, ends):
        self.ends = ends

    instances = {}

    @staticmethod
    def load(dictionary):
        return Segment.add((
            Point.load(dictionary["first_end"]),
            Point.load(dictionary["second_end"])
        ))

    def render(self, d):
        self.ends[0].draw(d)
        self.ends[0].draw(d)
        d.line(
            (
                self.ends[0].x, self.ends[0].y,
                self.ends[1].x, self.ends[1].y
            ), (0, 0, 0), 3
        )
