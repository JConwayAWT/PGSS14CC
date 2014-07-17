import random
import AminoAcid

coords = [[0,0]]

amino_acid_chain = 'AAAAAAABBBBBBBBBB'

list_of_amino_acids = list(amino_acid_chain)

num_of_acids = len(list_of_amino_acids)

def add_or_sub_one(coords):
    R = random.random()
    if (R >= 0) and (R <= .25):
        last_coord = coords[-1]
        last_coord[0] += 1

    elif (R <= .5):
        last_coord = coords[-1]
        last_coord[0] -= 1

    elif (R <= .75):
        last_coord = coords[-1]
        last_coord[1] += 1

    else:
        last_coord = coords[-1]
        last_coord[1] -= 1

    if last_coord not in coords:
        #
        if trapped(coords):
            coords.pop(-1)
        else:
            coords.append(last_coord)

def trapped(coords):
    last_coord = coords[-1]
    if ([last_coord[0] + 1, last_coord[1]] not in coords):
        return true
    elif ([last_coord[0] - 1, last_coord[1]] not in coords):
        return true
    elif ([last_coord[0], last_coord[1] + 1] not in coords):
        return true
    elif ([last_coord[0], last_coord[1] - 1 not in coords]):
        return true
    else:
        return false


while len(coords) < num_of_acids:
    add_or_sub_one(coords)


print coords
