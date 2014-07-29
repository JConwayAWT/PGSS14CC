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
from ase import visualize
from ase import io
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase import Atoms
from ase.optimize import FIRE, LBFGSLineSearch
from ase.calculators.emt import EMT
from copy import deepcopy
import heapq

class randomSolver(MetalicsSolver.MetalicFoldingSolver):

    def solve(self):
        self.particle = NanoClass.genParticle(self.definingString, int(self.numberOfAtoms))

        berendsen = NVTBerendsen(self.particle, 2.5 * units.fs, 3000, taut=0.5*1000*units.fs)
        dyn = FIRE(atoms=self.particle)
        MaxwellBoltzmannDistribution(self.particle,3000)
        berendsen.run(500)
        dyn.run()

        MAXIMUM_ITERATIONS = 50
        ITERATION = 0
        BEST_POTENTIAL_ENERGY = 99999999
        BEST_PARTICLE = None
        queue = [( self.particle.get_potential_energy(), self.particle)]
        while ITERATION < MAXIMUM_ITERATIONS:

          ITERATION += 1
          children = []
          best_child = heapq.heappop(queue)[1].copy()

          for k in range(5):
            child = self.make_new_child(best_child)

            print child.get_potential_energy()

            berendsen = NVTBerendsen(child, 2.5 * units.fs, 3000, taut=0.5*1000*units.fs)
            dyn = FIRE(atoms=child)
            MaxwellBoltzmannDistribution(child,3000)
            berendsen.run(500)
            dyn.run()

##            name_string = str(ITERATION) + "_child.png"
##            ase.io.write(child, name_string)



            print "Potential energy now = ", child.get_potential_energy()
            ase.visualize.view(child)

            if child.get_potential_energy() < BEST_POTENTIAL_ENERGY:
              print " -- new best found -- "
              BEST_POTENTIAL_ENERGY = child.get_potential_energy()
              BEST_PARTICLE = child

            heapq.heappush(queue, (child.get_potential_energy(), child))

    def make_new_child(self, best_child):
      new_child = best_child.copy()
      calc = EMT()
      new_child.set_calculator(calc)
      new_child.rattle(0.2, random.randint(0, 50))
      dyn = LBFGSLineSearch(atoms=new_child)
      dyn.run(steps=20000)
      dyn = FIRE(atoms=new_child)
      dyn.run(fmax=0.05)

      return new_child


d = {"definingString": "Pt15Au5", "numberOfAtoms": 20}
j = json.dumps(d)
solver = randomSolver(j)
solver.solve()