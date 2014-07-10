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

<<<<<<< HEAD
import json

class TravelingSalesmanSolver:
    cords = []
    answer=""
    def __init__ (self, params = None):
        if params == None:
            return
        data = json.loads(params)
        for c in range(0,len(data['x'])):
=======
import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)


import Coordinate
import json

class TravelingSalesmanSolver:
	cords = []
	answer=""

	def __init__(self, params=None):
		if params == None:
			return
		data = json.loads(params)
		for c in range(0,len(data['x'])):
>>>>>>> 12bef692fd3d84ceddea2c0badada6a334cce4d6
			cord = Coordinate.Coordinate(data['x'][c], data['y'][c], c)
			self.cords.append(cord)

	def solve(self):
		return "No solution implemented!"

	def loadCoordinatesFromXYArrays(self,xPoints, yPoints):
		assert len(xPoints) == len(yPoints)
		for i in range(0,len(xPoints)):
			c = Coordinate.Coordinate(xPoints[i],yPoints[i])
			self.cords.append(c)






