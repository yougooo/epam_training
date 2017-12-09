#!/usr/bin/python

import sys
import math

def cacl_x(a,b):
    x = 'Input error'
    if all([a>=0, b>0]):
        x = math.sqrt(a*b)/(math.exp(a)*b) + a*math.exp(2*a/b)
    return x


if __name__=="__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])

    print(cacl_x(a,b))

