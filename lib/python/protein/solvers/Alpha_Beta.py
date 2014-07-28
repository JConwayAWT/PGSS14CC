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

class Alpha_Beta(ProteinChainClass.ProteinChain):
    print "This code has started"
    def solve(self, amino_acid_chain):#(self, coordinates)
    # the input should look like: 'PHHPHHHPPHHHPHPHPPPHHHPHPHPHPHP'
        #place second amino acid
        hPoints = 0
        pPoints = 0
        sumPoints = 0
        valueH = 3
        valueP = 1

        self.chosen_coords = [[0,0]]
        for m in range(len(self.amino_acid_chain)):
            end_coord = deepcopy(self.chosen_coords[-1])
            test_coords = [[end_coord[0] + 1, end_coord[1]],[end_coord[0] - 1, end_coord[1]],[end_coord[0], end_coord[1] + 1],[end_coord[0], end_coord[1] - 1]]
            #^list of possible coords to choose from
            n = 0
            while n < len(test_coords):
                if test_coords[n] in self.chosen_coords:#if the space is filled
                    test_coords.pop(n)
                n = n+1
            #made a list of possible empty coordinates

            n = 0 #resetting increment
            #adjacent point system
            i = 0 #making new increment to test each possible empty space
            evaluated_coord = test_coords[i]
            coord_points = []#new list of points whose indices match up with those of test_coords
            while i < len(test_coords):
                test_evaluated_coords = [[evaluated_coord[0] + 1, evaluated_coord[1]],[evaluated_coord[0] - 1, evaluated_coord[1]],[evaluated_coord[0], evaluated_coord[1] + 1],[evaluated_coord[0], evaluated_coord[1] - 1]]
                #^looking at each location-neighbor of each test_coord

                while n < 4:
                    if test_evaluated_coords[n] in self.chosen_coords:
                        #if this possible coord has location-neighbors
                        if amino_acid_chain[self.chosen_coords.index(test_evaluated_coords[n])-1] == "H":
                            hPoints += 3*valueH
                        else: #must be polar
                            pPoints += 3*valueP
                        sumPoints = hPoints + pPoints
                        coord_points.append(sumPoints)
                    n = n+1
                i = i +1

            maximum_score = max(coord_points)
            maximum_score_index = coord_points.index(maximum_score)
            maximum_coordinate = test_coords[maximum_score_index]


            self.chosen_coords.append(maximum_coordinate)


s = Alpha_Beta("PPHHHPPHHPHPHPHH")
s.solve("PPPHHHPPHHPHPHP")

print s.chosen_coords
