#!/usr/bin/env python
import re
import sys
import getopt

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hdo:", ["help", "debug"])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  
  for i in args:
    print i
  
  print "====="
  
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-d", "--debug"):
      global _debug
      _debug = 1
    elif opt in ("-o", "--output"):
      print "output"
    
  
def usage():
  print "Usage: killEmptyStyles.py css-file [-o output-file]"

def killEmpties(source):
  emptyRule = re.compile(r".*\{(\s)*\}")
  for match in emptyRule.finditer(source):
    print match.group(0)

if __name__ == "__main__":
  main(sys.argv[1:])