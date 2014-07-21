#-------------------------------------------------------------------------------
# Name:        Brute Force Traveling Salesman Solver
# Purpose:     Traveling salesman brute force solver
#
# Author:      Martin Schneider
#
# Created:     07/09/2014
# Copyright:   (c) Martin 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate
import math
import TravelingSalesmanSolver
import LineOverlapEliminatorTravelingSalesmanSolver
import random
import copy

class AntTotalDistanceSolver (LineOverlapEliminatorTravelingSalesmanSolver.LineOverlapEliminatorTravelingSalesmanSolver):
#  probability =[[]]
  phermones =[[]]
  CALCULATIONS=10000
  CALCULATION_UPDATES=100
  BEST_UPDATES=1000
  debugData=""
  traversed=[]
  numTraversed=0
  start=0
  totalDistance=0  
  bestDistance=float("inf")
  avgEdgeWeight=0
  PHERNOME_SCALE=1000000
  PHERNOME_EXP  =3#must be odd
  order = []
  def solve(self):
    if self.REMOVE_LINE_CROSSES:
      self.calculateIntersects()
    self.startTime = self.millis()
    self.initArrays()
    self.compute()
    self.printBestPath()  
    return self.answer;

  def compute(self):
    for i in range(0,self.CALCULATIONS):
      if i%self.CALCULATION_UPDATES==0:
        pDone=float(i)/self.CALCULATIONS
        self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
        self.checkTimeout(self)
      if i%self.BEST_UPDATES==0:
        self.printBestPath()
        self.setSolution(self.answer)

      self.traverse()
      #self.printPhermones()
  def printPhermones(self):
    self.debugData+="PHERMONES:"
    for i in range(0,len(self.cords)):
      self.debugData+="<br>"
      for j in range(0,len(self.cords)):
        self.debugData+=str(round(self.phermones[i][j]*10000)/10000)+" "

  def initArrays(self):
    #self.probability = [[0.0000001]*len(self.cords)]*len(self.cords)    
    self.phermones =[[1 for i in range(0,len(self.cords))] for i in range(0,len(self.cords))]
    #totalEdgeDist=0
    #for i in range(0,len(self.cords)):
      #for j in range(0,len(self.cords)):
        #if i==j:
          #continue
        #totalEdgeDist+=self.cords[i].dist(self.cords[j])
    #self.avgEdgeWeight=totalEdgeDist/pow(len(self.cords),2)
    edgeDistScale=self.PHERNOME_SCALE/10#totalEdgeDist/len(self.cords)
    for i in range(0,len(self.cords)):
      for j in range(0,len(self.cords)):
        if i==j:
          continue              
        self.phermones[i][j]+=edgeDistScale/pow(self.cords[i].dist(self.cords[j]),3)#self.PHERNOME_EXP)
        self.phermones[j][i]+=edgeDistScale/pow(self.cords[i].dist(self.cords[j]),3)#self.PHERNOME_EXP)
    self.resetArrays()    
  def resetArrays(self):
    self.traversed = [False for i in range(0,len(self.cords))]
    self.totalDistance=0
    self.numTraversed=0
    self.order = []
    self.bestOrder = []
  def traverse(self):
    self.resetArrays()
    self.start=random.randint(0,len(self.cords)-1)
    self.oneStep(self.start)
  def oneStep(self,c):      
    self.numTraversed+=1
    works = True
    self.traversed[c]=True  
    self.order.append(c)

    if self.numTraversed>=len(self.cords):
      #x=self.order[0]
      #for i in range(1,len(self.order)):
        #x=self.order[i-1]
        #if(not works):break
        #xi = (min(x,i),max(x,i))
        #for a in range(1,len(self.order)):
          #b=self.order[a-1]
          #if(not works):break
          #ab = (min(a,b),max(a,b))
          #print "<br> Test", x,i,a,b
          #for l in range(1,len(self.intersecting[min(x,i)][max(x,i)])):
            #if ab == xi:
              #works=False
              #break
      if works:
        self.updatePhermones(c,self.start)
      return works

    total=0
    for j in range(0,len(self.cords)):
      if self.traversed[j]:
        continue
      total+=self.phermones[c][j]

    r = random.uniform(0,total)
    #self.debugData+="<br>"+" "+str(r)+" "+str(total)
    cur=0
    for j in range(0,len(self.cords)):
      if self.traversed[j]:
        continue
      cur+=self.phermones[c][j]
      if cur>r:
        self.totalDistance+=self.cords[c].dist(self.cords[j])
        works = self.oneStep(j)
        break

    if works:
      self.updatePhermones(c,j)
    return works
  def updatePhermones(self, c, j):
    avg = self.avgEdgeWeight*len(self.cords)
    self.phermones[c][j]+=self.PHERNOME_SCALE/pow(avg-self.totalDistance,self.PHERNOME_EXP)
    self.phermones[j][c]+=self.PHERNOME_SCALE/pow(avg-self.totalDistance,self.PHERNOME_EXP)

  def printBestPath(self):
    self.resetArrays()
    

    self.bestStep(0)
    self.removeLineCrosses()
    self.answer=self.debugData
    for c in range(0,len(self.bestOrder)):
      self.answer+=str(self.bestOrder[c])+","

    if self.totalDistance!=0:
      self.bestDistance=min(self.totalDistance,self.bestDistance)
  
  def bestStep(self,c):
    self.bestOrder.append(c)
    self.numTraversed+=1
    if self.numTraversed>=len(self.cords):
      self.totalDistance+=self.cords[c].dist(self.cords[0])
      return
    
    self.traversed[c]=True
    best=0
    bc=0
    for i in range(1,len(self.cords)):
      if self.traversed[i]:
        continue
      #print "<br>?",c,i,best,self.phermones[c][i]
      if self.phermones[c][i]>best:
        #print "!"
        best=self.phermones[c][i]
        bc=i
    
    #print "<br>B",best,bc

    if bc==0:
      self.totalDistance=float("inf")
    else:
      self.totalDistance+=self.cords[c].dist(self.cords[bc])
      self.bestStep(bc)
  
      
#a = AntTotalDistanceSolver()
#a.loadCoordinatesFromXYArrays([0,10,0,10],[0,0,10,10])
#print a.solve()