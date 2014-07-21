#-------------------------------------------------------------------------------
# Name:        Traveling Salesman Canvas
# Purpose:     Takes data from the JQuery canvas, processes it, and returns it to the user
#
# Author:      Martin Schneider
#
# Created:     07/09/2014
# Copyright:   (c) Martin 2014
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
  algorithm = "Dijkstra 2"

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
  for k in xrange(1,2000):
      print k
      timer = 0
      for j in xrange(10):
        if solver is None:
          print "ERROR: Invalid solver!"
        else:
          solver.cords = []
          xvalues = []
          yvalues = []
          for i in xrange(k):
              xvalues.append(random.randrange(1,500,1))
              yvalues.append(random.randrange(1,500,1))
          solver.loadCoordinatesFromXYArrays(xvalues,yvalues)
          timenow = time.time()
          solution =solver.solve()
          timer -= timenow - time.time()
      times.append(timer/10)
      print times[-1]
  print times

if __name__ == '__main__':
    main()


