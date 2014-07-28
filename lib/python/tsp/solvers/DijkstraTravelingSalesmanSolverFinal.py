import os, sys
lib_path = os.path.abspath('..')
sys.path.append(lib_path)

import Coordinate
import math
import TravelingSalesmanSolver
import LineOverlapEliminatorTravelingSalesmanSolver
from copy import deepcopy

class DijkstraSolver(LineOverlapEliminatorTravelingSalesmanSolver.LineOverlapEliminatorTravelingSalesmanSolver):

  def solve(self):
    for i in range(len(self.cords)):      
      pDone=float(i)/len(self.cords)
      self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
      self.checkTimeout(self)

      self.initialize_necessary_variables(i)
      self.distances_array = self.initialize_distances_array()
      while None in self.itinerary:
        self.add_nearest_city_to_head_or_tail()
      testDist = self.totalDistance()
      if (i == 0):
        self.bestitinerary = deepcopy(self.itinerary)
        self.bestSolution = self.totalDistance()
      elif (self.bestSolution > testDist):
        self.bestitinerary = deepcopy(self.itinerary)
        self.bestSolution = self.totalDistance()

    if self.REMOVE_LINE_CROSSES:
      self.bestOrder=self.bestitinerary
      self.removeLineCrosses()

    return ",".join([str(element) for element in self.bestitinerary])

  def totalDistance(self):
    itineraryDistance = 0.
    for i in range(len(self.itinerary) - 1):
      itineraryDistance += self.cords[self.itinerary[i]].dist(self.cords[self.itinerary[i + 1]])
    return itineraryDistance

  def add_nearest_city_to_head_or_tail(self):
    if self.itinerary.count(None) == 1:
      self.connect_head_to_tail()
    else:
      current_minimum_index, direction = self.get_lowest_legal_minimum_index_and_direction()
      self.update_itinerary_with_new_city(current_minimum_index, direction)

  def update_itinerary_with_new_city(self, min_index, direction):
    if direction == "in":
      self.add_new_city_to_incoming_path(min_index)
    else:
      self.add_new_city_to_outgoing_path(min_index)

  def add_new_city_to_incoming_path(self, min_index):
    index_for_insertion = (self.itinerary[::-1].index(None) + 1) * -1
    self.itinerary[index_for_insertion] = min_index

  def add_new_city_to_outgoing_path(self, min_index):
    index_for_insertion = self.itinerary.index(None)
    self.itinerary[index_for_insertion] = min_index


  def get_lowest_legal_minimum_index_and_direction(self):
    outgoing_distances = deepcopy(self.distances_array[self.outgoing_tip_index])
    incoming_distances = deepcopy(self.distances_array[self.incoming_tip_index])
    legal_found = False
    return self.search_for_legal_moves(incoming_distances,outgoing_distances,legal_found)

  def get_minimums_for_current_cities(self, incoming_distances, outgoing_distances):
    lowest_in = min([d for d in incoming_distances if d != 0])
    lowest_out = min([d for d in outgoing_distances if d != 0])
    return lowest_in, lowest_out

  def set_lowest_index(self, lowest_in, lowest_out, incoming_distances, outgoing_distances):
    if lowest_in <= lowest_out:
      return incoming_distances.index(lowest_in)
    else:
      return outgoing_distances.index(lowest_out)


  def search_for_legal_moves(self, incoming_distances, outgoing_distances, legal_found):
    while legal_found == False:
      lowest_in, lowest_out = self.get_minimums_for_current_cities(incoming_distances, outgoing_distances)
      lowest_index = self.set_lowest_index(lowest_in, lowest_out, incoming_distances, outgoing_distances)

      if self.is_legal(lowest_index):
        legal_found = True
        return self.update_variables_and_return_index_and_direction(lowest_in, lowest_out, lowest_index)

      else:
        incoming_distances, outgoing_distances = self.ignore_illegal_city(lowest_in,lowest_out,incoming_distances,outgoing_distances,lowest_index)

  def ignore_illegal_city(self, lowest_in, lowest_out, incoming_distances, outgoing_distances, lowest_index):
    if lowest_in <= lowest_out:
      incoming_distances[lowest_index] = 0
    else:
      outgoing_distances[lowest_index] = 0
    return incoming_distances, outgoing_distances

  def update_variables_and_return_index_and_direction(self, lowest_in, lowest_out, lowest_index):
    if lowest_in <= lowest_out:
      self.update_tracking_variables(lowest_index, "in")
      return lowest_index, "in"
    else:
      self.update_tracking_variables(lowest_index, "out")
      return lowest_index, "out"

  def update_tracking_variables(self, index, direction):
    self.degree_per_city[index] += 1
    if direction == "in":
      self.degree_per_city[self.incoming_tip_index] += 1
      self.incoming_tip_index = index
    else:
      self.degree_per_city[self.outgoing_tip_index] += 1
      self.outgoing_tip_index = index

  def is_legal(self, lowest_index):
    if (self.degree_per_city[lowest_index] != 2):
      if (self.incoming_tip_index != lowest_index) and (self.outgoing_tip_index != lowest_index):
        return True
    return False

  def connect_head_to_tail(self):
    index_for_insertion = self.itinerary.index(None)
    for k in range(self.path_length):
      if k not in self.itinerary:
        self.itinerary[index_for_insertion] = k

  def initialize_necessary_variables(self,i):
    self.path_length = len(self.cords)
    self.itinerary = [i] + [None]*(self.path_length - 1)
    self.degree_per_city = [0]*self.path_length
    self.outgoing_tip_index = i
    self.incoming_tip_index = i

  def initialize_distances_array(self):
    distances_per_city = []
    for j in self.cords:
      current_city_list = []
      for k in self.cords:
        current_city_list.append(j.dist(k))
      distances_per_city.append(current_city_list)
    return distances_per_city

#dijkstra = DijkstraSolver()

#dijkstra.cords.append(Coordinate.Coordinate(90,20))
#dijkstra.cords.append(Coordinate.Coordinate(21,34))#
#dijkstra.cords.append(Coordinate.Coordinate(34,56))
#dijkstra.cords.append(Coordinate.Coordinate(28,50))
#dijkstra.cords.append(Coordinate.Coordinate(51,80))
#dijkstra.cords.append(Coordinate.Coordinate(68,72))
#dijkstra.cords.append(Coordinate.Coordinate(40,72))
#dijkstra.cords.append(Coordinate.Coordinate(68,100))
#dijkstra.cords.append(Coordinate.Coordinate(25,50))


#solution = dijkstra.solve()

#print solution
