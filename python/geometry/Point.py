import Geometry
import re

class Point:
    def __init__(self, el):
        self.name = el.find('Name').get('val')
        Geometry.addpoints(self)

    regex = '[A-Z][0-9]*'
