#!/usr/bin/env python
import re
import sys

def main(argv):
  try:
    source = open(argv[0]).read()
  except:
    print "%s could not be opened" % argv
  killEmpties(source)
  


def killEmpties(source):
  emptyRule = re.compile(r".*\{(\s)*\}")
  for match in emptyRule.finditer(source):
    print match.group(0)

if __name__ == "__main__":
  main(sys.argv[1:])