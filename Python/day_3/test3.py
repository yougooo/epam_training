import sys


def super_fibonacci(n,m):
    if m > n:
        return 1

    start_fib = [1 for i in range(m)]

    for i in range(n-m):
        start_fib.append(sum(start_fib[i:m+i]))

    return start_fib[-1]


if __name__ == "__main__":

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    print(super_fibonacci(n,m))



