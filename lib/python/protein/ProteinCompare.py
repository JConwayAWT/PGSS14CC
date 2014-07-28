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

import random
import os
import sys
from solvers import ExampleSolver as e
from solvers import SlitheringSnakeSolver as ss
from solvers import alpha_beta_solver as ab
from solvers import alpha_beta_solver_3d as ab3d
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

percent_h = .5
length = 50
string = generateRandomString(length,percent_h)
print string
solver = ss.SlitheringSnakeSolver(string)
solution = solver.solve()
print getPotentialEnergy(solution)

solver = ab.alpha_beta(string)
solution = solver.solve()
print getPotentialEnergy(solution)

solver = ab3d.alpha_beta_3d(string)
solution = solver.solve()
print getPotentialEnergy(solution)
