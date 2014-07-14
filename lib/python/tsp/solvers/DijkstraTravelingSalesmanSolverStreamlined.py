import os, sys
lib_path = os.path.abspath('..')
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
    self.distances_to_and_from_each_city = self.initialize_distances_to_and_from_each_city()
    self.visited_cities_by_index = [False]*len(self.cords)
    self.outward_bound_current_city_index = 0
    self.inward_bound_current_city_index = 0
    self.degree_for_city_as_index = [0]*len(self.cords)
    for i in range(len(self.cords)):
      self.pick_the_next_best_available_path(i)

  def pick_the_next_best_available_path(self, i):
    pass
    #figure out what is currently the tip of the incoming path
    #figure out what is currently the tip of the outgoing path
    #find the distances from both of those cities to any other cities
    #choose the minimum distance city which meets the following criteria:
    # -- the distance is not 0 (don't travel to yourself)
    # -- the degree is not 2 (already has incoming/outgoing route)
    # -- we don't connect incoming and outgoing UNLESS this is the final move
    #
    # It may be more efficient to do a check such as this:
    # if (time_for_the_final_move()):
    #   connect_incoming_and_outgoing()
    # else:
    #   do_the_logic_from_above_except_for_the_last_line
    #
    # after choosing the next city:
    # -- update the degree of both cities involved
    # -- update the tip of whichever path is involved
    # -- update the itinerary
    #
    # the return value should probably be the index of the city


  def initialize_distances_to_and_from_each_city(self):
    distances_per_city = []
    for j in self.cords:
      current_city_list = []
      for k in self.cords:
        current_city_list.append(j.dist(k))
      distances_per_city.append(current_city_list)
    return distances_per_city




dijkstra = DijkstraTravelingSalesmanSolver()

dijkstra.cords.append(Coordinate.Coordinate(90,20))
dijkstra.cords.append(Coordinate.Coordinate(21,34))
dijkstra.cords.append(Coordinate.Coordinate(34,56))
dijkstra.cords.append(Coordinate.Coordinate(28,50))
dijkstra.cords.append(Coordinate.Coordinate(51,80))
dijkstra.cords.append(Coordinate.Coordinate(68,72))

print dijkstra.solve()