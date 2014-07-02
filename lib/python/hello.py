import pythonpg

def main():
    connection = pythonpg.connect("dbname='pgss_14_cc_prod'")
    import sys
    print sys.version

if __name__ == '__main__':
    main()