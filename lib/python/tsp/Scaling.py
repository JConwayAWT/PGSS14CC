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
from solvers import AntSolver as ats

def main():

  minPoints = 5
  maxPoints = 200
  pointInterval = 5
  iteration = 2
  for points in xrange(minPoints,maxPoints,pointInterval):
      print "X",points
      distances = [0,0,0,0,0,0,0,0,0,0,0]
      for iterations in xrange(iteration):
        xvalues = []
        yvalues = []
        for point in xrange(points):
          works = False
          while(works == False):
               xvalue = random.randrange(1,500)
               yvalue = random.randrange(1,500)
               works = True
               for checkpoint in range(len(xvalues)):
                   if ((xvalues[checkpoint] - xvalue)**2 + (yvalues[checkpoint] - yvalue)**2 <= 16):
                        works = False
          xvalues.append(xvalue)
          yvalues.append(yvalue)
          #print xvalues
          #print yvalues


        solver = []
        #solver.append(bft.BruteForceTravelingSalesmanSolver())
        #solver.append(loe.LineOverlapEliminatorTravelingSalesmanSolver())
        #solver.append(gts.GravitationalTravelingSalesmanSolver())
        #solver.append(atd.AntTotalDistanceSolver())
        #solver.append(atd.AntTotalDistanceSolver())
        #solver[-1].REMOVE_LINE_CROSSES=False
        #solver.append(dts.DijkstraSolver())
        #solver.append(dts2.DijkstraTravelingSalesmanSolver())
        #solver.append(ats.AntSolver())
        for solves in xrange(len(solver)):
           solver[solves].loadCoordinatesFromXYArrays(xvalues,yvalues)
           solver[solves].solve()
           distances[solves] += solver[solves].tourDistance()
      for solves in xrange(len(solver)):
        print distances[solves]/iteration
main()