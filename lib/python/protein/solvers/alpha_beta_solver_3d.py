import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import ProteinChainClass3D
#import Coordinate
import math
import random
import copy
import json
from copy import deepcopy

class alpha_beta_3d(ProteinChainClass3D.ProteinChain3D):
    def solve(self):
      self.chosen_coords = []

      self.chosen_coords.append([0,0,0])

      current_chain_index = 1

      while len(self.chosen_coords) < len(self.amino_acid_chain): ##keep going until all AAs are used
        current_amino_acid = self.amino_acid_chain[current_chain_index] #gives us "H" or "P"
        location_of_previous_acid = self.chosen_coords[current_chain_index-1]
        test_coords = self.get_hops_at_distance(1, location_of_previous_acid)
        test_coords = self.remove_filled_positions(test_coords)

        scores_per_coordinate = []

        for coordinate in test_coords:
          scores_per_coordinate.append(self.get_score_of_single_coordinate(coordinate, [32, 16, 8, 4, 2, 1]))

        maximum_score = max(scores_per_coordinate)
        maximum_score_index = scores_per_coordinate.index(maximum_score)
        maximum_coordinate = test_coords[maximum_score_index]

        self.chosen_coords.append(maximum_coordinate)

        current_chain_index += 1

      acids = []

      self.setCoords(self.chosen_coords)
      self.getEnergy()
      for i in range(len(self.chosen_coords)):
        acids.append({"type": self.amino_acid_chain[i], "x": self.chosen_coords[i][0], "y": self.chosen_coords[i][1], "z": self.chosen_coords[i][2]})
      dictionary_to_be_turned_into_json = {"potentialEnergy": self.Energy, "acids": acids}
      actually_json = json.dumps(dictionary_to_be_turned_into_json)
      return actually_json


    def get_hops_at_distance(self, desired_distance, coordinate):
      x = coordinate[0]
      y = coordinate[1]
      z = coordinate[2]
      possible_points = []
      legal_points = []
      for a in range(-2, 3):
        for b in range(-2, 3):
          for c in range(-2, 3):
            possible_points.append([x + a, b + y, z + c])
      for point in possible_points:
        if self.manhattan_distance(point, coordinate) == desired_distance:
          legal_points.append(point)
      return legal_points



    def get_score_of_single_coordinate(self, coordinate, values_at_hop_distance):
      total_score = 0
      h_value = 4
      p_value = 0
      coordinates_for_neighbords_with_manhattan_distance_of_index = [None]
      for k in range(1, 7):
        coordinates_for_neighbords_with_manhattan_distance_of_index.append(self.get_hops_at_distance(k, coordinate))

      hop_index = 0
      for list_of_neighbors in coordinates_for_neighbords_with_manhattan_distance_of_index[1:]:
        if list_of_neighbors == []:
          pass #nothing to do, so sad.
        else:
          for possible_neighbor in list_of_neighbors:
            h_points, p_points = 0, 0
            if possible_neighbor in self.chosen_coords:
              index_of_neighbor = self.chosen_coords.index(possible_neighbor)
              polarity_of_neighbor = self.amino_acid_chain[index_of_neighbor]
              if polarity_of_neighbor == "H":
                h_points += h_value*values_at_hop_distance[hop_index] #3 for touching, 1 for diagonal... (NYI)
              else: #that means it's "P"
                p_points += p_value*values_at_hop_distance[hop_index] #3 for touching, 1 for diagonal... (NYI)
            total_score += h_points + p_points
        hop_index += 1

      return total_score


    def manhattan_distance(self, start, finish):
      distance = 0
      for k in range(len(start)):
        distance += abs(start[k] - finish[k])
      return distance

    def remove_filled_positions(self, test_coordinates):
      legal_coords = []
      for coordinate in test_coordinates:
        if coordinate not in self.chosen_coords:
          legal_coords.append(coordinate)
      return legal_coords


##s = alpha_beta_3d("HHHHPHHPHPHPPPHPPHPPPPPHHHHHPHPHPHHPPPPHHHHHH")
##s.solve()
##
##print s.chosen_coords
##print s.Energy
