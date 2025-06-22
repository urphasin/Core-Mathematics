from shapely.geometry import Point, LineString, Polygon
from math import sqrt, acos, degrees

class Geometry:
  class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y

def distance(p1, p2):
  return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)  

