#!/usr/bin/python

import sys

a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]


def triangle_check(a,b,c):
    if all([a + b > c, a + c > b, b + c > a]):
        return 'triangle'
    else:
        return 'not triagle'


if __name__=='__main__':
    print(triangle_check(a,b,c))

