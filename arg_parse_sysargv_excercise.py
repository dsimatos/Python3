#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Docstring
'''
Exercise from https://learncodethehardway.org/more-python-book/ex4.html

You are to write two tiny Python scripts that test out processing command line arguments using two methods:

 1. Plain old sys.argv like you would do normally.
 2. Python's argparse package, for more fancy argument handling.

Your test script should be able to handle the following situations:

 1. Getting help with --help or -h.
 2. At least three arguments that are flags, meaning they don't take an extra argument but simply putting them on the command line turns something on.
 3. At least three arguments that are options, meaning they do take an argument and set a variable in your script to that option.
 4. Additional "positional" arguments, which are a list of files at the end of all the -- style arguments and can handle Terminal wildcards like */.txt.

Remember that this is a timed 45 minute exercise and you need to stick to that
'''

def main(argv):
	
	if ('-h' in argv) or ('--help' in argv):
		print('Help...')
		exit(0)
	
	count = 0
	
	if '-a' in argv:
		something1 = 1
		print('som1', end=' ')
		count += 1
		
	if '-b' in argv:
		something2 = 1
		print('som2', end=' ')
		count += 1
	
	if '-c' in argv:
		something3 = 1
		print('som3', end=' ')
		count += 1
	
	if '-d' in argv:
		var1 = argv[argv.index('-d') +1]
		print('var1=', var1, end=' ')
		count += 2
	
	if '-e' in argv:
		var2 = argv[argv.index('-e') +1]
		print('var2=', var2, end=' ')
		count += 2
	
	if '-f' in argv:
		var3 = argv[argv.index('-f') +1]
		print('var3=', var3, end=' ')
		count += 2
	
	if count == 0:
		print('Usage: arg_parse [-h | --help] [-a] [-b] [-c] [-d arg_d] [-e arg_e] [-f arg_f] [more args]*')
		exit(1)
	
	if argv[count + 1 : ] != []:
		print(argv[count + 1 : ])
	else:
		print()
	
	exit(0)
		
	
	

import sys
# We put it in the end of file if we want to run it directly in interpreter e.g. $python [filename].py {args}
if __name__ == "__main__":
	# execute something that may contain {args}
	main(sys.argv)
