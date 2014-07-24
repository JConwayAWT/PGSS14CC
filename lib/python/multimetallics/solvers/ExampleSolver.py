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
import json
from NanoClass import genParticle
from ase.md.nvtberendsen import NVTBerendsen
from ase import units 

class ExampleSolver(MetalicsSolver.MetalicFoldingSolver):

  def solve(self):
    #Create the initial particle from the defining string/number atoms
    self.particle = genParticle(self.definingString,int(self.numberOfAtoms))

    # self.definingString looks like: "Pt50Au30"
    #print "my defining string is " + self.definingString

    # self.numberOfAtoms looks like: "80" (you'll need to call int(self.numberOfAtoms))
    #print "my number of atoms is " + self.numberOfAtoms

    #do all of your solving stuff you want...

    #FINAL_SOLUTION = IMPLEMENT_FINAL_SOLUTION()

    a = {"symbol": "Pt", "x": 1, "y": 2, "z": 3}
    b = {"symbol": "Au", "x": 2, "y": 1, "z": -2}
    c = {"symbol": "Pt", "x": 1, "y": 1, "z": -2}
    listOfAtoms = [a, b, c]
    potentialEnergy = -325.43
    dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": potentialEnergy}
    actually_json = json.dumps(dictionary_to_be_turned_into_json)

    # this gets returned to the parent class and shoved into the database as a string, then
    # parsed as JSON on the page and displayed/drawn for the user
    return actually_json
