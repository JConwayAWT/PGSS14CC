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

import Coordinate
import math
import TravelingSalesmanSolver
import LineOverlapEliminatorTravelingSalesmanSolver
import random

class AntTotalDistanceSolver (LineOverlapEliminatorTravelingSalesmanSolver.LineOverlapEliminatorTravelingSalesmanSolver):
#  probability =[[]]
  phermones =[[]]
  CALCULATIONS=10000
  traversed=[]
  numTraversed=0
  start=0
  totalDistance=0  
  bestDistance=float("inf")
  PHERNOME_SCALE=10000
  answer=";"
  order = []
  def solve(self):
    self.calculateIntersects()
    self.initArrays()
    self.compute()
    self.printBestPath()  
    return self.answer;

  def compute(self):
    for i in range(0,self.CALCULATIONS):
      self.traverse()
      #self.printPhermones()
  def initArrays(self):
    #self.probability = [[0.0000001]*len(self.cords)]*len(self.cords)    
    self.phermones =[[1 for i in range(0,len(self.cords))] for i in range(0,len(self.cords))]
    self.resetArrays()
  def resetArrays(self):
    self.traversed = [False for i in range(0,len(self.cords))]
    self.totalDistance=0
    self.numTraversed=0
    self.order = []
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
              #print "OVERLAP"
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
    self.phermones[c][j]+=self.PHERNOME_SCALE/self.totalDistance/self.totalDistance/self.totalDistance
    self.phermones[j][c]+=self.PHERNOME_SCALE/self.totalDistance/self.totalDistance/self.totalDistance

  def printBestPath(self):
    #self.printPhermones()
    self.resetArrays()
    self.bestStep(0)
    if self.totalDistance!=0:
      self.bestDistance=min(self.totalDistance,self.bestDistance)
  
  def printPhermones(self):
    print "<br> PHERMONES"
    for i in range(0,len(self.cords)):
      print "<br>"
      for j in range(0,len(self.cords)):
        print self.phermones[i][j]," "

  def bestStep(self,c):
    self.answer+=str(c )+","
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