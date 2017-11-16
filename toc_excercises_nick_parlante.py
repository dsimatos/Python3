#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Extract table of contents from 'Exercises from Nick Parlante'
'''

import sys, string

def toc():
    fi = open('/home/dion/Documents/Python/Materials_for_thesis/Excercises-nick_parlante', 'rU')
    fo = open('/home/dion/Documents/Python/Materials_for_thesis/Excercises-nick_parlante_TOC', 'w')
    for line in fi:
        if line[0] in string.ascii_uppercase and line[1]=='.':
            fo.write(line)
        if line[0] in string.digits:
            if 'SOLUTION' in line:
                pass
            else:
                fo.write('   '+line)
    fi.close()
    fo.close()

if __name__ == '__main__':
    toc()
