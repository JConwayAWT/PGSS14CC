#-------------------------------------------------------------------------------
# Name:        Protein Comparison Program
# Purpose:     Compares properties of protein folding solutions
#
# Author:      Ishan Levy
#
# Created:     07/28/2014
# Copyright:   (c) Ishan 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------


import os, sys
lib_path = os.path.abspath('../helpers')
sys.path.append(lib_path)

lib_path = os.path.abspath('../database')
sys.path.append(lib_path)

import time
import random

from solvers import ExampleSolver as e
from solvers import MetalicsSolver as ms
from solvers import MDbasinhop as md
from solvers import SimulatedAnnealingNanoparticles as san
from solvers import standard_basin_hopping as sbh
from solvers import GeneticAlgorithmSolver as gas

def main():
  minPoints = 10
  maxPoints = 1500
  pointInterval = 6
  iteration = 1

  n = open('nul','w')
  sys.stdout=n

  output=""

  for points in xrange(minPoints,maxPoints,pointInterval):
      output+=str(points) + "\n\r"
      distances = [0,0,0,0,0,0,0,0,0,0,0]
      times =[0,0,0,0,0,0,0,0,0]
      for iterations in xrange(iteration):

        solver = []
        #solver.append(md.MDSolver()) WE NEVER RAN A TEST CASE WITH THIS
        #solver.append(san.simulatedAnnealingNano()) THIS WAS INCLUDED IN THE FIRST FOUR POINTS
        solver.append(sbh.randomSolver())
        solver.append(gas.GeneticSolver())

        for solves in xrange(len(solver)):
            solver[solves].numberOfAtoms = points
            string = "Al" + str(points/2) + "Ni" + str(points/2)
            solver[solves].definingString = string
            timer = time.time()
            solution = solver[solves].solve()
            timer = time.time()-timer
            times[solves] += timer
            distances[solves] += solver[solves].bestEnergy
            print"a",str(points)
      for solves in xrange(len(solver)):
        output+=str(times[solves]/iteration) + "\n\r"
        output+=str(distances[solves]/iteration) + "\n\r"
        f = open("output.txt", "w")
        #if points % 4 == 2:
#            f = open("output.txt", "w")
#        else:
#            f = open("output1.txt", "w")
        f.write(output)
        f.close()
main()
