#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Guirong
#
# Created:     17/07/2014
# Copyright:   (c) Guirong 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
R = random.random() #range of [0,1]

coords = [[0, 0], [0, -1], [1, -1], [1, -2], [1, -3], [1, -4], [0, -4]]


def newCoordinates():
    newCoord = []
    while (newCoord == []):
        R = random.random()
        last_coord = deepcopy(coords[-1])
        if (R >= 0) and (R <= 0.25) and ([last_coord[0]+1, last_coord[1]] not in coordinates):
            newCoord = [last_coord[0]+1, last_coord[1]]

        elif (R <= .5) and ([last_coord[0]-1, last_coord[1]] not in coordinates):
            newCoord = [last_coord[0]+1, last_coord[1]]

        elif (R <= .75) and ([last_coord[0], last_coord[1]+1] not in coordinates):
            newCoord = [last_coord[0], last_coord[1]+1]

        elif (R <= 1) and ([last_coord[0], last_coord[1]-1] not in coordinates):
            newCoord = [last_coord[0], last_coord[1]-1]

        return newCoord

    print newCoord

    if last_coord not in coordinates:
        if trapped(last_coord, coordinates):
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