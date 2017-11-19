from ._geomobj import _geomobj
from .Point import Point
import re


class Segment(_geomobj):
    instances = {}
    unnamed_instances = []

    def __init__(self, ends):
        super().__init__()
        self.ends = list(ends)

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
        Segment.add(frozenset({Point.add(a), Point.add(b)}))

    @classmethod
    def static_as_json(cls):
        return list(
            sorted(
                (i.as_json() for i in cls.instances.values()),
                key=lambda x: x["first_end"].name + x["second_end"].name
            )
        )

    def as_json(self):
        return dict(
            zip(
                ["first_end", "second_end"],
                sorted(self.ends, key=lambda x: x.name)
            )
        )

    def proceed(self):
        for i in self.ends:
            i.resolve_one()

    def update(self, length):
        # TODO: implement
        pass
