#-------------------------------------------------------------------------------
# Name:        SimulatedAnnealingSalesmanSolver
# Purpose:
#
# Author:      Justin
#
# Created:     14/07/2014
# Copyright:   (c) Justin 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys;
import random;
import math as m
lib_path = os.path.abspath('..');
sys.path.append(lib_path);

import Coordinate as CC

lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)

import math
import TravelingSalesmanSolver

class SimulatedAnnealingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  bestOrder=[]
  bestDistance=float("inf")
  Temperature = 1.0
  bestscore = 0
  def debug (self):
    print("A")
    print (self.main())
    print("Z")

  def __init__(self):
    pass
  def solve(self):
    self.bestDistance=float("inf")
    self.compute(0, 0, -1, []);
    self.getAnswer()
    return self.answer;

  def getcenterofmass(self): ###debugged
        xsum = 0.0;
        ysum = 0.0;
        for i in range(0, len(self.cords)):
            xsum += self.cords[i].x;
            ysum += self.cords[i].y;
        CM = CC.Coordinate(xsum/len(self.cords), ysum/len(self.cords), 0);
        return CM;



  def originTransform(self,index):
    xold=self.cords[index].x
    yold=self.cords[index].y

    cords=self.getcenterofmass()
    self.cords[index]=CC.Coordinate(xold-cords.x,yold-cords.y, index)

  def getradius(self, point):
    return ((self.cords[point].x)**2 + (self.cords[point].y)**2)**0.5

  def getangle(self,point):
    return m.atan2(self.cords[point].y,self.cords[point].x)

  def addpolarcord(self):
    pass
    """
    for index in range(0, len(self.cords)):
        self.originTransform(index)
        self.cords[index].append(self.getradius(point))
        self.cords[index].append(self.getangle(point))
        """
  def generatepath(self):
    answerpath = ""
    for index in range(0,len(self.cords)):
            answerpath += str(self.cords[index])
    return answerpath #organize based on angle value


  def distance(self, path):
    distance = 0
    for node in path:
        print(node)
        distance += self.cords[path[int(node)]].dist(self.cords[path[int(node)+1]])
    return distance

  def Scoringfunction(self,path):
    scorefn=math.e*((-self.distance(path))/Temperature)

  def generatenewpath (self, path):#######bug########
    print((path,"aa"))
    answerpath = ""
    randint1 = random.randint(0,(len(self.cords)%2))
    switchedentry = 0
    index = 0
    for entry in path:
        entry = str(entry)
        if index == randint1:
            switchedentry = entry
        elif index == (randint1 + 1):
            answerpath += (str(switchedentry) + entry)
        else:
            answerpath += entry
    return answerpath
  def AnnealingMC(self):
    currentpath = self.generatepath()
    newpath =self.generatenewpath(currentpath)

    newscore = self.Scoringfunction(newpath)
    currentscore = self.Scoringfunction(currentpath)

    score = [newscore,currentscore]
    if currentscore < newscore:
        return [newpath, score]
    else:
        randint = random.randint(100)
        probability = newscore/currentscore
        if randint > 100*probability:
            return [newpath, score]
        else:
            return [currentpath, score]

  def main(self):
    self.addpolarcord()
    path = "a"
    #path=self.generatepath()
    for timestried in range(10):
        solution = self.AnnealingMC()
        if solution[1]>bestscore:
            path = solution[0]
    self.setSolution(path)
    return path

#if __name__ == '__main__':
    #A=SimulatedAnnealingSalesmanSolver()
    #A.cords.append(CC.Coordinate(0,0,0))
    #A.cords.append(CC.Coordinate(1,1,1))
    #A.cords.append(CC.Coordinate(1,2,2))
    #print(A.debug())
    #print(A.main())
