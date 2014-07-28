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
#import Coordinate
import math
import random
import copy
import json
from copy import deepcopy

class SlitheringSnakeSolver(ProteinChainClass.ProteinChain):

  def solve(self):
    moves = len(self.amino_acid_chain)*100
    self.bestEnergy = deepcopy(self.Energy)
    self.bestCords = deepcopy(self.cords)
    self.currentJson = self.formatSolution()
    self.setSolution(self.currentJson)
    for i in range(moves):
      self.singleMove()
      self.reCenter()
      #if (i % 100 == 0):
      #  print i
      if (self.Energy < self.bestEnergy):
        self.bestEnergy = deepcopy(self.Energy)
        self.bestCords = deepcopy(self.cords)
        self.currentJson = self.formatSolution()
        self.setSolution(self.currentJson)
      self.checkTimeout()
    return self.currentJson

  def singleMove(self):
    end_coord = deepcopy(self.coords[-1])
    test_coords = [[end_coord[0] + 1, end_coord[1]],[end_coord[0] - 1, end_coord[1]],[end_coord[0], end_coord[1] + 1],[end_coord[0], end_coord[1] - 1]]
    testtrapped = True
    while (len(test_coords) > 0):
      R = random.randint(0,len(test_coords) - 1)
      trial_move = test_coords.pop(R)
      if (trial_move not in self.coords):
        testtrapped = False
        break
    if (testtrapped == False):
      new_coords = deepcopy(self.coords)
      new_coords.pop(0)
      new_coords.append(trial_move)
      self.setCoords(new_coords)
    else:
      self.trappedCount += 1
      self.generateChainCoordinates()
      self.getEnergy()

  def reCenter(self):
    offset = deepcopy(self.coords[0])
    new_coords = deepcopy(self.coords)
    for coord in new_coords:
      coord[0] -= offset[0]
      coord[1] -= offset[1]
    self.setCoords(new_coords)
