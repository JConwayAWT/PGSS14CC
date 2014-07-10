#-------------------------------------------------------------------------------
# Name:        AntSolver
# Purpose:     Implement an ant pheremone solver
#
# Author:      Ishan Levy
#
# Created:     07/09/2014
# Copyright:   (c) Ishan Levy 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)
import Coordinate
import math
import random
import TravelingSalesmanSolver
import copy

class AntSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  def solve(self):
    numpoints = len(self.cords)
    path = [0]
    prob = [[1] * numpoints] * numpoints
    while len(path)<len(prob):
        path.append(self.probability(copy.copy(prob),path[-1],path))
    return path

  def probability(self,prob,coordinate,path):
    for i in path:
        prob[coordinate][i] = 0
    total = sum(prob[coordinate])
    normalizedProb = [float(i)/total for i in prob[coordinate]]
    rand = random.random()
    location = 0
    while rand > 0:
        rand -= normalizedProb[location]
        location +=1
    location -=1
    return location

ant = AntSolver()
ant.cords.append(Coordinate.Coordinate(400,100))
ant.cords.append(Coordinate.Coordinate(300,100))
ant.cords.append(Coordinate.Coordinate(200,100))
ant.cords.append(Coordinate.Coordinate(100,100))
ant.cords.append(Coordinate.Coordinate(100,200))
ant.cords.append(Coordinate.Coordinate(100,300))
ant.cords.append(Coordinate.Coordinate(100,400))
ant.cords.append(Coordinate.Coordinate(200,400))
ant.cords.append(Coordinate.Coordinate(300,400))
ant.cords.append(Coordinate.Coordinate(400,400))
ant.cords.append(Coordinate.Coordinate(400,300))
ant.cords.append(Coordinate.Coordinate(400,200))
print ant.solve()