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
        self.particle = genParticle(self.definingString,int(self.numberOfAtoms)); #Generates the base particle
        print self.particle.get_potential_energy(); #Prints base case energy
        self.bestParticles = []; #Initializes the list of bestParticles
        self.bestEnergy = self.particle.get_potential_energy(); #Initializes best energy
        self.bestParticle = copy.copy(self.particle); #Best particle is a copy of particle
        heapq.heappush(self.bestParticles, (self.particle.get_potential_energy(), self.particle)); #Pushes particle to bestParticles
        for i in range(100): #Mutates particle 100 times and pushes results into a heap
            self.bestPparticle = self.mutate(self.particle);
            heapq.heappush(self.bestParticles, (self.bestParticle.get_potential_energy(), self.bestParticle));
        self.currentEnergy = 0;
        self.currentParticle = None;
        for i in range(15):
            self.currentEnergy = 1000000;
            self.newBestParticles = [];
            for l in range(10):
                self.newBestParticles.append(heapq.heappop(self.bestParticles));
                print((self.newBestParticles[-1])[0]);
            self.bestParticles = copy.copy(self.newBestParticles);
            self.children = self.breed(self.bestParticles);
            for j in range(len(self.bestParticles)):
                newparticle = self.mutate((self.bestParticles[j])[1]);
                self.bestParticles[j] = (newparticle.get_potential_energy(), newparticle);
                if((self.bestParticles[j])[0] < self.currentEnergy):
                    self.currentParticle = (self.bestParticles[j])[1];
                    self.currentEnergy = (self.bestParticles[j])[0];
            for index in range(len(self.children)):
                newparticle = (self.children[index]);
                heapq.heappush(self.bestParticles, (newparticle.get_potential_energy(), newparticle));
            print("-------------");
        self.minEnergy = 100000;
        self.bestParticle = None;
        for i in range(len(self.bestParticles)):
            if((self.bestParticles[i])[0] < self.minEnergy):
                self.bestParticle = (self.bestParticles[i])[1];
                minEnergy = (self.bestParticles[i])[0];
        listOfAtoms = [];
        for atom in self.bestParticle:
          dictElement = {"symbol":atom.symbol,"x":atom.position[0],"y":atom.position[1],"z":atom.position[2]}
          listOfAtoms.append(dictElement)
        dictionary_to_be_turned_into_json = {"atoms": listOfAtoms, "potentialEnergy": minEnergy}
        actually_json = json.dumps(dictionary_to_be_turned_into_json)

        # this gets returned to the parent class and shoved into the database as a string, then
        # parsed as JSON on the page and displayed/drawn for the user
        return actually_json

  def breed(self, generation):
    children = [];
    for i in range(len(generation)):
        for j in range(i, len(generation)):
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
            children.append(self.breedParticles((generation[i])[1], (generation[j])[1]));
    return children;

  def mutate(self, particle):
    temp = particle.get_potential_energy;
    for atom in particle:
        if(random.random() < 0.05):
            val = random.random()/100.0;
            atom.x += val;
            if(particle.get_potential_energy > temp):
                atom.x -= 2*val
        elif(random.random() < 0.05):
            val = random.random()/100.0;
            atom.y += val;
            if(particle.get_potential_energy > temp):
                atom.y -= 2*val
        elif(random.random() < 0.05):
            val = random.random()/100.0;
            atom.z += val;
            if(particle.get_potential_energy > temp):
                atom.z -= 2*val
        elif(random.random() < 0.05):
            val = random.random()/100.0;
            atom.x -= val;
            if(particle.get_potential_energy > temp):
                atom.x += 2*val
        elif(random.random() < 0.05):
            val = random.random()/100.0;
            atom.y -= val;
            if(particle.get_potential_energy > temp):
                atom.y += 2*val
        elif(random.random() < 0.05):
            val = random.random()/100.0;
            atom.z -= val;
            if(particle.get_potential_energy > temp):
                atom.z += 2*val
    return particle;

    #NEED TO FIX
  def breedParticles(self, particle1, particle2):
    index = 0;
    mindistance = 0;
    bestatom = None;
    for atom in particle1:
        mindistance = 1000000;
        bestatom = None;
        if(random.random() < 0.5):
            for atom2 in particle2:
                if(atom2.symbol == atom.symbol and (atom.position[0] - atom2.position[0])**2 + (atom.position[1] - atom2.position[1])**2 + (atom.position[2] - atom2.position[2])**2 < mindistance**2):
                    mindistance = ((atom.position[0] - atom2.position[0])**2 + (atom.position[1] - atom2.position[1])**2 + (atom.position[2] - atom2.position[2])**2)**0.5;
                    bestatom = atom2;
            atom.x = bestatom.position[0];
            atom.y = bestatom.position[1];
            atom.z = bestatom.position[2];
    return particle1;

if __name__ == '__main__':
    GA = GeneticSolver();
    GA.definingString = "Pt10Au5";
    GA.numberOfAtoms = 15;
    print GA.solve();
    print "DONE";