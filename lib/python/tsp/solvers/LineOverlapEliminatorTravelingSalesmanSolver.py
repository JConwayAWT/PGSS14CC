#-------------------------------------------------------------------------------
# Name:        Brute Force Traveling Salesman Solver
# Purpose:     Traveling salesman brute force solver
#
# Author:      Martin Schneider
#
# Created:     07/09/2014
# Copyright:   (c) Martin 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import Coordinate
import math
import TravelingSalesmanSolver
import Line
import random

class LineOverlapEliminatorTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):
  def calculateIntersects(self):
    return 
    self.intersecting= [[ [] for i in range(0,len(self.cords))] for i in range(0,len(self.cords))]
    for i in range(0,len(self.cords)):
      for x in range(i+1,len(self.cords)):
        for a in range(i+1,len(self.cords)):
          if a == x or a == i:
            continue
          for b in range(a+1,len(self.cords)):
            if b == x or b == i:
              continue
            if Line.linesIntersect(self.cords[i],self.cords[x],self.cords[a],self.cords[b]):
              self.intersecting[i][x].append((a,b))
              self.intersecting[a][b].append((i,x))
              #print "<BR> Intersect",i,x,a,b
  