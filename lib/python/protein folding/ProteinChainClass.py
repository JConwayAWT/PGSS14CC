import random
from copy import deepcopy

class ProteinChain:

  def __init__(self,amino_acid_chain_string):
    self.amino_acid_chain = list(amino_acid_chain)
    self.coords = [[0,0]]
    self.number_of_acids = len(self.amino_acid_chain)

  def list_of_as_in_a_row (chain):
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
    print (element for element in list_of_a_indexes if element != [])


  def add_or_subtract_one_from_x_or_y(coordinates):
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
    if new_coord not in coordinates:
      if trapped(new_coord, coordinates):
        coordinates.pop(-1)
        #removing the acid, starting from the right hand of the list, denoted by the minus
      else:
        coordinates.append(new_coord)
      return coordinates

  def trapped(last_coord, coordinates):
    if ([last_coord[0]+1, last_coord[1]] in coordinates)and([last_coord[0]-1, last_coord[1]] in coordinates)and([last_coord[0], last_coord[1]+1] in coordinates)and([last_coord[0], last_coord[1]-1] in coordinates):
      return True
    else:
      return False

  def generateChain():
    while (len(self.coords) < self.number_of_acids):
      self.coords = add_or_subtract_one_from_x_or_y(self.coords)

  def getCoords():
    return self.coords
