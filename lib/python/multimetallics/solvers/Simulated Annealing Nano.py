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
from ase.optimize import FIRE
from copy import deepcopy
from ase import Atoms
import random

class simulatedAnnealingNano(MetalicsSolver.MetalicFoldingSolver):

    def solve(self):
    #Create the initial particle from the defining string/number atoms

        temp = 3000
        self.particle = genParticle(self.definingString,int(self.numberOfAtoms))
        self.bestEnergy = self.particle.get_potential_energy()
        self.bestParticle = copy(self.particle)
        berendsen = NVTBerendsen(self.particle, 0.1 * units.fs, temp, taut=0.5*1000*units.fs)

        while temp > 0:
            berendsen.run(temp)
            testEnergy = self.particle.get_potential_energy()
            if (testEnergy < self.bestEnergy):
        	self.bestEnergy = testEnergy
        	self.bestParticle = copy(self.particle)
            temp -= 10

        for atom in self.bestParticle:
                dictElement = {"symbol":atom.symbol,"x":atom.position[0],"y":atom.position[1],"z":atom.position[2]}
        potentialEnergy = self.bestEnergy
        dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": potentialEnergy}
        actually_json = json.dumps(dictionary_to_be_turned_into_json)

            # this gets returned to the parent class and shoved into the database as a string, then
            # parsed as JSON on the page and displayed/drawn for the user
        return actually_json

