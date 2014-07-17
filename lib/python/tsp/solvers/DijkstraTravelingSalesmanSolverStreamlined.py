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
    return ",".join(str(self.itinerary[i]) for i in range(len(self.itinerary)))

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
    # minimum_distance_from_outbound = min(distance for distance in distances_from_outbound if distance > 0)
    # minimum_distance_from_inbound = min(distance for distance in distances_from_inbound if distance > 0) 
    # index_minimum_current_outbound_city = distances_from_outbound.index(minimum_distance_from_outbound)
    # index_minimum_current_inbound_city = distances_from_outbound.index(minimum_distance_from_outbound)
    
    print "minimum_distance_from_inbound FINAL" + str(minimum_distance_from_inbound)
    print "index_minimum_current_inbound_city FINAL" + str(index_minimum_current_inbound_city)
    #choose the minimum distance city which meets the following criteria:
    # -- the distance is not 0 (don't travel to yourself)
    # -- the degree is not 2 (already has incoming/outgoing route)
    # -- we don't connect incoming and outgoing UNLESS this is the final move

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
    #
    # It may be more efficient to do a check such as this:
    # if ():
    #   index_minimum_current_distance_city = inward_index
    #   minimum_current_distance = minimum_distance_from_outbound
    #   self.degree_for_city_as_index[outward_index, inward_index] += 1
    #   connect_incoming_and_outgoing()
    # else:
    #   do_the_logic_from_above_except_for_the_last_line
    #
    # after choosing the next city:
    # -- update the degree of both cities involved
    # --- did this above
    # -- update the tip of whichever path is involved
    # --- did this above
    # -- update the itinerary
    self.itinerary.append(index_minimum_current_distance_city)
    # the return value should probably be the index of the city


  def initialize_distances_to_and_from_each_city(self):
    distances_per_city = []
    for j in self.cords:
      current_city_list = []
      for k in self.cords:
        current_city_list.append(j.dist(k))
      distances_per_city.append(current_city_list)
    return distances_per_city