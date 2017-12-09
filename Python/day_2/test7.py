#!/usr/bin/python


import sys

def main(x,p,y):
    counter = 0
    while x < y:
        x = x + x * p/100.0
        counter += 1
        x = int(x)
    return counter

if __name__ == "__main__":
    x = int(sys.argv[1])
    p = int(sys.argv[2])
    y = int(sys.argv[3])
    print(main(x,p,y))

