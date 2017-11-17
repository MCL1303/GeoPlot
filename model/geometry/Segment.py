from ._geomobj import _geomobj
from .Point import Point
import re

class Segment(_geomobj):
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

    def as_json(self):
        ends = list(self.ends)
        return {
            "first_end": ends[0],
            "second_end": ends[1]
        }

    def proceed(self):
        for i in self.ends:
            i.resolve_one()

    def update(self, length):
        # TODO: implement
        pass
