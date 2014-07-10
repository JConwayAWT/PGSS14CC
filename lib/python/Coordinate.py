#-------------------------------------------------------------------------------
# Name:        Coordinate
# Purpose:     A coordinate
#
# Author:      Martin Schneider
#
# Created:     07/09/2014
# Copyright:   (c) Martin 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------

import math
class Coordinate:
  def __init__(self,x, y,i = 0):
    self.x=float(x)
    self.y=float(y)
    self.i=int(i)
  def dist(self,px, py):
    return math.sqrt(pow(self.px-a.x, 2)+pow(self.py-a.y, 2))
  def dist(self,a):
    return math.sqrt(pow(self.x - a.x, 2) + pow(self.y - a.y, 2))
