#PUT THIS AT THE TOP OF YOUR CODE:

import os, sys
lib_path = os.path.abspath('../helpers')
sys.path.append(lib_path)

#YOUR CODE HERE

class ProteinFolderSolver:
	def __init__(self):


		
		x=5
		y=10
		#CREATE THE CORDINATE
		cord = Coordinate.Coordinate(x,y)
		#ACCESS THE COORDINATE
		print cord.x
		print cord.y

