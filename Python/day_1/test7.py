#!/usr/bin/python


import sys


def polindrom_maker():
    word_list = sys.argv[1:]
    return ' '.join(word_list[::-1])


if __name__=='__main__':
    print(polindrom_maker())


