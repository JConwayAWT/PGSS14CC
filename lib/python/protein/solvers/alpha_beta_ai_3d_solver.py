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

class alpha_beta_ai_3d(ProteinChainClass3D.ProteinChain3D):
    def solve(self):
      bestEnergy = 999
      bestChain = []

      for a in range(1, 4):
        for b in range(1, 4):
          for c in range(1, 4):
            for d in range(1, 4):
              for e in range(1, 4):
                for f in range(1, 4):
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
                      scores_per_coordinate.append(self.get_score_of_single_coordinate(coordinate, [a, b, c, d, e, f]))

                    try:
                      scores_with_coordinates = [[scores_per_coordinate[k], test_coords[k]] for k in range(len(test_coords))]
                      scores_with_coordinates.sort()
                      R = random.random()
                      if R > 0.1:
                        self.chosen_coords.append(scores_with_coordinates[-1][1])
                      elif R > 0.05:
                        try: self.chosen_coords.append(scores_with_coordinates[-2][1])
                        except: self.chosen_coords.append(scores_with_coordinates[-1][1])
                      else:
                        try: self.chosen_coords.append(scores_with_coordinates[-3][1])
                        except: self.chosen_coords.append(scores_with_coordinates[-1][1])

                      current_chain_index += 1
                    except:
                      print "no possible neighbors..."
                      number_to_pop = random.gauss(6, 3)
                      number_to_pop = max(0, int(number_to_pop))
                      self.chosen_coords = self.chosen_coords[-1*number_to_pop:]
                      current_chain_index = len(self.chosen_coords)

                      ## TO DO : FIX THIS.  IT STILL GETS STUCK SOMETIMES.


                  self.setCoords(self.chosen_coords)
                  self.getEnergy()

                  if self.Energy < bestEnergy:
                    bestChain = copy.deepcopy(self.chosen_coords)
                    bestEnergy = copy.deepcopy(self.Energy)
                    print "NEW BEST!"
                    print bestEnergy, bestChain

      self.setCoords(bestChain)
      self.getEnergy()
      acids = []
      for i in range(len(bestChain)):
        acids.append({"type": self.amino_acid_chain[i], "x": bestChain[i][0], "y": bestChain[i][1], "z": bestChain[i][2]})
      dictionary_to_be_turned_into_json = {"potentialEnergy": bestEnergy, "acids": acids}
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
      p_value = 1
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


s = alpha_beta_ai_3d("HHHHPPPPHHHHPHHHPPPHHHHPPPHPHPHHHPPPPHHHHHH")
s.solve()

print s.chosen_coords
print s.Energy
