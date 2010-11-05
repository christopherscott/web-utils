#!/usr/bin/env python

""" Styles by type: a tool for extracting CSS rules by property type or value"""

import sys
import re

reSelector = re.compile(r"(.*?){")

mydict = {}

def main(argv):
    """ Main"""
    # first assign variables
    try:
      source = open(argv[0])
    except:
      print("%s could not be opened")
    
    # wondering if there should be a check here
    # for a valid regex... or otherwise validate this argument
    pattern = re.compile( r"(" + argv[1] + r".*?;)")
    
    # start the process
    # ideally after input has been validated/checked
    buildDict(source, pattern)

def buildDict(source, pattern):
  """ Build a dictionary of selector => rule string pairs
  
  Should, at a minimum return a status to the environment from which it was called"""
  for line in source.readlines():
    if reSelector.match(line):
      selector = reSelector.match(line)
    if pattern.search(line):
      match = pattern.search(line)
      if selector:
        mydict[selector.group(1)] = match.group(1)

  for selector, rule in mydict.items():
    print("%s { \n %s \n } \n" % (selector, rule))
    
if __name__ == "__main__":
  main(sys.argv[1:])
