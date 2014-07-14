#-------------------------------------------------------------------------------
# Name:        Traveling Salesman Solver
# Purpose:     Traveling salesman base solver
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
import time
import Coordinate
import json
import math

class TravelingSalesmanSolver:
	cords = []
	answer=";"
	cur=None
	database_row_id=0

	def __init__(self, params=None):

		self.startTime = self.millis()

		if params == None:
			return
		data = json.loads(params)
		for c in range(0,len(data['x'])):
			cord = Coordinate.Coordinate(data['x'][c], data['y'][c], c)
			self.cords.append(cord)

	def solve(self):
		return "No solution implemented!"

	def setMessage(self,message):
		self.cur.execute ("UPDATE traveling_salesmen SET message=\'"+message+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def setStatusDone(self,statusDone):
		self.cur.execute ("UPDATE traveling_salesmen SET statusdone=\'"+statusDone+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def setSolution(self,answer):
		self.cur.execute ("UPDATE traveling_salesmen SET answer=\'"+answer+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def setDone(self,done):
		self.cur.execute ("UPDATE traveling_salesmen SET done=\'"+done+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def loadCoordinatesFromXYArrays(self,xPoints, yPoints):
		assert len(xPoints) == len(yPoints)
		for i in range(0,len(xPoints)):
			c = Coordinate.Coordinate(xPoints[i],yPoints[i])
			self.cords.append(c)
	def millis(self):
		return int(round(time.time() * 1000))
	def remainingTime(self,pDone):
		if pDone==0:
			pDone=1
		elapsedSec=int((self.millis()-self.startTime)/1000)
		totalSec =int(elapsedSec/pDone)
		return str(totalSec-elapsedSec)+"s remaining /"+str(totalSec)+"s total"







