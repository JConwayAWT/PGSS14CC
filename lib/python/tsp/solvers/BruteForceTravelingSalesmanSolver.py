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

class BruteForceTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  bestOrder=[]
  bestDistance=float("inf")
  CALCS_DONE=0
  CALCULATIONS=0
  CALCULATION_UPDATES=100000

  def solve(self):
    # I dont understand what the actual running time is... for some reason it isn't N!
    # This isn't perfect:
    self.CALCULATIONS=math.sqrt(len(self.cords))*math.factorial(len(self.cords))


    self.bestDistance=float("inf")
    self.compute(0, 0, -1, []);
    self.getAnswer()
    return self.answer;

  def getAnswer(self):
    self.answer=";"
    for c in self.bestOrder:
      self.answer+=str(c.i)+","
    self.answer+="0"

  def compute(self,traversed, totalDistance, srcNum, order):

    self.CALCS_DONE+=1
    if self.CALCS_DONE%self.CALCULATION_UPDATES==0:
      pDone=float(self.CALCS_DONE)/self.CALCULATIONS
      self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))

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

