#!/usr/bin/env python3

''' 
    Result of the fraction 1/N where N is an integer
    If second argument (optional) is 'len', returns length of repeated digits
    
    Examples :
    recur(0)->nan,          recur(1)->0,
    recur(2)->0.5,          recur(2, 'len')->0,
    recur(3)->0.(3),        recur(3, 'len')->1,
    recur(4)->0.25,         recur(4, 'len')->0,
    recur(6)->0.1(6),       recur(6, 'len')->1,
    recur(14)->0.0(714285), recur(14, 'len')->6
    
    Code translated from R from site http://r.prevos.net/euler-problem-26/
'''

import math, sys

# recur <- function(x, output = "") {
def recur(N, output=''):
    
    # Prepare variable
    N = int(N)
    if N == 0:
        return(float('nan'))
    if N == 1:
        return(0)
    N = math.floor(abs(N))
    
    # Initiate vectors to store decimals and remainders
    dec = []
    rem = []
    
    # Initiate values
    r = 10
    rem.append(r)
    
    # Long division
    while True:
        dec.append(math.floor(r / N))
        r = 10 * (r % N)
        # Test wether the number is terminating or repeating
        if r == 0 or r in rem:
            break
        rem.append(r)
    
    # Determine number of recurring digits
    if r != 0:
        rep = len(rem) - rem.index(r)
    else:
        rep = 0
    
    # Output
    if output == 'len':
        if __name__ == '__main__':
            print(rep)
            return
        else:
            return(rep)
    else:
        if rep != 0:
            if rep == len(dec):
                l = ['(']
            else:
                l = []
                for i in dec[0 : len(dec) - rep]:
                    l.append(i)
                l.append('(')
            dec1 = []
            for i in l:
                dec1.append(i)
            for i in dec[len(dec) - rep : len(dec)]:
                dec1.append(i)
            dec1.append(')')
            dec1.insert(0, '0.')
        else:
            dec1 = dec[:]
            dec1.insert(0, '0.')
        
        s = ''.join([str(x) for x in dec1])
        if __name__ == '__main__':
            s = '1/' + str(N) + '=' + s
            print(s)
            return
        else:
            return(s)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        if len(sys.argv) == 2:
            output = ''
        else:
            output = sys.argv[1]
        for N in sys.argv[1 : -1]:
            recur(N, output)
    else:
        print("Usage : recur <N> [<N>...] ['len']|'char(s) if multiple numbers before'")
        print("where N the denominator of 1/N")
