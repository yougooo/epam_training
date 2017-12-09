#!/usr/bin/python


import sys


def list_maker(number, start_list=[0,0,0,0,0,0]):
    """
    number:: int, in range 0-999999
    start_list:: represent digit by item, 1000 -> [0,0,1,0,0,0]
    """
    for i in range(1, len(str(number))+1):
        start_list[-i] = int(str(number)[-i])
    return start_list


def ticket_gen(n_start, n_end):
    for i in range(n_start, n_end+1):
        yield list_maker(i)


def check_luck(gen):
    """
    gen:: generator object from function ticket_gen
    return:: counted luck ticket and list with this ticket
    """
    lack_list = []
    for digit in gen:
        if sum(digit[:3]) == sum(digit[3:]):
            lack_list.append(''.join([str(i) for i in digit]))
    return len(lack_list), lack_list



if __name__ == "__main__":
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    tikets = ticket_gen(start,end)
    print(check_luck(tikets))

