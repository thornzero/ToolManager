#!/usr/bin/python

import sys
import getopt
import re


def main(argv):
    inputfile = ''
    outputfile = '!setup.nc'
    p = re.compile(r'(T\d+)')

    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'test.py -i <{0}>'.format(inputfile)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print "test.py -i <{0}>".format(inputfile)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            myfile = open(inputfile)

        for line in myfile:
            if p.findall(line) != '':
                print(line)

if __name__ == "__main__":
  main(sys.argv[1:])