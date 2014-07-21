import numpy as np

class Grid:

    grid
    centerx
    centery
    currentx
    currenty
    list

    def __init__(self):
        pass

    def generateList(num):
        a= 0
        while a<num:
            list.append(0)
            a+=1

    def makeGrid(): #creates a grid that will simulate a coordinate plane (hopefully maybe please)
        grid = [[list],[list]]
        centerx = num + 1
        centery = num + 1
        return grid

    def changePoint(x1, y1, value): #changePoint will change the character at the coordinates (x1, y1) to value (value should be 'A' or 'B'
        grid[x1, y1] = value

    def returnPoint(x1, y1): #returnPoint will return the character at the coordinates (x1, y1)
        return grid[x1, y1]








