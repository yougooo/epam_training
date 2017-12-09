import sys


def st_long(s):
    dict_index = {len(key):key for key in s.split()}
    return dict_index[max(dict_index.keys())]


if __name__ == '__main__':
    s = sys.argv[1]
    print(st_long(s))

