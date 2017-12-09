#!/usr/bin/python


import sys

def card_num(n, c_list):
    return [i for i in range(1, n+1) if i not in c_list][0]


if __name__ == "__main__":
    n = int(sys.argv[1])
    card_list = [int(num) for num in sys.argv[2:]]
    print(card_num(n, card_list))
