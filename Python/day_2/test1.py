#!/usr/bin/python


import sys
import re


def main(b):
    # bad solution) improve soon
    if all([len(b) == 2, b.startswith('('),b.endswith(')')]):
           return 'YES'
    pattern = re.compile('^\(.+\)$')
    return 'YES' if all([b.count('(')==b.count(')'),pattern.match(b)]) else 'NO'


if __name__ == "__main__":
    brackets = sys.argv[1]
    print(main(brackets))

