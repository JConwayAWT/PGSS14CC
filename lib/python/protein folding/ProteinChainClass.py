import random
from copy import deepcopy

coords = [[0,0]]
list_of_amino_acids = range(100)
number_of_acids = len(list_of_amino_acids)
def add_or_subtract_one_from_x_or_y(coordinates):
    R = random.random()#range of [0,1]
    last_coord = coordinates[-1]
    new_coord = deepcopy(coordinates[-1])
    if (R >= 0) and (R <= 0.25):
        new_coord[0]+=1
    elif (R <= .5):
        new_coord[0]-=1
    elif(R <= 0.75):
        new_coord[1]+=1
    else:
        new_coord[1]-=1

    if new_coord not in coordinates:
        if trapped(new_coord, coordinates):
            coordinates.pop(-1)
            coordinates.pop(-1)
            coordinates.pop(-1)
            coordinates.pop(-1)
            coordinates.pop(-1)
            #removing the acid, starting from the right hand of the list, denoted by the minus
        else:
            coordinates.append(last_coord)

    return coordinates

def trapped(last_coord, coordinates):
    if([last_coord[0]+1, last_coord[1]] in coordinates)and([last_coord[0]-1, last_coord[1]] in coordinates)and([last_coord[0], last_coord[1]+1] in coordinates)and([last_coord[0], last_coord[1]-1] in coordinates):
        return True
    else:
        return False

while len(coords) < number_of_acids:
    print len(coords)
    coords = add_or_subtract_one_from_x_or_y(coords)

print coords
