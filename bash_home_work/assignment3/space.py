#!/usr/bin/python

import sys

def main():
    data = sys.argv[1].split('\n')
    return '\n'.join([len(link.split()[1].split('/'))*' '+link for link in data])


if __name__=='__main__':
    print(main())

