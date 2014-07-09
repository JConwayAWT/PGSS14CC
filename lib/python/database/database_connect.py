import urlparse
import os
import psycopg2


def connect_to_database(rails_environment):
  if rails_environment == "production":
    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'DATABASE_URL' in os.environ:
      url = urlparse.urlparse(os.environ['DATABASE_URL'])

      DATABASES['default'] = DATABASES.get('default', {})
      connection = psycopg2.connect("dbname='"+url.path[1:]+"' user='"+url.username+"' host='"+url.hostname+"' password='"+url.password+"'")
    else:
      print "DATABASE_URL is missing"
  else:
    connection = psycopg2.connect("dbname='pgss_14_cc_dev' user='postgres' password='password'")

  return connection
