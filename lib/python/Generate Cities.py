#-------------------------------------------------------------------------------
# Name:        Generate Cities
# Purpose:     Generates Cities for Travelling salesman problem
#
# Author:      Ishan Levy
#
# Created:     07/07/2014
# Copyright:   (c) Ishan 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------
import random
import math
def city_generate_random(number_of_cities, startx, stopx, starty, stopy, mindistance = 0):
    xpoint = []
    ypoint = []
    for i in xrange(0,number_of_cities):#Runs for each city
        x = 0
        y = 0
        restart = True
        while restart == True:#Runs this while loop until a certain distance from each city
            restart = False
            x = random.randint(startx,stopx)
            y = random.randint(starty,stopy)
            if i > 1:
                for j in xrange(0,i-1):
                    #MARTIN : Was this intended to be a rectangular distance comparison?
                    if abs(xpoint[i-1]-x) < mindistance and abs(ypoint[i-1]-y) < mindistance:
                        restart = True
        xpoint.append(x)
        ypoint.append(y)
    return xpoint,ypoint

if __name__ == '__main__':
    print city_generate_random(10,0,100,0,100,10)