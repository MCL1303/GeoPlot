import Geometry
import re

class Triangle:
  def __init__(self, el):
    self.first, self.second, self.third = re.match('(' + Geometry.Point.regex + ')(' + Geometry.Point.regex + ')(' + Geometry.Point.regex + ')', el.find('Names').get('val')).group(1, 2, 3)
    
