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

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

lib_path = os.path.abspath('../database')
sys.path.append(lib_path)

import psycopg2
import os
import urlparse
import sys
from solvers import TravelingSalesmanSolver
from solvers import BFTS2 as bft
from solvers import AntTotalDistanceSolver as atd
from solvers import LineOverlapEliminatorTravelingSalesmanSolver as loe
from solvers import GravitationalTravelingSalesmanSolver as gts
from solvers import DijkstraTravelingSalesmanSolverFinal as dts
from solvers import DijkstraTravelingSalesmanSolverStreamlined as dts2
from solvers import SimulatedAnnealingSalesmanSolver as sas
from database import database_connect as dbf

def main():
  rails_environment = sys.argv[1]
  connection = dbf.connect_to_database(rails_environment)
  connection.autocommit = True

  database_row_id=sys.argv[2]

  cur = connection.cursor()
  cur.execute ("SELECT * FROM traveling_salesmen WHERE id=\'"+database_row_id+"\' LIMIT 1;")
  database_row = cur.fetchone()
  database_row_id = database_row[0]
  params = database_row[3]
  algorithm = database_row[4] 
  remove_overlaps=database_row[10]

  if algorithm =="Brute Force (n!)":
    solver = bft.BFTS2(params)

  if algorithm =="Ant Total Distance (n^2)":
    solver = atd.AntTotalDistanceSolver(params)

  if algorithm =="Random (n)":
    solver = loe.LineOverlapEliminatorTravelingSalesmanSolver(params)

  if algorithm =="Gravity (n^2)":
    solver = gts.GravitationalTravelingSalesmanSolver(params)

  #Change this to Wheel Dijkstra and the other one to just Dijkstra
  if algorithm =="Wheel Dijkstra (n^3)":
    solver =dts.DijkstraSolver(params)
    
  if algorithm =="Fast Dijkstra (n^2)":
    solver = dts2.DijkstraTravelingSalesmanSolver(params)

  if algorithm =="Simulated Annealing":
    solver = sas.SimulatedAnnealingSalesmanSolver(params)

  solver.REMOVE_LINE_CROSSES=remove_overlaps

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


