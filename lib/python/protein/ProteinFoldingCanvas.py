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


import os, sys
lib_path = os.path.abspath('../helpers')
sys.path.append(lib_path)

lib_path = os.path.abspath('../database')
sys.path.append(lib_path)

import psycopg2
import os
import urlparse
import sys
from solvers import ExampleSolver as e
from solvers import SlitheringSnakeSolver as ss
from solvers import alpha_beta_solver as ab
from solvers import alpha_beta_solver_3d as ab3d
from solvers import alpha_beta_ai_3d_solver as ab_3d_ai
from database import database_connect as dbf


def main():
  rails_environment = sys.argv[1]
  connection = dbf.connect_to_database(rails_environment)
  connection.autocommit = True

  database_row_id=sys.argv[2]

  cur = connection.cursor()
  cur.execute ("SELECT * FROM proteins WHERE id=\'"+database_row_id+"\' LIMIT 1;")
  database_row = cur.fetchone()
  database_row_id = database_row[0]
  params = database_row[3]
  algorithm = database_row[4]
  solver = None

  if algorithm == "Alpha Beta":
    solver = ab.alpha_beta(params)

  if algorithm =="Slithering Snake":
    solver = ss.SlitheringSnakeSolver(params)

  if algorithm == "Alpha Beta 3D AI":
    solver = ab_3d_ai.alpha_beta_ai_3d(params)

  if algorithm == "Alpha Beta 3D":
    solver = ab3d.alpha_beta_3d(params)

  if solver is None:
    print "ERROR: Invalid solver!"
  else:
    solver.cur = cur
    solver.database_row_id=database_row_id
    solver.setStatusDone("Calculating solution...")
    solution =solver.solve()
    solver.setSolution(solution)
    solver.setDone('y')
    print solution

if __name__ == '__main__':
    main()


