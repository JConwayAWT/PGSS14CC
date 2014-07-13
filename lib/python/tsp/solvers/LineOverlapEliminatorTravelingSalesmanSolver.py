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
import Line
import random
import copy

class LineOverlapEliminatorTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):
  REMOVE_LINE_CROSSES=True
  bestOrder = []
  intersecting = []

  def solve(self):
    self.bestOrder = [i for i in range(0,len(self.cords))]

    random.shuffle(self.bestOrder)

    self.calculateIntersects()
    self.removeLineCrosses()
    self.printBestPath()  
    return self.answer;

  def printBestPath(self):
    for c in range(0,len(self.bestOrder)):
      self.answer+=str(self.bestOrder[c])+","

  def removeLineCrosses(self):
    restarts=0
    if self.REMOVE_LINE_CROSSES:
      #self.bestOrder.append(0)
      restarts=-1
      restart=True
      while restart:
        #print "<br> <b> START</b>"
        restart=False
        restarts+=1
        if restarts==len(self.cords):
          break
        for iindex in range(1,len(self.bestOrder)):
          i=self.bestOrder[iindex] 
          x=self.bestOrder[iindex-1]
          xi = (min(x,i),max(x,i))
          for aindex in range(iindex+2,len(self.bestOrder)+1):
            aindexAdjusted= aindex if aindex<len(self.bestOrder) else 0
            a=self.bestOrder[aindexAdjusted]           
            b=self.bestOrder[aindex-1]
            ab = (min(a,b),max(a,b))
            #print "<br>?",x,i,b,a,iindex,aindexAdjusted,len(self.bestOrder),len(self.intersecting[min(x,i)][max(x,i)]),ab,xi
            for l in range(0,len(self.intersecting[min(x,i)][max(x,i)])):
              #print "<br>L ",ab,min(x,i),max(i,x),self.intersecting[min(x,i)][max(x,i)][l]
              if ab == self.intersecting[min(x,i)][max(x,i)][l]:
                bestOrderCopy = copy.copy(self.bestOrder)
                for r in range(iindex,(aindex-1)+1):
                  self.bestOrder[r]=bestOrderCopy[aindex-1-(r-iindex)]
                restart=True
                break
    #print "Restarts: ",restarts,";"

  def calculateIntersects(self):    
    self.intersecting= [[ [] for i in range(0,len(self.cords))] for i in range(0,len(self.cords))]
    for i in range(0,len(self.cords)):
      for x in range(i+1,len(self.cords)):
        for a in range(i+1,len(self.cords)):
          if a == x or a == i:
            continue
          for b in range(a+1,len(self.cords)):
            if b == x or b == i:
              continue
            if Line.linesIntersect(self.cords[i],self.cords[x],self.cords[a],self.cords[b]):
              #print "<br> Intersect ",i,x,a,b
              self.intersecting[i][x].append((a,b))
              self.intersecting[a][b].append((i,x))
              
  