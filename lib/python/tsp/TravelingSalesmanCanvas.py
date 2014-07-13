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
from solvers import BruteForceTravelingSalesmanSolver as bft
from solvers import AntTotalDistanceSolver as atd
from solvers import LineOverlapEliminatorTravelingSalesmanSolver as loe
from database import database_connect as dbf


def main():
  rails_environment = sys.argv[1]
  connection = dbf.connect_to_database(rails_environment)

  database_row_id=sys.argv[2]

  cur = connection.cursor()
  cur.execute ("SELECT * FROM traveling_salesmen WHERE id=\'"+database_row_id+"\' LIMIT 1;")
  database_row = cur.fetchone()
  database_row_id = database_row[0]
  params = database_row[3]
  algorithm = database_row[4]
  if algorithm =="Brute Force (n!)":
    solver = bft.BruteForceTravelingSalesmanSolver(params)
  if algorithm =="Ant Total Distance (n^2)":
    solver = atd.AntTotalDistanceSolver(params)
    solver.REMOVE_LINE_CROSSES=False
  if algorithm =="Ant Total Distance Remove Line Crosses (n^3)":
    solver = atd.AntTotalDistanceSolver(params) 
  if algorithm =="Random Remove Line Crosses (n^2 to n^3)":
    solver = loe.LineOverlapEliminatorTravelingSalesmanSolver(params)
  if solver is None:
    print "ERROR: Invalid solver!"
  else:
    solution = solver.solve()
    print solution

if __name__ == '__main__':
    main()


