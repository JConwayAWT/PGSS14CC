#-------------------------------------------------------------------------------
# Name:        Scaling Measuring
# Purpose:     Measures how fast certain solutions scale
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
  algorithm = "Ant Total Distance Remove Line Crosses (n^2)"

  if algorithm =="Brute Force (n!)":
    solver = bft.BruteForceTravelingSalesmanSolver()

  if algorithm =="Ant Total Distance (n^2)":
    solver = atd.AntTotalDistanceSolver()
    solver.REMOVE_LINE_CROSSES=False

  if algorithm =="Ant Total Distance Remove Line Crosses (n^2)":
    solver = atd.AntTotalDistanceSolver()

  if algorithm =="Random Remove Line Crosses (n^2)":
    solver = loe.LineOverlapEliminatorTravelingSalesmanSolver()

  if algorithm =="Gravity":
    solver = gts.GravitationalTravelingSalesmanSolver()

  if algorithm =="Dijkstra":
    solver =dts.DijkstraSolver()

  if algorithm =="Dijkstra 2":
    solver = dts2.DijkstraTravelingSalesmanSolver()

  times = []
  for k in xrange(5,2000,5):
      print k
      timer = 0
      times_to_run = 1
      for j in xrange(times_to_run):
        if solver is None:
          print "ERROR: Invalid solver!"
        else:
          solver.cords = []
          xvalues = []
          yvalues = []
          for i in xrange(k):
            works = False
            while(works == False):
              a = random.randrange(1,500)
              b = random.randrange(1,500)
              works = True
              for c in range(len(solver.cords)):
                if ((solver.cords.x - a)**2+ (solver.cords.y - b)**2 < 16):
                    works = false
            xvalues.append(random.randrange(1,500,1))
            yvalues.append(random.randrange(1,500,1))
          solver.loadCoordinatesFromXYArrays(xvalues,yvalues)
          timenow = time.time()
          solution =solver.solve()
          timer -= timenow - time.time()
      times.append(timer/times_to_run)
      print times[-1]
  print times

if __name__ == '__main__':
    main()


