#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Description : Gives 'whois' information about abusers taken from 'lastb'
Date        : 13/10/2017
Revision    : 3
Author      : dsim
'''

# Reverse a file using tac linux command
def tac(file1, file2):
	import os
	print(os.system('tac %s > %s' % (file1,file2)))

# Print file1 in reverse order
def reverse_read_file(file1):
	for line in reversed(list(open("file1"))):
		print(line.rstrip())
	 
def main:
	mabbr=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	fin1="/home/dion/Documents/abusers/abusers_per_day"
	fin2="/home/dion/Documents/abusers/lastb_fullname_all_abusers"
	
	# Format of file fin1
	# month day1
	# ip1 sumOfLoginAttempts
	# ip2 sumOfLoginAttempts
	# ip3 sumOfLoginAttempts
	# ...
	# month day2
	# ip1 sumOfLoginAttempts
	# ip2 sumOfLoginAttempts
	# ip4 sumOfLoginAttempts
	# ...
	#
	# The following code transforms the above in a list of lists :
	# [
	#  [['month' 'day1'], ['ip1', 'sumOfLoginAttempts'], ['ip2', 'sumOfLoginAttempts'], ['ip3', 'sumOfLoginAttempts'], ...,],
	#  [['month' 'day2'], ['ip1', 'sumOfLoginAttempts'], ['ip2', 'sumOfLoginAttempts'], ['ip4', 'sumOfLoginAttempts'], ...,],
	#  ...
	# ]
	recordsList = []
	record = []
	with open(fin1, 'r') as f1:
		for line in f1:
			if line[0:3] in mabbr and line[3].isspace() and line[4:].isdecimal() :
				if record:
					recordsList.append(record)
				record = []
			record.append(line.split())
		recordsList.append(record)
		f1.close()
	
	# Format of file fin2
	# <nouser> ssh:notty    139.162.122.110  Tue    Oct   24 03:23 - 03:23  (00:00)
	# admin    ssh:notty    173.254.216.66   Mon    Oct   23 16:12 - 16:12  (00:00)
	# admin    ssh:notty    94.142.242.84    Mon    Oct   23 16:11 - 16:11  (00:00)
	# admin    ssh:notty    23.129.64.11     Mon    Oct   23 16:11 - 16:11  (00:00)
	# ubuntu   ssh:notty    46.246.37.180    Mon    Oct   23 15:58 - 15:58  (00:00)
	# ...
	# were filds are :
	# user     protocol     ip              weekday month day various...
	#
	# The following code transforms the above in a list of lists :
	# 
	
	newRecordsList = []
	with open(fin2, 'r') as f2:
		for line in f2:
			record = []
			l = line.split()
			record.append
			


if __name__ == "__main__":
	pass
