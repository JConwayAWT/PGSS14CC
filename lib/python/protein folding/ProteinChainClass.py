import random
from copy import deepcopy
import AminoAcid

class ProteinChain:

  def __init__(self,amino_acid_chain_string):
    self.amino_acid_chain = list(amino_acid_chain_string)
    self.coords = [[0,0]]
    self.number_of_acids = len(self.amino_acid_chain)
    self.chainAminoAcids = []

  def add_or_subtract_one_from_x_or_y(self,coordinates):
    R = random.random() #range of [0,1]
    last_coord = coordinates[-1]
    new_coord = deepcopy(coordinates[-1])
    if (R >= 0) and (R <= 0.25):
      new_coord[0]+=1
    elif (R <= .5):
      new_coord[0]-=1
    elif (R <= 0.75):
      new_coord[1]+=1
    else:
      new_coord[1]-=1
    if (new_coord not in coordinates):
      if self.trapped(new_coord, coordinates):
        coordinates.pop(-1)
        #removing the acid, starting from the right hand of the list, denoted by the minus
      else:
        coordinates.append(new_coord)
    return coordinates

  def trapped(self,last_coord, coordinates):
    if (([last_coord[0]+1, last_coord[1]] in coordinates) and ([last_coord[0]-1, last_coord[1]] in coordinates)and([last_coord[0], last_coord[1]+1] in coordinates)and([last_coord[0], last_coord[1]-1] in coordinates)):
      return True
    else:
      return False

  def generateChainCoordinates(self):
    while (len(self.coords) < self.number_of_acids):
      self.coords = self.add_or_subtract_one_from_x_or_y(self.coords)

  def getCoords(self):
    return self.coords

  def generateChainAminoAcids(self):
    try:
      assert len(self.coords) == self.number_of_acids
    except:
      self.generateChainCoordinates()
    for i in range(self.number_of_acids):
      acid = self.amino_acid_chain[i]
      coord = self.coords[i]
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

  def getChain(self):
    return self.chainAminoAcids

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
