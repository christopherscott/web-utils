#!/usr/bin/env python

import os, sys, fileinput

store = "ch"

ch_tokens = {
  "@i18n.countryCode.english@" : "en_CH",
  "@i18n.countryCode.french@" : "fr_CH",
  "@i18n.countryCode.german@" : "de_CH",
  "@i18n.countryCode.italian@" : "it_CH"
}

types = (".css", ".js", ".jsp", ".jspf")

def replaceAll(text, dict):
  for token, value in dict.iteritems():
    text = text.replace(token, value)
  return text
  
def getFilesByType(directory):
  
  for root, dirnames, files in os.walk(directory):
    
    # ignore directories like .svn and .git
    dirnames[:] = [ d for d in dirnames if not d.startswith('.') ]
    
    # create file list if ends with correct types
    filelist = [ os.path.join(root, f) for f in files if f.endswith(types) ]
    
    # if list isn't empty, loop through, in-place edit
    if filelist:
      for line in fileinput.input(filelist, inplace=1):
        
        # igore lines with no token whatsoever
        if line.find("@i18n.countryCode."):
          # eventually needs other store codes
          if store == "ch":
            sys.stdout.write(replaceAll(line, ch_tokens))            
        else:
          sys.stdout.write(line)

if __name__ == "__main__":
  getFilesByType(os.getcwd())