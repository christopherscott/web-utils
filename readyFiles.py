#!/usr/bin/env python

# replace tokens in css, js, etc.. files

# 

import os, sys, fileinput

store = "ch"
 
ch_tokens = {
  "@some.token.one@" : "one",
  "@some.token.two@" : "two",
  "@some.token.three@" : "three",
  "@some.token.four@" : "four"
}

types = (".css", ".js", ".jsp", ".jspf")

def replaceAll(text, dict):
  for token, value in dict.iteritems():
    text = text.replace(token, value)
    
  return text

def getFiles(directory):
  filelist = []
  for root, dirnames, files in os.walk(directory):
    # ignore directories like .svn and .git
    dirnames[:] = [ d for d in dirnames if not d.startswith('.') ]
    # create file list if ends with correct types
    filelist.extend([ os.path.join(root, f) for f in files if f.endswith(types) ])
  
  return filelist    

def replaceTokens(filelist):
  for line in fileinput.input(filelist, inplace=1):
    # igore lines with no token whatsoever
    if line.find("@some.token."):
      # eventually needs other store codes
      if store == "ch":
        sys.stdout.write(replaceAll(line, ch_tokens))            
    else:
      sys.stdout.write(line)

if __name__ == "__main__":
  replaceTokens( getFiles( os.getcwd() ) )
  