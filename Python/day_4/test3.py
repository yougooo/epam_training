import sys
from itertools import groupby


def cool(s):
    index = s.find('#')
    number = s.replace('#', s[index-1])
    return number


def main(s):
    data = cool(s)
    group_list = [list(group) for item, group in groupby(data)]
    return ''.join([item[0] for item in group_list if len(item)>1])


if __name__ == '__main__':
    s = sys.argv[1]
    print(main(s))


