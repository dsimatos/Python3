#!/usr/bin/env python
''' Given a url, try to retrieve it. If it's text/html, print its base url and its text.
This version uses try/except to print an error message if the urlopen() fails. '''

import sys
import urllib

def wget(url):
    try:
        ufile = urllib.urlopen(url)                 ## get file-like object for url
        if ufile.info().gettype() == 'text/html':   ## meta-info about the url content
            print ('Base url:' + ufile.geturl())
            print (ufile.read())                    ## read all its text
    except IOError:
        print ('Problem reading url:', url)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        wget(sys.argv[1])
    else:
        print('Usage : wget <url>')
