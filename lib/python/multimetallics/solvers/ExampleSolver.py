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
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
import math
import MetalicsSolver
import random
import copy

class ExampleSolver(MetalicsSolver.MetalicFoldingSolver):

  def solve(self):
    print "I have " + str(len(self.atoms)) + " atoms."
    for k in range(len(self.atoms)):
      print "Atom " + str(k) + " has symbol " + self.atoms[k]["symbol"]
    return "I'm a metal lol"

##e = ExampleSolver('{"atoms": [{"x": 1, "y": 2, "z": 3, "symbol": "Pt"},{"x": 5, "y": 1, "z": 3, "symbol": "Pt"},{"x": 3, "y": 10, "z": 1, "symbol": "Au"}], "algorithm": "Basin Hopping"}')
##e.solve()

