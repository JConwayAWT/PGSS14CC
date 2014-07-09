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
import TravelingSalesmanSolver
import BruteForceTravelingSalesmanSolver

def main():
  rails_environment = sys.argv[1]
  if rails_environment == "production":
    if 'DATABASES' not in locals():
      DATABASES = {}

    if 'DATABASE_URL' in os.environ:
      url = urlparse.urlparse(os.environ['DATABASE_URL'])

      DATABASES['default'] = DATABASES.get('default', {})
      connection = psycopg2.connect("dbname='"+url.path[1:]+"' user='"+url.username+"' host='"+url.hostname+"' password='"+url.password+"'")
      #print sys.version
    #else:
      #print "DATABASE_URL is missing"
  else:
    connection = psycopg2.connect("dbname='pgss_14_cc_dev' user='postgres' password='password'")
    cur = connection.cursor()
    cur.execute ("SELECT * FROM traveling_salesmen ORDER by id DESC;")
    database_row = cur.fetchone()
    database_row_id = database_row[0]
    params = database_row[3]

    solver = BruteForceTravelingSalesmanSolver.BruteForceTravelingSalesmanSolver(params)
    solution = solver.solve()

    print solution

    #print sys.version
  print "Success! ID:", database_row_id

if __name__ == '__main__':
    main()


