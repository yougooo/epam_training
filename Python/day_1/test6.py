#!/usr/bin/python

import sys


def polindrom_check(word):
    word = word.lower()
    word = word.replace(' ','')
    return 'YES' if word == word[::-1] else 'NO'


if __name__=='__main__':
    word = sys.argv[1]
    print(polindrom_check(word))
