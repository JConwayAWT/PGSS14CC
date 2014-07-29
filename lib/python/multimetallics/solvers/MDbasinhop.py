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
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.optimize import FIRE
from copy import deepcopy

class MDSolver(MetalicsSolver.MetalicFoldingSolver):

  def solve(self):

    #Create the initial particle from the defining string/number atoms
    self.particle = NanoClass.genParticle(self.definingString, int(self.numberOfAtoms))
    self.reCenter()
    self.bestEnergy = self.particle.get_potential_energy()
    self.bestParticle = deepcopy(self.particle)
    berendsen = NVTBerendsen(self.particle, 2.5 * units.fs, 1500, taut=0.5*1000*units.fs)
    dyn = FIRE(atoms=self.particle)
    MaxwellBoltzmannDistribution(self.particle,1500*units.kB)
    CALCULATIONS=100
    for i in range(CALCULATIONS):
      if i%1==0:
        pDone=float(i)/CALCULATIONS
        self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
        self.checkTimeout()
        self.setSolution(self.getAnswer())
      self.particle.rattle(stdev=0.1)
      MaxwellBoltzmannDistribution(self.particle,1500*units.kB)
      self.particle.get_potential_energy()
      berendsen.run(500)
      dyn.run()
      self.reCenter()
      testEnergy = self.particle.get_potential_energy()
      if (testEnergy < self.bestEnergy):
        self.bestEnergy = testEnergy
        self.bestParticle = deepcopy(self.particle)
      elif ((testEnergy +5.) > self.bestEnergy):
        self.particle = NanoClass.genParticle(self.definingString, int(self.numberOfAtoms))
        MaxwellBoltzmannDistribution(self.particle,1500*units.kB)
        self.particle.get_potential_energy()
        if (testEnergy < self.bestEnergy):
          self.bestEnergy = testEnergy
          self.bestParticle = deepcopy(self.particle)
    return self.getAnswer()

  def getAnswer(self):
    listOfAtoms = []
    for atom in self.bestParticle:
      dictElement = {"symbol":atom.symbol,"x":atom.position[0],"y":atom.position[1],"z":atom.position[2]}
      listOfAtoms.append(dictElement)
    potentialEnergy = self.bestEnergy
    dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": potentialEnergy}
    actually_json = json.dumps(dictionary_to_be_turned_into_json)
    return actually_json

  def reCenter(self):
    self.particle.center()
    self.particle.set_positions(self.particle.get_positions() - 200.)
