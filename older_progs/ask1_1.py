#! /usr/bin/env python
# -*- coding: utf8 -*-
# 
import sys
if len(sys.argv)>1:
	w=int(sys.argv[1])
else:
	w=input("Βάρος : ")

print 'A weight of', w, 'on the moon is', float(w/6), 'on Venus is', float(w*0.9), 'and on Sun is', float(w*27.07)
