#-------------------------------------------------------------------------------
# Name:        SimulatedAnnealingSalesmanSolver
# Purpose:     model traveling salesman problem based on simulated annealing
#
# Author:      Justin
#
# Created:     10/07/2014
# Copyright:   (c) Justin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys;
lib_path = os.path.abspath('..');
sys.path.append(lib_path);
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)


import math
import TravelingSalesmanSolver

class SimulatedAnnealingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  bestOrder=[]
  bestDistance=float("inf")

  def __init__(self,cords):
    self.cords = cords
    self.cords[0].dist()
  def solve(self):
    self.bestDistance=float("inf")
    self.compute(0, 0, -1, []);
    self.getAnswer()
    return self.answer;

  def getcenterofmass(self):
    pass#(get from Narahari)
  def originTransform(self,index):
    xold=self.cord[index].x
    yold=self.cord[index].y
    cords=self.getcenterofmass()
    self.cord[index].init(xold-cords[0],yold-cords[1], 0);

  def getradius(self, point):
    return ((self.cords[point].x)**2 + (self.cords[point].y)**2)**0.5
  def getangle(self,point):
    return atan2(self.cords[point].y,self.cords[point].x)

  def addpolarcord(self,cords):

    for index in range(0, len(self.cords)):
        self.originTransform()
        self.cords[index].append(self.getradius(point),self.getangle(point),index)
  def generatepath(self):
    return [//path//]#organize based on angle value



  def Scoringfunction(self):
    scorefn=math.e*((-self.cord.dist)/)
  def AnnealingMC(self):

  def main(self):

    self.addpolarcord(cords)
    path=self.generatepath()












if __name__ == '__main__':
    cords ="database"
    A=SimulatedAnnealingSalesmanSolver(cords)
