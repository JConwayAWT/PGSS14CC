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
      self.bestOrder.append(0)
      restarts=-1
      restart=True
      while restart:
        restart=False
        restarts+=1
        if restarts==2*len(self.cords):
          break
        for iindex in range(1,len(self.bestOrder)):
          if restart:
              break
          i=self.bestOrder[iindex] 
          x=self.bestOrder[iindex-1]
          xi = (min(x,i),max(x,i))
          for aindex in range(iindex+2,len(self.bestOrder)):
            if restart:
              break
            a=self.bestOrder[aindex]           
            b=self.bestOrder[aindex-1]
            ab = (min(a,b),max(a,b))
            #print "<br>?",x,i,b,a,iindex,aindex,len(self.bestOrder),len(self.intersecting[min(x,i)][max(x,i)])
            for l in range(1,len(self.intersecting[min(x,i)][max(x,i)])):
              #print " L ",l
              if ab == self.intersecting[min(x,i)][max(x,i)][l]:
                bestOrderCopy = copy.copy(self.bestOrder)
                #print "<br> REPLACE ",iindex,aindex
                for r in range(iindex,(aindex-1)+1):
                  self.bestOrder[r]=bestOrderCopy[aindex-1-(r-iindex)]
                restart=True
                break
    print "Restarts: ",restarts,";"

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
              self.intersecting[i][x].append((a,b))
              self.intersecting[a][b].append((i,x))
              
  