#!/usr/bin/python


import sys
import string


key = 'aaaaabbbbbabbbaabbababbaaababaab'
memo_dict = {key[i:i+5]:string.ascii_lowercase[i] for i in range(26)}


def pick_up_ab(word):
    return ''.join(['b' if letter.isupper() else 'a' for letter in word])


def main(st):
    st = st.replace(' ', '')
    st = st[:len(st)-len(st)%5]
    group_list = [st[i:i+5] for i in range(0,len(st),5)]
    return ''.join([memo_dict[pick_up_ab(word)] for word in group_list])


if __name__ == "__main__":
    data = sys.argv[1]
    print(main(data))

