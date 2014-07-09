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

import math
import TravelingSalesmanSolver

class BruteForceTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  bestOrder=[]
  bestDistance=float("inf")

  def solve(self):
    self.bestDistance=float("inf")
    self.compute(0, 0, -1, []);
    self.getAnswer()
    return self.answer;

  def getAnswer(self):
    for c in self.bestOrder:
      self.answer+=str(c.i)+","
      

  def compute(self,traversed, totalDistance, srcNum, order):
    if traversed==(pow(2, len(self.cords))-1):
      totalDistance+=order[len(order)-1].dist(order[0])
      if (totalDistance<self.bestDistance):
        self.bestDistance=totalDistance
        self.bestOrder=order
      return

    src=None
    if (srcNum>=0):
      src=self.cords[srcNum]
    
    farthest=0
    f=-1
    
    for i in range(0,len(self.cords)):
      if (not checkTraversed(traversed, i)):
        dist = 0  if (srcNum == -1) else src.dist(self.cords[i])
        farthest = max(farthest,dist)
        f=i
    
    for i in range(0,len(self.cords)):
      if (not checkTraversed(traversed, i)):
        dist = 0  if (srcNum == -1) else src.dist(self.cords[i])
        o = list(order)
        o.append(self.cords[i])
        self.compute(setTraversed(traversed, i), totalDistance+dist, i, o)


def setTraversed(traversed, n):
  return traversed | 1<<n


def checkTraversed(traversed, n):
  return (traversed & 1<<n)>0

