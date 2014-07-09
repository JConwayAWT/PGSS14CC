import database_connect as db_connect
import sys

def main():

    rails_environment = sys.argv[1]
    connection = db_connect.connect_to_database(rails_environment)
    print "Current Python version is " + sys.version

if __name__ == '__main__':
    main()