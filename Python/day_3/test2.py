import sys

def counter(a,b):
    unic_list = []
    for i in str(b):
        if i in str(a) and i not in unic_list:
            unic_list.append(i)
    return len(unic_list)


if __name__ == '__main__':

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(counter(a,b))


