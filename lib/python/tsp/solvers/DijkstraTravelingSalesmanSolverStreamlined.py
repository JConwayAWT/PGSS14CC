import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import Coordinate
import math
import TravelingSalesmanSolver

class DijkstraTravelingSalesmanSolver (TravelingSalesmanSolver.TravelingSalesmanSolver):

  itinerary = []

  def solve(self):
    self.distances_array = self.initialize_distances_to_and_from_each_city()
    self.visited_cities_by_index = [False]*len(self.cords)
    self.outward_bound_current_city_index = 0
    self.inward_bound_current_city_index = 0
    self.degree_for_city_as_index = [0]*len(self.cords)
    for i in range(len(self.cords)):
      self.pick_the_next_best_available_path(i)
    print self.itinerary

  def pick_the_next_best_available_path(self, i):
    #figure out what is currently the tip of the incoming path
    outward_index = self.outward_bound_current_city_index
    outward_degree = self.degree_for_city_as_index[outward_index]
    print "outward_index BEFORE" + str(outward_index)
    #figure out what is currently the tip of the outgoing path
    inward_index = self.inward_bound_current_city_index
    inward_degree = self.degree_for_city_as_index[inward_index]
    #find the distances from both of those cities to any other cities
    distances_from_outbound = self.distances_array[outward_index]
    print self.distances_array
    print distances_from_outbound
    minimum_distance_from_outbound = 9999999999999999
    index_minimum_current_outbound_city = 0
    for i in range(len(self.cords)):
      if distances_from_outbound[i] < minimum_distance_from_outbound and distances_from_outbound[i] != 0 and self.degree_for_city_as_index[i] != 2:
        minimum_distance_from_outbound = distances_from_outbound[i]
        index_minimum_current_outbound_city=i
    print "minimum_distance_from_outbound" + str(minimum_distance_from_outbound)
    print "index_minimum_current_outbound_city" + str(index_minimum_current_outbound_city)

    distances_from_inbound = self.distances_array[inward_index]
    print distances_from_inbound
    minimum_distance_from_inbound = 99999999999999
    index_minimum_current_inbound_city = 0
    print "minimum_distance_from_inbound" + str(minimum_distance_from_inbound)
    for i in range(len(self.cords)):
      if distances_from_inbound[i] < minimum_distance_from_inbound and distances_from_inbound[i] != 0 and self.degree_for_city_as_index[i] != 2:
        print "distances_from_inbound[i]" + str(distances_from_inbound[i])
        minimum_distance_from_inbound = distances_from_inbound[i]
        index_minimum_current_inbound_city=i
        print "minimum_distance_from_inbound" + str(minimum_distance_from_inbound)
    
    print "minimum_distance_from_inbound FINAL" + str(minimum_distance_from_inbound)
    print "index_minimum_current_inbound_city FINAL" + str(index_minimum_current_inbound_city)

    if index_minimum_current_outbound_city == inward_index and index_minimum_current_inbound_city == outward_index:
      index_minimum_current_distance_city = inward_index
      print "index_minimum_current_distance_city LAST!!" + str(index_minimum_current_distance_city)
    elif minimum_distance_from_outbound <= minimum_distance_from_inbound and index_minimum_current_outbound_city != inward_index:
      index_minimum_current_distance_city = index_minimum_current_outbound_city
      minimum_current_distance = minimum_distance_from_outbound
      self.degree_for_city_as_index[index_minimum_current_distance_city] += 1
      self.degree_for_city_as_index[outward_index] += 1
      self.outward_bound_current_city_index = index_minimum_current_distance_city
    elif index_minimum_current_inbound_city != outward_index:
      index_minimum_current_distance_city = index_minimum_current_inbound_city
      minimum_current_distance = minimum_distance_from_inbound
      self.degree_for_city_as_index[index_minimum_current_distance_city] += 1
      self.degree_for_city_as_index[inward_index] += 1
      self.inward_bound_current_city_index = index_minimum_current_distance_city
    
    print "index_minimum_current_distance_city" + str(index_minimum_current_distance_city)
    print "outward_bound_current_city_index" + str(self.outward_bound_current_city_index)
    print "inward_bound_current_city_index" + str(self.inward_bound_current_city_index)
    self.itinerary.append(index_minimum_current_distance_city)

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