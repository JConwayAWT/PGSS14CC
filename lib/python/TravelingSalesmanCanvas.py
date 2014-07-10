#-------------------------------------------------------------------------------
# Name:        Traveling Salesman Canvas
# Purpose:     Takes data from the JQuery canvas, processes it, and returns it to the user
#
# Author:      Martin Schneider
#
# Created:     07/09/2014
# Copyright:   (c) Martin 2014
# Licence:     Creative Commons (CC)
#-------------------------------------------------------------------------------


import psycopg2
import os
import urlparse
import sys
from solvers import TravelingSalesmanSolver
from solvers import BruteForceTravelingSalesmanSolver
from database import database_connect as dbf
def main():
  rails_environment = sys.argv[1]
  connection = dbf.connect_to_database(rails_environment)

  cur = connection.cursor()
  cur.execute ("SELECT * FROM traveling_salesmen ORDER by id DESC;")
  database_row = cur.fetchone()
  database_row_id = database_row[0]
  params = database_row[3]

  solver = BruteForceTravelingSalesmanSolver.BruteForceTravelingSalesmanSolver(params)
  solution = solver.solve()

  print solution

if __name__ == '__main__':
    main()


