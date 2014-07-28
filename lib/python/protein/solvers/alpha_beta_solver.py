import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import ProteinChainClass
#import Coordinate
import math
import random
import copy
import json
from copy import deepcopy

class alpha_beta(ProteinChainClass.ProteinChain):

    def solve(self):
      self.chosen_coords = []

      self.chosen_coords.append([0,0])

      current_chain_index = 1

      while len(self.chosen_coords) < len(self.amino_acid_chain): ##keep going until all AAs are used
        current_amino_acid = self.amino_acid_chain[current_chain_index] #gives us "H" or "P"
        location_of_previous_acid = self.chosen_coords[current_chain_index-1]
        test_coords = [[location_of_previous_acid[0] + 1, location_of_previous_acid[1]],[location_of_previous_acid[0] - 1, location_of_previous_acid[1]],[location_of_previous_acid[0], location_of_previous_acid[1] + 1],[location_of_previous_acid[0], location_of_previous_acid[1] - 1]]
        test_coords = self.remove_filled_positions(test_coords)

        scores_per_coordinate = []

        for coordinate in test_coords:
          scores_per_coordinate.append(self.get_score_of_single_coordinate(coordinate, 9, 3, 1))

        maximum_score = max(scores_per_coordinate)
        maximum_score_index = scores_per_coordinate.index(maximum_score)
        maximum_coordinate = test_coords[maximum_score_index]

        self.chosen_coords.append(maximum_coordinate)

        current_chain_index += 1

      acids = []
      self.getEnergy()
      for i in range(len(self.chosen_coords)):
        acids.append({"type": self.amino_acid_chain[i], "x": self.chosen_coords[i][0], "y": self.chosen_coords[i][1]})
      dictionary_to_be_turned_into_json = {"potentialEnergy": self.Energy, "acids": acids}
      actually_json = json.dumps(dictionary_to_be_turned_into_json)
      return actually_json




    def get_score_of_single_coordinate(self, coordinate, adjacent_value, diagonal_value, twice_removed_value):
      total_score = 0
      h_value = 4
      p_value = 0
      neighbor_locations = [[coordinate[0] + 1, coordinate[1]],[coordinate[0] - 1, coordinate[1]],[coordinate[0], coordinate[1] + 1],[coordinate[0], coordinate[1] - 1]]
      diagonal_locations = [[coordinate[0] + 1, coordinate[1] + 1],[coordinate[0] - 1, coordinate[1] - 1],[coordinate[0] - 1, coordinate[1] + 1],[coordinate[0] + 1, coordinate[1] - 1]]
      twice_removed_neighbors = self.get_twice_removed_neighbors(coordinate)
      for possible_neighbor in neighbor_locations:
        h_points, p_points = 0, 0
        if possible_neighbor in self.chosen_coords:
          index_of_neighbor = self.chosen_coords.index(possible_neighbor)
          polarity_of_neighbor = self.amino_acid_chain[index_of_neighbor]
          if polarity_of_neighbor == "H":
            h_points += h_value*adjacent_value #3 for touching, 1 for diagonal... (NYI)
          else: #that means it's "P"
            p_points += p_value*adjacent_value #3 for touching, 1 for diagonal... (NYI)
        total_score += h_points + p_points
      for diagonal_neighbor in diagonal_locations:
        h_points, p_points = 0, 0
        if diagonal_neighbor in self.chosen_coords:
          index_of_neighbor = self.chosen_coords.index(diagonal_neighbor)
          polarity_of_neighbor = self.amino_acid_chain[index_of_neighbor]
          if polarity_of_neighbor == "H":
            h_points += h_value*diagonal_value
          else:
            p_points += p_value*diagonal_value
        total_score += h_points + p_points
      for twice_removed_neighbor in twice_removed_neighbors:
        h_points, p_points = 0, 0
        if twice_removed_neighbor in self.chosen_coords:
          index_of_neighbor = self.chosen_coords.index(twice_removed_neighbor)
          polarity_of_neighbor = self.amino_acid_chain[index_of_neighbor]
          if polarity_of_neighbor == "H":
            h_points += h_value*twice_removed_value
          else:
            p_points += p_value*twice_removed_value
        total_score += h_points + p_points

      return total_score


    def get_twice_removed_neighbors(self, coordinate):
      x = coordinate[0]
      y = coordinate[1]
      neighbor_coordinates = []
      for x_value in range(-2, 3):
        neighbor_coordinates.append([x + x_value, y + 2])
        neighbor_coordinates.append([x + x_value, y - 2])
      for y_value in range(-2, 3):
        neighbor_coordinates.append([x + 2, y + y_value])
        neighbor_coordinates.append([x - 2, y + y_value])
      non_duplicated_neighbors = []
      for neighbor in neighbor_coordinates:
        if neighbor not in non_duplicated_neighbors:
          non_duplicated_neighbors.append(neighbor)
      return non_duplicated_neighbors


    def remove_filled_positions(self, test_coordinates):
      legal_coords = []
      for coordinate in test_coordinates:
        if coordinate not in self.chosen_coords:
          legal_coords.append(coordinate)
      return legal_coords

    def find_corner(self, chosen_coords):
        corners = []
        current_amino_acid = self.amino_acid_chain[current_chain_index] #gives us "H" or "P"
        location_of_previous_acid = self.chosen_coords[current_chain_index-1]
        location_of_next_acid = self.chosen_coords[current_chain_index+1]
        if location_of_previous_acid[0] != location_of_next_acid[0] and location_of_previous_acid[1]!= location_of_next_acid[1]:
            corners.append(current_amino_acid)

    def change_corner(self, corners):
        potential_paths = []
        for current_corner in range(corners()):
            possible_paths.append(current_corner)#original path
            possible_paths = [[current_corner[0] + 1, current_corner[1]],[current_corner[0] - 1, current_corner[1]],[current_corner[0], current_corner[1] + 1],[current_corner[0], current_corner[1] - 1]]
            possible_paths = self.remove_filled_positions(possible_paths)
            for coordinate in chosen_coords:
                if chosen_coords.index(coordinate) > chosen_coords.index(current_corner):
                    chosen_coords.pop(coordinate)
            for i in range(len(self.possible_paths)):
                chosen_coords.append(possible_paths[i])
                #FIX NEEDED: solve, only calculating potential energy
                self.getEnergy()
                potential_energy_per_path = []
                potential_energy_per_path.append(self.Energy)

                minimum_energy = min(potential_energy_per_path)
                minimum_energy_index = potential_energy_per_path.index(minimum_energy)
                minimum_path = possible_paths[minimum_energy_index]

                print minimum_path

                #current_chain_index += 1



s = alpha_beta("HHHHHHHHHHHHHHHHHHHHHHHHHH")
s.solve()

print s.chosen_coords
