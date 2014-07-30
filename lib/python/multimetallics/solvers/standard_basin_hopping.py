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
from heapq import *
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.optimize import FIRE, LBFGSLineSearch

class randomSolver(MetalicsSolver.MetalicFoldingSolver):

    def solve(self):
        self.setStatusDone("Initializing configuration...")
        self.particle = NanoClass.genParticle(self.definingString, int(self.numberOfAtoms))
        self.reCenter()
        self.bestEnergy = self.particle.get_potential_energy()
        self.bestParticle = self.particle.copy()


        berendsen = Langevin(self.particle, 5*units.fs, units.kB*2000,0.005)
        dyn = FIRE(atoms=self.particle)
        dyn.run(500)
        MaxwellBoltzmannDistribution(self.particle,2000*units.kB)

        MAXIMUM_ITERATIONS = 20
        ITERATION = 0
        BEST_POTENTIAL_ENERGY = 999999
        BEST_PARTICLE = None
        queue = [( self.particle.get_potential_energy(), self.particle)]

        pDone=float(ITERATION)/MAXIMUM_ITERATIONS
        self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
        self.checkTimeout()
        current_particle = self.bestParticle.copy()
        calc = EMT()
        current_particle.set_calculator(calc)
        self.setSolution(self.getAnswer(current_particle, current_particle.get_potential_energy()))

        while ITERATION < MAXIMUM_ITERATIONS:


          new_parent = heappop(queue)[1].copy()
          calc = EMT()
          new_parent.set_calculator(calc)
          print new_parent.get_positions()
          print new_parent.get_potential_energy()

          for x in range(5):
            new_child = self.create_child_from(new_parent)

            potential_energy = copy.deepcopy(new_child.get_potential_energy())
            heappush(queue, (potential_energy, new_child))

            if potential_energy < BEST_POTENTIAL_ENERGY:
              print "--------------- NEW BEST FOUND ---------------"
              print "POTENTIAL ENERGY = ", potential_energy
              BEST_POTENTIAL_ENERGY = potential_energy
              self.bestParticle = new_child
              print new_child.positions

          pDone=float(ITERATION)/MAXIMUM_ITERATIONS
          self.setStatusDone(str(math.floor(pDone*100))+"% | "+self.remainingTime(pDone))
          self.checkTimeout()
          self.setSolution(self.getAnswer(self.bestParticle, BEST_POTENTIAL_ENERGY))

          ITERATION += 1

        return self.getAnswer(self.bestParticle, BEST_POTENTIAL_ENERGY)


    def create_child_from(self, parent):
      child = parent.copy()
      calc = EMT()
      child.set_calculator(calc)
      if (random.random() > 0.25):
        child.rattle(0.02, random.randint(0, 50))
      else:
        child.rattle(0.2, random.randint(0, 50))
      dyn = LBFGSLineSearch(atoms=child)
      dyn.run(steps=20000)
      dyn = FIRE(atoms=child)
      dyn.run(fmax=0.05)

      return child


    def getAnswer(self, particle, energy):
      listOfAtoms = []
      for atom in particle:
        dictElement = {"symbol":atom.symbol,"x":atom.position[0],"y":atom.position[1],"z":atom.position[2]}
        listOfAtoms.append(dictElement)
      dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": energy}
      actually_json = json.dumps(dictionary_to_be_turned_into_json)
      return actually_json

    def reCenter(self):
      self.particle.center()
      self.particle.set_positions(self.particle.get_positions() - 200.)

# d = {"definingString": "Pt50Au50", "numberOfAtoms": 100}
# j = json.dumps(d)
# solver = randomSolver(j)
# solver.solve()