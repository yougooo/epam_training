#!/usr/bin/python


import sys


def main(n):
    if n > 9 or n < 0:
        return 'n must be n <= 9 and n > 0'
    line = []
    line_s = ''
    for i in range(1,n+1):
        line_s = line_s + str(i)
        line.append(line_s)
    return '\n'.join(line)


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(main(n))

