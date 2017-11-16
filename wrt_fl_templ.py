#!/usr/bin/env python3
'''
    Write a file with the specific template
'''
import sys

def wrt_fl_templ(filename):
    with open(filename, 'w') as f:
        for i in range(1,21):
            f.write('-'*79+'\n')
            f.write(str(i)+'. \n')
            f.write('\n')
            f.write('\n')
            f.write(str(i)+'. SOLUTION\n')
            f.write('\n')
            f.write('\n')
    f.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: wrt_fl_templ <filename>')
        sys.exit(1)
    wrt_fl_templ(sys.argv[1])
