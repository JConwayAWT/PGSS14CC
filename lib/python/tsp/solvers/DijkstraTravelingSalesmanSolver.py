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
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate
import math
import TravelingSalesmanSolver

class DijkstraTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

	bestOrder=[]
	bestDistance=float("inf")
	number_of_connections = []
	distances_array = [[]]
	
	def solve(self):
		self.number_of_cities = len(self.cords)
		self.city_used_in_path = [False]*self.number_of_cities
  		self.city_used_in_path[0] = True
  		self.itinerary = []
  		number_of_connections = [0]*self.number_of_cities
		self.compute_dist_to_next_city()
		print "itinerary is: " + str(self.itinerary)

	def compute_all_distances(self): # creating a two-way array for all distances, doesn't seem to be working yet
		for k in range(0, len(self.cords)):
			for j in range(0, len(self.cords)):
				distances_array[k].append(self.cords[k].dist(self.cords[j]))
		print distances_array

	def compute_dist_to_next_city(self): # computes distances to all other cities from one individual city
		self.dist_to_next_city = []
		for j in range(0, len(self.cords)):
			self.dist_to_next_city.append(self.cords[0].dist(self.cords[j]))
			print "dist to next city is: " + str(self.dist_to_next_city)
			print "this many coordinates: " + str(len(self.cords))
		print "min dist is: " + str(min(dist for dist in self.dist_to_next_city if dist > 0))
		self.next_city = self.dist_to_next_city.index(min(dist for dist in self.dist_to_next_city if dist > 0))
		print "goto here: " + str(self.next_city)
		self.itinerary.append(self.next_city)
		self.city_used_in_path[0] = True
		print "index of next city is: " + str(self.itinerary)



dijkstra = DijkstraTravelingSalesmanSolver()

dijkstra.cords.append(Coordinate.Coordinate(90,20))
dijkstra.cords.append(Coordinate.Coordinate(21,34))
dijkstra.cords.append(Coordinate.Coordinate(34,56))
dijkstra.cords.append(Coordinate.Coordinate(28,50))
dijkstra.cords.append(Coordinate.Coordinate(51,80))
dijkstra.cords.append(Coordinate.Coordinate(68,72))

print dijkstra.solve()