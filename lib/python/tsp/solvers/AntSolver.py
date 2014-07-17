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
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate
import math
import random
import TravelingSalesmanSolver
import copy

class AntSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

# Solve Method

  def solve(self):
    self.REFERENCE_POINTS = 12
    self.ITERATIONS = 4000
    numpoints = len(self.cords)
    self.setupprob()
    print self.prob
    self.run()
    self.path = self.lastrun(copy.deepcopy(self.prob))
    return self.makeoutput(self.path)

# Supplementary Methods

  def makeoutput(self,path):
    pathstring = ""
    for i in self.path:
        pathstring += str(self.path[i])
        pathstring += ","
    return pathstring[:-2]

  def setupprob(self):
    self.prob = [ [1/self.distance(i,j) for i in xrange(len(self.cords))] for j in xrange(len(self.cords))]
    for j in xrange(len(self.cords)):
        total = sum(self.prob[j])
        self.prob[j] = [500*float(i)/total for i in self.prob[j]]

  def run(self):
    for j in xrange(0,self.ITERATIONS):
        path = [0]
        while len(path)<len(self.prob):
            path.append(self.probability(copy.deepcopy(self.prob),path[-1],path))
        for i in xrange(1,len(path)):
            # Method of Production
            distsum = 0
            for k in xrange(int(-math.floor(self.REFERENCE_POINTS/2)),int(math.floor(self.REFERENCE_POINTS/2))):
                distsum += pow(1.003,j)/self.distance(i+k-1,i+k)
            distsum /= self.REFERENCE_POINTS
            self.prob[path[i-1]][path[i]] += distsum
            self.prob[path[i]][path[i-1]] += distsum
    return path

  def distance(self,pt1,pt2):
    if pt1 >= len(self.cords):
        pt1 -= len(self.cords)
    if pt2 >= len(self.cords):
        pt2 -= len(self.cords)
    if pt1 != pt2:
        return math.sqrt((self.cords[pt1].x-self.cords[pt2].x)**2+(self.cords[pt1].y-self.cords[pt2].y)**2)
    else:
        return 1

  def lastrun(self,prob):
    path = [0]
    while len(path)<len(prob):
        for i in path:
           prob[path[-1]][i] = 0
        print prob[path[-1]]
        path.append(prob[path[-1]].index(max(prob[path[-1]])))
    return path

  def probability(self,prob,coordinate,path):
    for i in path:
        prob[coordinate][i] = 0.0
    total = sum(prob[coordinate])
    normalizedProb = [float(i)/total for i in prob[coordinate]]
    if coordinate == 0:
        print normalizedProb
    rand = random.random()
    location = 0
    while rand > 0:
        rand -= normalizedProb[location]
        location +=1
    location -=1
    return location

ant = AntSolver()
ant.cords.append(Coordinate.Coordinate(300,200))
ant.cords.append(Coordinate.Coordinate(300,100))
ant.cords.append(Coordinate.Coordinate(200,100))
ant.cords.append(Coordinate.Coordinate(200,200))
ant.cords.append(Coordinate.Coordinate(100,200))
ant.cords.append(Coordinate.Coordinate(100,300))
ant.cords.append(Coordinate.Coordinate(200,400))
ant.cords.append(Coordinate.Coordinate(200,300))
ant.cords.append(Coordinate.Coordinate(300,400))
ant.cords.append(Coordinate.Coordinate(300,300))
ant.cords.append(Coordinate.Coordinate(400,300))
ant.cords.append(Coordinate.Coordinate(400,200))
print ant.solve()
