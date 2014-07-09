import psycopg2
import os
import urlparse
import sys

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
    params = cur.fetchone()
    print params
    print params[0]
    
    #print sys.version
  print "E"
  print len(sys.argv)
  print str(sys.argv)

if __name__ == '__main__':
    main()


