#!/urs/bin/python

import sys

def fib(n):
    fibo_list = [0, 1]
    for i in range(2, n+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list[n]


if __name__=="__main__":
    n = int(sys.argv[1])
    print(fib(n))
