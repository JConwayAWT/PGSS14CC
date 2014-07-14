#-------------------------------------------------------------------------------
# Name:        Example solver
# Purpose:     Example solver
#
# Author:      Martin Schneider
#
# Created:     07/14/2014
# Copyright:   (c) Martin 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
import Coordinate
import math
import random
import copy

class ExampleSolver (ProteinFoldingSolver.ProteinFoldingSolver):
  def solve:
    #YOUR CODE HERE
    for c in range(len(self.cords)):
      print self.cords[c].x
      print self.cords[c].y
