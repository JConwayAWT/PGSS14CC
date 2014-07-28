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

from math import *
from TravelingSalesmanSolver import *


class SimulatedAnnealingSalesmanSolver (TravelingSalesmanSolver):

  def __init__(self,params=None):

    self.initSolver(params)
    self.bestOrder=[]
    self.bestDistance=float("inf")
    self.Temperature = 1.0
    self.bestscore = None
    self.bestPath = []

#  def solve(self):
    #self.bestDistance=float("inf")
    #self.compute(0, 0, -1, []);
    #self.getAnswer()
    #return self.answer;
  def setbestPath(self, changepath):
        self.bestPath = changepath
  def getcenterofmass(self): ###debugged
        xsum = 0.0;
        ysum = 0.0;
        for i in range(0, len(self.cords)):
            xsum += self.cords[i].x;
            ysum += self.cords[i].y;
        CM = CC.Coordinate(xsum/len(self.cords), ysum/len(self.cords), 0);
        return CM;


  """
  def originTransform(self,index):
    xold=self.cords[index].x
    yold=self.cords[index].y

    cords=self.getcenterofmass()
    self.cords[index]=CC.Coordinate(xold-cords.x,yold-cords.y, index)

  def getradius(self, point):
    return ((self.cords[point].x)**2 + (self.cords[point].y)**2)**0.5

  def getangle(self,point):
    return m.atan2(self.cords[point].y,self.cords[point].x)
    """
  def addpolarcord(self):
    pass
    """
    for index in range(0, len(self.cords)):
        self.originTransform(index)
        self.cords[index].append(self.getradius(point))
        self.cords[index].append(self.getangle(point))
        """
  def generatepath(self):
    answerpath = []
    for index in range(0,len(self.cords)):
        #print(len(self.cords), index)
        #print (self.cords[index].i)
        answerpath.append( self.cords[index].i)
    #print (answerpath, "generatepathdebug")
    return answerpath #organize based on angle value


  def distance(self, path):
    distance = 0
    countruns =0
    finalnode = 0
    pathclone = copy.deepcopy(path)
    #print path
    #pathclone = pathclone.split(",")
    for node in pathclone:
        node = int(node)
        #print node
        if countruns == 0:
            finalnode = node
        #nextnodecount = countruns + 1
        if (countruns + 1) == len(pathclone):
            countruns = -1
        nextnode= pathclone[countruns+1]
        if nextnode == (len(pathclone)):
            nextnode = finalnode
        #print (node,nextnode)
        #print(self.cords[int(node)].dist(self.cords[nextnode]))
        #print (finalnode)
        distance += self.cords[node].dist(self.cords[nextnode])
        #print (self.cords[node].dist(self.cords[nextnode]))
        countruns += 1
        #print ("d",distance)
    return distance

  def Scoringfunction(self,path):
    scorefn=self.distance(path)#math.e*((-self.distance(path))/self.Temperature)
    return scorefn
  def generatenewpath (self, path):#######bug########
    answerpath = copy.deepcopy(path)
    randint1 = random.randint(0,(len(path)-1))
    switchedentry = None
    first = answerpath[randint1]
    indextwo = randint1 + 1
    #print (indextwo)
    if randint1 +1 >= len(path):
        indextwo = 0
    second = answerpath[indextwo]
    #print (first,second,randint1,indextwo, "answerpath")
    answerpath[randint1] = second
    answerpath[indextwo] = first
    """
    for entry in path:
        entry = int(entry)
        if index == randint1:
            switchedentry = entry
        elif index == (randint1 + 1):
            answerpath += (entry + str(switchedentry) )
        else:
            answerpath+=(entry)
        index += 1
        """
    #print((answerpath,"aa"))
    return answerpath
  def AnnealingMC(self, path):
    #currentpath = self.generatepath()
    currentpath = path
    newpath =self.generatenewpath(currentpath)

    newscore = self.Scoringfunction(newpath)
    currentscore = self.Scoringfunction(currentpath)

    score = newscore
    #print (currentpath, currentscore, newpath, score)

    if currentscore >= newscore:
        #print ("YAYAYAY", newpath)
        return [newpath, score,newpath]
    else:
        randint = random.randint(0,100)
        probability = newscore/currentscore
        if randint > 100*probability:
            return [newpath, score,newpath]
        else:
            return [currentpath, currentscore,newpath]

  def solve(self):
    #self.addpolarcord()
    bestpath=[]
    path = []
    #path=self.generatepath()
    currentpath = self.generatepath()
    CALCULATIONS=100000
    for timestried in range(CALCULATIONS):
        if timestried%1000==0:
            pDone=float(timestried)/CALCULATIONS
            self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
            self.checkTimeout(self)

        solution = self.AnnealingMC(currentpath)
        currentpath = solution[2]
        if self.bestscore == None:
            self.bestscore = solution[1]
            self.bestPath = solution[0]
        if solution[1] < self.bestscore:
            print(self.bestscore,self.bestPath)
            self.bestscore = solution[1]
            self.bestPath = solution[0]
            print(self.bestPath, self.bestscore, "bestpath")
    #self.setSolution(path)
    finalsolution = ""
    index = 0
    print (self.bestPath, "sdf")
    for element in self.bestPath:
        if index != 0:
            finalsolution += ","
        print (element)
        element = str(element)
        finalsolution += element
        index += 1
    return finalsolution

#
if __name__ == '__main__':
    A=SimulatedAnnealingSalesmanSolver()
    A.cords.append(CC.Coordinate(-2,0,0))
    A.cords.append(CC.Coordinate(-1,2,1))
    A.cords.append(CC.Coordinate(0,2,2))
    A.cords.append(CC.Coordinate(1,1,3))
    A.cords.append(CC.Coordinate(2,0,4))
    A.cords.append(CC.Coordinate(0,-2,5))
    print(A.solve(), "sol")
    #print(A.distance([0,1,2,3]))
    #print(A.distance([0,2,1,3]))
    #print(A.distance([1,0,2,3]))
