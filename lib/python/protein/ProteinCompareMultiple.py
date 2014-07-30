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
import os
import sys
from solvers import ExampleSolver as e
from solvers import SlitheringSnakeSolver as ss
from solvers import alpha_beta_solver as ab
from solvers import alpha_beta_solver_3d as ab3d
from solvers import alpha_beta_ai_3d_solver as abai3d
def getPotentialEnergy(solution):
    continuing = True
    i = len(solution) - 1
    while (i >= 0 and continuing):
        if solution[i] == ' ':
            continuing = False
        else:
            i -= 1
    return float(solution[i:len(solution)-1])

def generateRandomString(length, percent_h):
    ph = float(percent_h)
    hs = 0
    string = ""
    for i in xrange(length):
        rand = random.random()
        if rand <= float(length*ph - hs)/float(length - i):
            string += "H"
            hs += 1
        else:
            string += "P"
    return string

def main():
  minPoints = 10
  maxPoints = 300
  pointInterval = 5
  iteration = 2
  for points in xrange(minPoints,maxPoints,pointInterval):
      print points
      distances = [0,0,0,0,0,0,0,0,0,0,0]
      times =[0,0,0,0,0,0,0,0,0]
      for iterations in xrange(iteration):
        string = generateRandomString(points,50)


        solver = []
        solver.append(ab3d.alpha_beta_3d(string))
        solver.append(ab.alpha_beta(string))
        solver.append(ss.SlitheringSnakeSolver(string))
        #solver.append(abai3d.alpha_beta_ai_3d(string))

        for solves in xrange(len(solver)):
            timer = time.time()
            solution = solver[solves].solve()
            timer = time.time()-timer
            times[solves] += timer
            distances[solves] += getPotentialEnergy(solution)
           # print"a"
      for solves in xrange(len(solver)):
        print times[solves]/iteration
        print distances[solves]/iteration
main()
