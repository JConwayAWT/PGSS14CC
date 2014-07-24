import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
#lib_path = os.path.abspath('')
#sys.path.append(lib_path)
import math
from solvers import MetalicsSolver
import random
import copy
import json
import ase
from ase import Atoms,io
from ase.calculators.emt import EMT
from ase.optimize import FIRE, LBFGSLineSearch

def genParticle(definingString,number):
  """definingString should be something like " 'Pt80' ", for example.
  number should be the number of atoms that will be in the molecule."""
  dummyAtom = ase.io.read('InputGeom.vasp',format='vasp')
  while (len(dummyAtom) > number):
    dummyAtom.pop(-1)
  coords = dummyAtom.get_positions()
  newAtom = Atoms(definingString,coords)
  calc = EMT()
  newAtom.set_calculator(calc)
  dyn = LBFGSLineSearch(atoms=newAtom)
  dyn.run(steps=200000)
  dyn = FIRE(atoms=newAtom)
  dyn.run(fmax=0.01)
  return newAtom

def create_sample_atom(inNumberOfAtoms,inAtomType):
  """Creates a mostly spherical atom with inNumberOfAtoms atoms
  and all of element inAtomType.  inAtomType MUST BE A STRING.
  For example, 'Pt79' for Platinum and 79 atoms."""
  positionList = []
  halfOfRadius = 3
  standardDeviation = 1.65
  for x in range(0,inNumberOfAtoms):
    atomX = random.normal(halfOfRadius,standardDeviation)*plusOrMinus()
    atomY = random.normal(halfOfRadius,standardDeviation)*plusOrMinus()
    atomZ = random.normal(halfOfRadius,standardDeviation)*plusOrMinus()
    positionList.append((atomX,atomY,atomZ))
  sample_atom = Atoms(inAtomType,numpy.asarray(positionList))
  return sample_atom

def nearlySphericalAtom(definingString,inRadius,number):
  """definingString should be something like " 'Pt80' ", for example.
  inRadius should be the radius that you wish to have for the atom.
  number should be the number of atoms that will be in the molecule."""
  positionList = []
  for x in range(number):
    xDistance = random.uniform(0,inRadius)*plusOrMinus()
    remainingX = ((inRadius**2) - (xDistance**2))**0.5
    yDistance = random.uniform(0,remainingX)*plusOrMinus()
    zDistance = random.uniform(0,(((remainingX**2) - (yDistance**2))**0.5)*plusOrMinus() + random.normal(0,0.1))
    coordinates = (xDistance,yDistance,zDistance)
    positionList.append(coordinates)
  newAtom = Atoms(definingString,positionList)
  calc = EMT()
  newAtom.set_calculator(calc)
  dyn = LBFGSLineSearch(atoms=newAtom)
  dyn.run(steps=200000)
  dyn = FIRE(atoms=newAtom)
  dyn.run(fmax=0.01)
  return newAtom

def distanceCenter(atoms):
	distanceArray = numpy.zeros(len(atoms))
	cx = atoms.get_center_of_mass()[0]
	cy = atoms.get_center_of_mass()[0]
	cz = atoms.get_center_of_mass()[0]
	for i in range(len(atoms)):
                px = atoms.get_positions()[i,0]
		py = atoms.get_positions()[i,1]
		pz = atoms.get_positions()[i,2]
		distance = ((px-cx)**2+(py-cy)**2+(pz-cz)**2)**0.5
		distanceArray[i] = distance
	return distanceArray

def plusOrMinus():
    a = random.uniform(0,1)
    if (a>0.5):
        return 1
    else:
        return -1
