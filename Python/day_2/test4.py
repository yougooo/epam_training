#!/usr/bin/python


import sys


def chocolate(n,m,k):
    s = n*m
    return 'YES' if any([s%k == n, s%k == m]) else 'NO'


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    k = int(sys.argv[3])

    print(chocolate(n,m,k))

