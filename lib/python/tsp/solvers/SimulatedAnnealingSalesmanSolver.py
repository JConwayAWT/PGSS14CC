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
import copy
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
#  def solve(self):
    #self.bestDistance=float("inf")
    #self.compute(0, 0, -1, []);
    #self.getAnswer()
    #return self.answer;

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
            answerpath += str(self.cords[index].i)
    print (answerpath)
    return answerpath #organize based on angle value


  def distance(self, path):
    distance = 0
    countruns =0
    finalnode = 0
    pathclone = copy.deepcopy(path)
    #pathclone = pathclone.split(",")
    for node in pathclone:
        node = int(node)
        if countruns == 0:
            finalnode = node
        nextnodecount = countruns + 1
        if (countruns + 1) == len(pathclone):
            countruns = -1
        nextnode= int(pathclone[countruns+1])
        if nextnode == (len(pathclone)):
            nextnode = int(finalnode)
        print(self.cords[int(node)].dist(self.cords[nextnode]),node,nextnode)
        distance += self.cords[int(node)].dist(self.cords[nextnode])
        countruns += 1

    return distance

  def Scoringfunction(self,path):
    scorefn=-self.distance(path)#math.e*((-self.distance(path))/self.Temperature)
    return scorefn
  def generatenewpath (self, path):#######bug########
    print((path,"aa"))
    answerpath = ""
    randint1 = random.randint(0,(len(path)-2))
    switchedentry = ""
    index = 0
    for entry in path:
        entry = str(entry)
        if index == randint1:
            switchedentry = entry
        elif index == (randint1 + 1):
            answerpath += (entry + str(switchedentry) )
        else:
            answerpath += entry
        index += 1
    return answerpath
  def AnnealingMC(self):
    currentpath = self.generatepath()
    newpath =self.generatenewpath(currentpath)

    newscore = self.Scoringfunction(newpath)
    currentscore = self.Scoringfunction(currentpath)

    score = newscore

    if currentscore <= newscore:
        return [newpath, score]
    else:
        randint = random.randint(0,100)
        probability = newscore/currentscore
        if randint > 100*probability:
            return [newpath, score]
        else:
            return [currentpath, score]

  def solve(self):
    self.addpolarcord()
    bestpath=""
    path = "a"
    #path=self.generatepath()
    for timestried in range(1000):
        solution = self.AnnealingMC()
        print (solution[1])
        if path == "a":
                path = solution[0]
        if solution[1]<self.bestscore:
            path = solution[0]
            bestscore = solution[1]
    print(path, bestscore, "path")
    #self.setSolution(path)
    finalsolution = ""
    for element in path:
        finalsolution += element.i
        finalsolution += ","
    return finalsolution

#
#if __name__ == '__main__':
    #A=SimulatedAnnealingSalesmanSolver()
    #A.cords.append(CC.Coordinate(-2,0,0))
    #A.cords.append(CC.Coordinate(-1,1,5))
    #A.cords.append(CC.Coordinate(0,2,2))
    #A.cords.append(CC.Coordinate(1,1,4))
    #A.cords.append(CC.Coordinate(2,0,3))
    #A.cords.append(CC.Coordinate(0,-2,1))
    #print(A.main(), "sol")
    #print(A.distance("3,0,1,2"))
