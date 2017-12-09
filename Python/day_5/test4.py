import sys


def fs(file_st):
    lines = file_st.split('\n')
    file_system_dict = {}

    for line in lines:
        temp = line.split()
        file_system_dict[temp[0]] = temp[1:]

    return file_system_dict


def permmision_cheker(permmision_dict ,nfile, action):
    try:
        return 'OK' if action[0].upper() in permmision_dict[nfile] else 'Access denied'
    except KeyError:
        return 'File not in filesystem'


if __name__ == "__main__":
    test_fs = """helloworld.exe R X
              pinglog W R
              nya R
              goodluck X W R"""

    permmission = fs(test_fs)
    print permmision_cheker(permmission, 'nya', 'write')
    print permmision_cheker(permmission, 'goodluck', 'write')
    print permmision_cheker(permmission, 'ny', 'write')
    print permmision_cheker(permmission, 'pinglog', 'read')
    print permmision_cheker(permmission, 'nya', 'execute')

