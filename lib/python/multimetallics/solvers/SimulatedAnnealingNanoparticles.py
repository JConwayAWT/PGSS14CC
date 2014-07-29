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
from ase.md.langevin import Langevin
from ase import units
from ase.optimize import FIRE
from copy import deepcopy
from ase import Atoms
import random
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

class simulatedAnnealingNano(MetalicsSolver.MetalicFoldingSolver):

    def solve(self):
    #Create the initial particle from the defining string/number atoms

        temp = 1500
        maxtemp = temp
        mintemp = 150
        self.particle = genParticle(self.definingString,int(self.numberOfAtoms))
#        self.bestEnergy = self.particle.get_potential_energy()
#        self.bestParticle = copy.copy(self.particle)
        berendsen = Langevin(self.particle, 2.5 * units.fs, units.kB * temp, 0.02)
        # the 5.0 * units.fs is used instead of 0.1 * units.fs b/c it makes the program run faster
        MaxwellBoltzmannDistribution(self.particle,units.kB * temp)
        self.bestEnergy = self.particle.get_potential_energy()
        self.bestParticle = deepcopy(self.particle)
        self.reCenter()
        self.getAnswer()

        while (temp > mintemp):
            berendsen = Langevin(self.particle, 2.5 * units.fs, units.kB * temp, 0.02)
            berendsen.run(100)
            testEnergy = self.particle.get_potential_energy()
            self.bestEnergy = self.particle.get_potential_energy()
            self.bestParticle = deepcopy(self.particle)
            self.reCenter()
            self.getAnswer()
            temp -= 10
            if (temp % 50 == 0):
              self.bestEnergy = self.particle.get_potential_energy()
              self.bestParticle = deepcopy(self.particle)
              self.reCenter()
              self.checkTimeout()
              self.setSolution(self.getAnswer())
              pDone=float(maxtemp - temp)/(maxtemp-mintemp)
              self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
            elif (temp <= mintemp):
              dyn = FIRE(atoms=self.particle)
              dyn.run(fmax=0.01)
              self.bestEnergy = self.particle.get_potential_energy()
              self.bestParticle = deepcopy(self.particle)
              self.reCenter()
              self.setSolution(self.getAnswer())
              pDone=float(temp)/(maxtemp-mintemp)
              self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))

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