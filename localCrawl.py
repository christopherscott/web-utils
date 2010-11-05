#!/usr/bin/env python
import sys
import re
import urllib
from sgmllib import SGMLParser

try:
	homepage = sys.argv[1]
except:
	print "Usage: localcrawl.py [url]"
	sys.exit(2)

class URLParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []
	
	def start_a(self, attributes):
		href = [value for key, value in attributes if key=='href']
		if href:
			self.urls.extend(href)

# set starting page, pattern, empty array for pages to visit
itinerary = []

relpattern = re.compile("/")

# open the socket, store source as string object
response = urllib.urlopen(homepage)
source = response.read()
response.close()

# create parser, feed in the source, close the parser
# to free up memory and flush the buffer
parser = URLParser()
parser.feed(source)
parser.close()

print "Itenerary:"

# loop over urls, printing only those that match 
for url in parser.urls:
	if relpattern.match(url) and not url in itinerary:
		itinerary.append(url)
		print url

for stop in itinerary:
	current = urllib.urlopen("%s%s" % (homepage, stop))
	code = current.getcode()
	if 100 <= code <= 199:
		pre = "\033[1;33m"
	elif 200 <= code <= 299:
		pre = "\033[1;32m"
	elif 300 <= code <= 399:
		pre = "\033[1;36m"
	elif 400 <= code <= 499:
		pre = "\033[1;31m"
	elif 500 <= code <= 599:
		pre = "\033[1;35m" 
	print "%s%s%s %s%s" % (pre, code, "\033[1;m", homepage, stop)	
	current.close()