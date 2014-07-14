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
	cords = []
	answer=""

	def __init__(self, params):
		data = json.loads(params)
		for c in range(0,len(data['x'])):
			cord = Coordinate.Coordinate(data['x'][c], data['y'][c], c)
			self.cords.append(cord)

	def solve(self):
		return "No solution implemented!"