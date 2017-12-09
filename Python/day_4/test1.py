import sys

if __name__ == '__main__':
    st = sys.argv[1]
    print(st)
    print(st.encode('UTF-8'))
    print(bytes(st, encoding='CP1251'))

