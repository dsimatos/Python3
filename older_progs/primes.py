#! /usr/bin/env python
def primes(k=10):
	for n in range(2,k):
		for x in range(2,n):
			if n%x==0:
				break
		else:
			print n,
			
if __name__ == '__main__':
	import sys
	primes(int(sys.argv[1]))
