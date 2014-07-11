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

import Coordinate
import json

class TravelingSalesmanSolver:
<<<<<<< HEAD
    cords = []
    answer=""

    def __init__(self, params = None):
        if params == None:
            return
        data = json.loads(params)
        for c in range(0,len(data['x'])):
=======
	cords = []
	answer=""

	def __init__(self, params):
		data = json.loads(params)
		for c in range(0,len(data['x'])):
>>>>>>> e83d1c30ccb7f76513547fed35dba64196a9554f
			cord = Coordinate.Coordinate(data['x'][c], data['y'][c], c)
			self.cords.append(cord)

	def solve(self):
<<<<<<< HEAD
		return "No solution implemented!"






=======
		return "No solution implemented!"
>>>>>>> e83d1c30ccb7f76513547fed35dba64196a9554f
