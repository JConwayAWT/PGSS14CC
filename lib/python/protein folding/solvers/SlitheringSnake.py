#-------------------------------------------------------------------------------
# Name:        slithering snake protein folding solver
# Purpose:     solves the HP protein folding model with slithering snake
#
# Author:      Zachary Pozun
#
# Created:     07/21/2014
# Copyright:   (c) ZDP 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import ProteinChainClass
import Coordinate
import math
import random
import copy
from copy import deepcopy

class SlitheringSnakeSolver(ProteinChainClass.ProteinChain):

  def solve(self,moves):
    self.bestEnergy = deepcopy(self.Energy)
    self.bestCords = deepcopy(self.cords)
    for i in range(moves):
      print i
      self.singleMove()
      if (self.Energy < self.bestEnergy):
        self.bestEnergy = deepcopy(self.Energy)
        self.bestCords = deepcopy(self.cords)

  def singleMove(self):
    end_coord = self.coords[-1]
    test_coords = [[end_coord[0] + 1, end_coord[1]],[end_coord[0] - 1, end_coord[1]],[end_coord[0], end_coord[1] + 1],[end_coord[0], end_coord[1] - 1]]
    trapped = True
    while (len(test_coords) > 0):
      R = random.randint(0,len(test_coords) - 1)
      trial_move = test_coords.pop(R)
      if (trial_move not in self.coords):
        trapped = False
        break
    if (trapped == False):
      new_coords = deepcopy(self.coords)
      new_coords.pop(0)
      new_coords.append(trial_move)
      self.setCoords(new_coords)
    else:
      self.generateChainCoordinates()
      self.generateChainAminoAcids()
      self.getEnergy()
