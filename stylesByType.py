#!/usr/bin/env python

import sys
import re

reBackground = re.compile(r"(background.*?url.*?);")
reSelector = re.compile(r"(.*?){")

mydict = {}

def main(argv):
    source = open(argv[0])
    buildDict(source)

def buildDict(source):  
  for line in source.readlines():
    if reSelector.match(line):
      selector = reSelector.match(line)
    if reBackground.search(line):
      background = reBackground.search(line)
      if selector:
        mydict[selector.group(1)] = background.group(1)

  for selector, rule in mydict.items():
    print("%s : %s" % (selector, rule))
    
if __name__ == "__main__":
  main(sys.argv[1:])
