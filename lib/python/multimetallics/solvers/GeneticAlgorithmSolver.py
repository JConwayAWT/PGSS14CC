#-------------------------------------------------------------------------------
# Name:        Genetic Algorithm Solver
# Purpose:     Multimetallic Nanoparticles
#
# Author:      Narahari Bharadwaj
#
# Created:     07/24/2014
# Copyright:   (c) Narahari 2014
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
import heapq
from NanoClass import genParticle
from ase.md.nvtberendsen import NVTBerendsen
from ase import units

class GeneticSolver(MetalicsSolver.MetalicFoldingSolver):

  def solve(self):
    #Create the initial particle from the defining string/number atoms
    self.particle = genParticle("Pt50Au30", 80)

    # self.definingString looks like: "Pt50Au30"
    print "my defining string is " + self.definingString

    # self.numberOfAtoms looks like: "80" (you'll need to call int(self.numberOfAtoms))
    print "my number of atoms is " + self.numberOfAtoms

    #do all of your solving stuff you want...

    FINAL_SOLUTION = IMPLEMENT_FINAL_SOLUTION()

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

  def fitnessAlgorithm(allAtoms):
   return 1.0/allAtoms.getPotentialEnergy();

  def breed(generation):
	children = [];
	for i in range(len(generation)):
		for j in range(i, len(generation)):
			children.append(breedAtoms(generation[i], generation[j]));
			children.append(breedAtoms(generation[i], generation[j]));

  def mutate(atoms1):
    return true;

    #NEED TO FIX
  def breedAtoms(atoms1, atoms2):
    atoms1xheap = [];
	atoms2xheap = [];
    for atom in atoms1:
        heappush(atoms1xheap, (atom.position[0], atom));
    for atom in atoms2:
		heappush(atoms2xheap, (atom.position[0], atom));
    output = [];
    int atom1counter = 0;
    int atom2counter = 0;
    String atom1counter = atoms1.get_chemical_symbols()[0];
    String atom2counter = atoms2.get_chemical_symbols()[1];
    atom1counter = atoms1[]
    for atom in atoms1:

    if(random() < 0.25):
        for index in range(50):
			output.append(atom);
		for index2 in range(50):
			output.append(heapPop(atoms2.xheap(-1)[1]);
	elif(random() < 0.50):
		for index in range(50):
			output.append(atoms1xheap.pop(0)[1]);
		for index2 in range(50):
			output.append(heapPop(atoms1.xheap(-1)[1]);
	elif(random() < 0.75):
		for index in range(50):
			output.append(atoms2xheap.pop(0)[1]);
		for index2 in range(50):
			output.append(heapPop(atoms1.xheap(-1)[1]);
	else:
		for index in range(50):
			output.append(atoms2xheap.pop(0)[1]);
		for index2 in range(50):
			output.append(heapPop(atoms2.xheap(-1)[1]);
	return output;

  def IMPLEMENT_FINALSOLUTION():
    return [];