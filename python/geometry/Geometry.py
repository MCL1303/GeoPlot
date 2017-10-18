from random import random

class Geomerty:
    points = {}
    segments = set()

    @staticmethod
    def addpoints(*points):
        for i in points:
            if type(i) == str:
                points.setdefault(i, (random(), random()))

    @staticmethod
    def addsegment(segment):
        Geomerty.addpoints(segment.start, segment.end)
        segments.add(segment)
