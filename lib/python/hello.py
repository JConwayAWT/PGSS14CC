import psycopg2
import os
import urlparse

def main():
    if 'DATABASES' not in locals():
      DATABASES = {}
    if 'DATABASE_URL' in os.environ:
      url = urlparse.urlparse(os.environ['DATABASE_URL'])

      DATABASES['default'] = DATABASES.get('default', {})
      connection = psycopg2.connect("dbname='"+url.path[1:]+"' user='"+url.username+"' host='"+url.hostname+"' password='"+url.password+"'")

    import sys
    print sys.version

if __name__ == '__main__':
    main()