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

class ExampleSolver(ProteinFoldingSolver.ProteinFoldingSolver):

  def solve(self):
  	return "Lol im a metal"