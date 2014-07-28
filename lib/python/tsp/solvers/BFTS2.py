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
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate
import math
import itertools
import TravelingSalesmanSolver

class BFTS2 (TravelingSalesmanSolver.TravelingSalesmanSolver):
  def __init__(self,params):
     self.initSolver(params)
     self.initOverlapSolver()
     self.CALCS_DONE=0
     self.CALCULATIONS=0
     self.CALCULATION_UPDATES=100000

  def solve(self):
    self.CALCULATIONS=math.factorial(len(self.cords))
    perms = itertools.permutations(range(len(self.cords)),len(self.cords))
    bestOrder=None
    bestDistance=float("inf")

    for p in perms:
        self.CALCS_DONE+=1
        if self.CALCS_DONE%self.CALCULATION_UPDATES==0:
            pDone=float(self.CALCS_DONE)/self.CALCULATIONS
            self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
        d=0
        pr=p[-1]
        for n in p:
            d+=self.cdists[n][pr]
            pr=n
        if d<bestDistance:
            bestOrder = p
            bestDistance = d

    self.answer=";"
    for c in bestOrder:
      self.answer+=str(c)+","
    self.answer+="0"
    return self.answer;


