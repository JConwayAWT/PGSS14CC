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


import Coordinate
import json

class TravelingSalesmanSolver:
	cords = []
	answer=";"
	cur=None
	database_row_id=0

	def __init__(self, params=None):
		if params == None:
			return
		data = json.loads(params)
		for c in range(0,len(data['x'])):
			cord = Coordinate.Coordinate(data['x'][c], data['y'][c], c)
			self.cords.append(cord)

	def solve(self):
		return "No solution implemented!"

	def setStatusDone(self,statusDone):
		self.cur.execute ("UPDATE traveling_salesmen SET statusDone=\'"+statusDone+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def setSolution(self,answer):
		print "Solution"
		print answer
		print self.cur
		print self.database_row_id
		self.cur.execute ("UPDATE traveling_salesmen SET answer=\'"+answer+"\' WHERE id=\'"+str(self.database_row_id)+"\';")

	def loadCoordinatesFromXYArrays(self,xPoints, yPoints):
		assert len(xPoints) == len(yPoints)
		for i in range(0,len(xPoints)):
			c = Coordinate.Coordinate(xPoints[i],yPoints[i])
			self.cords.append(c)







