import psycopg2

def main():
    connection = psycopg2.connect("dbname='pgss_14_cc_dev'")
    import sys
    print sys.version

if __name__ == '__main__':
    main()