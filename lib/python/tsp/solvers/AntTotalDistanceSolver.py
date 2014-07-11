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
import random

class AntTotalDistanceSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):
  probability =[[]]
  phermones =[[]]
  CALCULATIONS=10000
  travelIncrease=.1
  traversed=[]
  numTraversed=0
  start=0
  totalDistance=0
  totalDistance
  bestDistance=float("inf")
  PHERNOME_SCALE=1000
  answer=""
  def solve(self):
    self.initArrays()
    self.calculateDistances()
    self.compute()
    self.printBestPath()  
    return self.answer;

  def compute(self):
    for i in range(0,self.CALCULATIONS):
      self.resetArrays()
      self.traverse()
  def initArrays(self):
    self.probability = [[0]*len(self.cords)]*len(self.cords)
    self.phermones = [[0]*len(self.cords)]*len(self.cords)
    self.resetArrays()
  def resetArrays(self):
    self.traversed = [False]*len(self.cords)
    self.totalDistance=0
    self.numTraversed=0
  def traverse(self):
    self.start =int(random.randrange(0,len(self.cords)-1))
    self.oneStep(self.start)
  def oneStep(self,c):  
    self.numTraversed+=1
    if self.numTraversed>=len(self.cords):
      self.totalDistance+=self.cords[c].dist(self.cords[self.start])
      return

    
    self.traversed[c]=True
    total=0
    for j in range(0,len(self.cords)):
      if self.traversed[j]:
        continue
      total+=self.probability[c][j]+self.phermones[c][j]
    
    r = random.random()*total
    cur=0
    
    j=0
    for j in range(0,len(self.cords)):
      if self.traversed[j]:continue
      cur+=self.probability[c][j]+self.phermones[c][j]
      if cur>r:
        self.totalDistance+=self.cords[c].dist(self.cords[j])
        self.oneStep(j)
        break
      
    
    self.phermones[c][j]+=self.PHERNOME_SCALE/self.totalDistance/self.totalDistance/self.totalDistance
  
  def printBestPath(self):
    self.resetArrays()
    self.bestStep(0)
    if self.totalDistance!=0:
      self.bestDistance=min(self.totalDistance,self.bestDistance)
  
  def bestStep(self,c):
    self.answer+=str(c)+","
    self.numTraversed+=1
    if self.numTraversed>=len(self.cords):
      self.totalDistance+=self.cords[c].dist(self.cords[0])
      return
    
    self.traversed[c]=True
    best=0
    bc=0
    for i in range(1,len(self.cords)):
      if self.traversed[i]:continue
      if self.phermones[c][i]>best:
        best=self.phermones[c][i]
        bc=i
      
    
    if bc==0:
      self.totalDistance=float("inf")
    else:
      self.totalDistance+=self.cords[c].dist(self.cords[bc])
      self.bestStep(bc)
  
  
  def calculateDistances(self):
    for i in range(0,len(self.cords)):
      for j in range(0,len(self.cords)):
        if i==j:continue
        self.probability [i][j]=1/self.cords[i].dist(self.cords[j])
      
    
#a = AntTotalDistanceSolver()
#a.loadCoordinatesFromXYArrays([0,10,0,10],[0,0,10,10])
#print a.solve()