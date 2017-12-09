import sys
import re

memo_dict = {'-':0,'0':1,'1':0,'2':0,'3':0,'4':1,'5':0,'6':1,'7':0,'8':2,'9':1}
#pattern = re.compile('^-?[1-9][0-9]*$') # only for 100% digit
pattern = re.compile('([1-9][0-9]*)') # for string with digit

def count_holes(digit):
    if isinstance(digit, float):
        return 'Input Error'
    digit = str(digit)
    find = pattern.findall(digit)
    if find != []:
        find = ''.join(find)
        return sum([memo_dict[i] for i in find])
    return 'Input Error'

digit_pattern = re.compile('^-?[1-9][0-9]*$') # only for 100% digit

def only_digit_holes(digit):
    digit = str(digit)
    if digit_pattern.match(digit):
        return sum([memo_dict[i] for i in digit])
    return 'Input Error'


if __name__ == "__main__":

    data = sys.argv[1]
    print(only_digit_holes(data))
    print(count_holes('123'))
    print(count_holes(906))
    print(count_holes('001'))
    print(count_holes(-8))
    print(count_holes(-8.0))

