#!/usr/bin/python

import sys


def spacer(line):
    """
    line:: like 'File: /path/to/file has 0 line'
    return string with spaces.
    """
    return ' '*len(line.split()[1].split('/'))


def base_name(line):
    """
    line:: like 'File: /path/to/file has 0 line'
    return line like 'File file has 0 line'
    """
    temp = line.split()
    temp[1]=temp[1].split('/')[-1]
    return ' '.join(temp)


def main():
    data = sys.argv[1].split('\n')
    return '\n'.join([spacer(link)+base_name(link) for link in data])


if __name__=='__main__':
    print(main())

