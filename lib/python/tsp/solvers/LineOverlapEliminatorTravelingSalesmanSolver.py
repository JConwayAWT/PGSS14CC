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
import Line
import random
import copy

class LineOverlapEliminatorTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  def __init__(self,params=None):
    self.initSolver(params)
    self.initOverlapSolver()
  def initOverlapSolver(self):
     #print "L"
     #super(TravelingSalesmanSolver,self).__init__()
     self.REMOVE_LINE_CROSSES=True
     self.bestOrder = []
     self.intersecting = []

  def solve(self):
    self.bestOrder = [i for i in range(0,len(self.cords))]

    random.shuffle(self.bestOrder)

    self.calculateIntersects()
    self.removeLineCrosses()
    self.printBestPath()
    return self.answer;

  def printBestPath(self):
    self.answer+=";"
    for c in range(0,len(self.bestOrder)):
      self.answer+=str(self.bestOrder[c])+","

  def removeLineCrosses(self):
    self.setStatusDone("Removing line crosses...")
    restarts=0
    if self.REMOVE_LINE_CROSSES:
      #self.bestOrder.append(0)
      restarts=-1
      restart=True
      while restart:
        #print "<br> <b> START</b>"
        restart=False
        restarts+=1
        #self.answer+="Start<br>"
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
            if a==x:
              continue
            ab = (min(a,b),max(a,b))
            #self.answer+="<br>L "+str(a)+" "+str(b)+" "+str(x)+" "+str(i)+" "+str(aindex)+" "+str(iindex)
            if self.intersects(a,b,x,i):#ab == self.intersecting[min(x,i)][max(x,i)][l]:
              bestOrderCopy = copy.copy(self.bestOrder)
              #self.answer+="New Inter"+" "+str(iindex)+" "+str(aindex)
              for r in range(iindex,(aindex-1)+1):
                self.bestOrder[r]=bestOrderCopy[aindex-1-(r-iindex)]
                restart=True
            #break
    #print "Restarts: ",restarts,";"

  def intersects(self, a,b,x,i):
    #if self.intersecting[a][b][x][i] == None:
      #self.intersecting[a][b][x][i]=Line.linesIntersect(self.cords[i],self.cords[x],self.cords[a],self.cords[b])
    #return self.intersecting[a][b][x][i]
    return Line.linesIntersect(self.cords[i],self.cords[x],self.cords[a],self.cords[b])


  def calculateIntersects(self):
    self.intersecting= [[ [] for i in range(0,len(self.cords))] for i in range(0,len(self.cords))]
    #for i in range(0,len(self.cords)):
      #pDone = float(i)/len(self.cords)
      #self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone)+" | Calculating intersections...")
      #for x in range(i+1,len(self.cords)):
        #for a in range(i+1,len(self.cords)):
          #if a == x or a == i:
            #continue
          #for b in range(a+1,len(self.cords)):
            #if b == x or b == i:
              #continue
            #if Line.linesIntersect(self.cords[i],self.cords[x],self.cords[a],self.cords[b]):
              #print "<br> Intersect ",i,x,a,b
              #self.intersecting[i][x].append((a,b))
              #self.intersecting[a][b].append((i,x))

