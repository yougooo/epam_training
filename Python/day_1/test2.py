#!/usr/bin/python

import sys
import math

def calc(x,m,g):
    return (1/g*math.sqrt(2*math.pi))*math.exp(-((x-m)**2/2*m**2))


if __name__=='__main__':
    x = float(sys.argv[1])
    m = float(sys.argv[2])
    g = float(sys.argv[3])

    print(calc(x,m,g))
