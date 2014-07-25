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
#  solver.append = bft.BruteForceTravelingSalesmanSolver()
  solver.append = atd.AntTotalDistanceSolver()
  solver[-1].REMOVE_LINE_CROSSES=False
  solver.append = atd.AntTotalDistanceSolver()
  solver.append = loe.LineOverlapEliminatorTravelingSalesmanSolver()
  solver.append = gts.GravitationalTravelingSalesmanSolver()
  solver.append = gts.GravitationalTravelingSalesmanSolver()
  solver.append = dts.DijkstraSolver()

minPoints = 15
maxPoints = 200
pointInterval = 5
cords = []

for points in xrange(minPoints,maxPoints,pointInterval):
    for point in xrange(points):
        works = False
        while(works == False):
            xvalue = random.randrange(1,500)
            yvalue = random.randrange(1,500)
            works = True
            for checkpoint in range(len(cords)):
                if (cords.x - a)**2+ (cords.y - b)**2 <= 16):
                    works = false
        xvalues.append(random.randrange(1,500,1))
        yvalues.append(random.randrange(1,500,1))
        solver.loadCoordinatesFromXYArrays(xvalues,yvalues)
if __name__ == '__main__':
    main()


