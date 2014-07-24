import random
from copy import deepcopy
import ProteinFoldingSolver
import AminoAcid
import os, sys
lib_path = os.path.abspath('../../helpers')
sys.path.append(lib_path)
lib_path = os.path.abspath('../')
sys.path.append(lib_path)
random.seed()

class ProteinChain(ProteinFoldingSolver.ProteinFoldingSolver):

  def __init__(self,amino_acid_chain_string):
    self.startTime = self.millis()
    self.amino_acid_chain = list(amino_acid_chain_string)
    self.coords = [[0,0]] # this is just a list of coordinates
    self.cords = [] # this is the list of coordinates with identities
    self.number_of_acids = len(self.amino_acid_chain)
    self.chainAminoAcids = []
    self.Energy = float('inf')
    self.generateChainCoordinates()
    self.generateChainAminoAcids()
    self.getEnergy()

  def add_or_subtract_one_from_x_or_y(self):
    R = random.random() #range of [0,1]
    last_coord = deepcopy(self.coords[-1])
    new_coord = deepcopy(self.coords[-1])
    if (R >= 0) and (R <= 0.25):
      new_coord[0]+=1
    elif (R <= .5):
      new_coord[0]-=1
    elif (R <= 0.75):
      new_coord[1]+=1
    else:
      new_coord[1]-=1
    if (new_coord not in self.coords):
      self.coords.append(new_coord)
    if self.trapped():
      self.trappedCount += 1
      self.coords.pop(-1)
      self.coords.pop(-1)
      self.coords.pop(-1)
      self.coords.pop(-1)
      self.coords.pop(-1)

  def trapped(self):
    last_coord = deepcopy(self.coords[-1])
    if (([last_coord[0]+1, last_coord[1]] in self.coords) and ([last_coord[0]-1, last_coord[1]] in self.coords)and([last_coord[0], last_coord[1]+1] in self.coords)and([last_coord[0], last_coord[1]-1] in self.coords)):
      return True
    else:
      return False

  def generateChainCoordinates(self):
    self.coords = [[0,0]]
    self.trappedCount = 0
    while (len(self.coords) < self.number_of_acids):
      self.add_or_subtract_one_from_x_or_y()
      if (self.trappedCount > 10):
        self.coords = [[0,0]]
        self.trappedCount = 0

  def getCoords(self):
    return self.coords

  def getCords(self):
    return self.cords

  def generateChainAminoAcids(self):
    self.cords = []
    self.chainAminoAcids = []
    try:
      assert len(self.coords) == self.number_of_acids
    except:
      self.generateChainCoordinates()
    for i in range(self.number_of_acids):
      acid = self.amino_acid_chain[i]
      coord = self.coords[i]
      cord = deepcopy(self.coords[i])
      cord.append(acid)
      self.cords.append(cord)
      self.chainAminoAcids.append(AminoAcid.AminoAcid())
      self.chainAminoAcids[i].setCoord(coord)
      self.chainAminoAcids[i].set_Polarity_and_Index(acid,i)
      if (i > 0):
        self.chainAminoAcids[i].setPreviousNeighbor(self.coords[i - 1])
      if (i < (len(self.coords) - 1)):
        self.chainAminoAcids[i].setNextNeighbor(self.coords[i + 1])

  def setCoords(self, newCoords):
    try:
      assert (len(newCoords) == len(self.coords))
    except:
      print "Size mismatch in coords!"
      return
    try:
      assert (len(self.chainAminoAcids) == self.number_of_acids)
    except:
      self.generateChainAminoAcid()
    for i in range(self.number_of_acids):
      coord = newCoords[i]
      self.chainAminoAcids[i].setCoord(coord)
      if (i > 0):
        self.chainAminoAcids[i].setPreviousNeighbor(newCoords[i - 1])
      if (i < (len(self.coords) - 1)):
        self.chainAminoAcids[i].setNextNeighbor(newCoords[i + 1])
    self.coords = newCoords
    for i in range(len(self.coords)):
      self.cords[i][0] = self.coords[i][0]
      self.cords[i][1] = self.coords[i][1]
    self.getEnergy()

  def getChain(self):
    return self.chainAminoAcids

  def getEnergy(self):
    self.Energy = 0.
    for acid in self.chainAminoAcids:
      if acid.pole == 'H':
        coord = deepcopy(acid.coord)
        test_coord = deepcopy(coord)
        test_coord[0] += 1
        if ((test_coord in self.coords) and (test_coord != acid.pNeighbor) and (test_coord != acid.nNeighbor)):
          index = self.coords.index(test_coord)
          if (self.cords[index][2] == 'H'):
            self.Energy -= 0.5
        test_coord = deepcopy(coord)
        test_coord[0] -= 1
        if ((test_coord in self.coords) and (test_coord != acid.pNeighbor) and (test_coord != acid.nNeighbor)):
          index = self.coords.index(test_coord)
          if (self.cords[index][2] == 'H'):
            self.Energy -= 0.5
        test_coord = deepcopy(coord)
        test_coord[1] -= 1
        if ((test_coord in self.coords) and (test_coord != acid.pNeighbor) and (test_coord != acid.nNeighbor)):
          index = self.coords.index(test_coord)
          if (self.cords[index][2] == 'H'):
            self.Energy -= 0.5
        test_coord = deepcopy(coord)
        test_coord[1] -= 1
        if ((test_coord in self.coords) and (test_coord != acid.pNeighbor) and (test_coord != acid.nNeighbor)):
          index = self.coords.index(test_coord)
          if (self.cords[index][2] == 'H'):
            self.Energy -= 0.5

def list_of_as_in_a_row(chain):
  list_of_a_indexes = []
  current_list = []
  for k in range(len(chain)):
      if chain[k] == 'A':
          current_list.append(k)
      else:
          if current_list != []:
              list_of_a_indexes.append(current_list)
          current_list= []
      if k == len(chain) -1:
          list_of_a_indexes.append(current_list)
  return [element for element in list_of_a_indexes if element != []]
