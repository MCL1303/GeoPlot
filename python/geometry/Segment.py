import Geometry
import re

class Segment:
  def __init__(self, el):
    self.start, self.end = re.match('(' + Geometry.Point.regex + ')(' + Geometry.Point.regex + ')', el.find('Names').get('val')).group(1, 2)
    self.length = float(el.find('Length').get('val'))
    
