#-------------------------------------------------------------------------------
# Name:        Scaling Measuring Comparison
# Purpose:     Measures how fast certain solutions scale and compares them
#
# Author:      Ishan Levy
#
# Created:     07/21/2014
# Copyright:   (c) Ishan levy 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------

import os, sys
lib_path = os.path.abspath('../helpers')
sys.path.append(lib_path)
import time
import os
import urlparse
import sys
import random
from solvers import TravelingSalesmanSolver
from solvers import BruteForceTravelingSalesmanSolver as bft
from solvers import AntTotalDistanceSolver as atd
from solvers import LineOverlapEliminatorTravelingSalesmanSolver as loe
from solvers import GravitationalTravelingSalesmanSolver as gts
from solvers import DijkstraTravelingSalesmanSolverFinal as dts
from solvers import DijkstraTravelingSalesmanSolverStreamlined as dts2

def main():
  solver = []
#  solver.append(bft.BruteForceTravelingSalesmanSolver())
  solver.append(atd.AntTotalDistanceSolver())
  solver[-1].REMOVE_LINE_CROSSES=False
#  solver.append(atd.AntTotalDistanceSolver())
  solver.append(loe.LineOverlapEliminatorTravelingSalesmanSolver())
  solver.append(gts.GravitationalTravelingSalesmanSolver())
  solver.append(dts.DijkstraSolver())

  minPoints = 25
  maxPoints = 200
  pointInterval = 5
  cords = []
  xvalues = []
  yvalues = []
  for points in xrange(minPoints,maxPoints,pointInterval):
      print points
      for point in xrange(points):
          works = False
          while(works == False):
              xvalue = random.randrange(1,500)
              yvalue = random.randrange(1,500)
              works = True
              for checkpoint in range(len(cords)):
                  if ((cords[checkpoint].x - xvalue)**2 + (cords[checkpoint].y - yvalue)**2 <= 16):
                      works = False
          xvalues.append(xvalue)
          yvalues.append(yvalue)
      print xvalues
      print yvalues
      for solves in solver:
          solves.loadCoordinatesFromXYArrays(xvalues,yvalues)
          timer = time.time()
          solves.solve()
          timer = time.time()-timer
          print timer
main()