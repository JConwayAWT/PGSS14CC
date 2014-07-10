# ------------------------------------------------------------------------------
# THIS IS MY OWN HEADING, ISHAN
# Name:		Dijkstra Traveling Salesman Solver
# Purpose:	To solve the traveling salesman problem using Dijkstra's Algorithm
# Author: 	Songela Chen
# Date: 	07/10/14
# ------------------------------------------------------------------------------

import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import Coordinate
import math
import TravelingSalesmanSolver

class DijkstraTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

	bestOrder=[]
	bestDistance=float("inf")
	
	def solve(self):
		self.cords[0].i

		number_of_cities = len(self.cords)
		city_used_in_path = [False]*number_of_cities
  		city_used_in_path[0] = True
  		index_of_min_distance = [1]

	def dist(self):
		for k in range(0,len(self.cords)):
			for j in range(0, len(self.cords)):
				dist_to_city = self.cords[k].dist(self.cords[j])
				min_dist_from_city = min(dist_to_city)
				next_city = self.cords.index(min_dist_from_city)
				index_of_min_distance.append(next_city)

		print index_of_min_distance