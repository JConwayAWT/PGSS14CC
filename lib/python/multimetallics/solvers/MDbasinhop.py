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
import NanoClass
import ase
import os
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.optimize import FIRE
from copy import deepcopy

class MDSolver(MetalicsSolver.MetalicFoldingSolver):

  def solve(self):
    #Create the initial particle from the defining string/number atoms

    #self.particle = NanoClass.genParticle(self.definingString,int(self.numberOfAtoms))
    self.particle = NanoClass.genParticle(self.definingString, int(self.numberOfAtoms))
    self.bestEnergy = self.particle.get_potential_energy()
    self.bestParticle = deepcopy(self.particle)
    berendsen = NVTBerendsen(self.particle, 2.5 * units.fs, 5000, taut=0.5*1000*units.fs)
    dyn = FIRE(atoms=self.particle)
    MaxwellBoltzmannDistribution(self.particle,5000)
    for i in range(1):
      self.particle.rattle(stdev=0.1)
      berendsen.run(500)
      dyn.run()
      self.reCenter()
      testEnergy = self.particle.get_potential_energy()
      if (testEnergy < self.bestEnergy):
        self.bestEnergy = testEnergy
        self.bestParticle = deepcopy(self.particle)
    listOfAtoms = []
    for atom in self.bestParticle:
      dictElement = {"symbol":atom.symbol,"x":atom.position[0],"y":atom.position[1],"z":atom.position[2]}
      listOfAtoms.append(dictElement)
    potentialEnergy = self.bestEnergy
    dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": potentialEnergy}
    actually_json = json.dumps(dictionary_to_be_turned_into_json)

    # this gets returned to the parent class and shoved into the database as a string, then
    # parsed as JSON on the page and displayed/drawn for the user
    return actually_json

  def reCenter(self):
    self.particle.center()
    self.particle.set_positions(self.particle.get_positions() - 200.)
