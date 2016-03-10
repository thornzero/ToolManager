#!/usr/bin/python

import sys, getopt, re

def main(argv):
  inputfile = ''
  outputfile = '!setup'
  p = re.compile(r'(T\d+)')

  try:
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
  except getopt.GetoptError:
    print 'test.py -i <inputfile>'
    sys.exit(2)

  for opt, arg in opts:
    if opt == '-h':
      print 'test.py -i <inputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
      file = open(inputfile)

      for line in file:
        if p.findall(line) != '':
        print(line)

if __name__ == "__main__":
  main(sys.argv[1:])