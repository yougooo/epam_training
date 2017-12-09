import sys


def clean_list(list_to_clean):
    float_bicycle = map(lambda x: x+0.1 if isinstance(x,float) else x, list_to_clean)
    total_unic = list(set(float_bicycle))
    total_unic = map(lambda x: x-0.1 if isinstance(x,float) else x, total_unic)
    return total_unic


if __name__ == "__main__":

    test_set = [[1,1.,'1',-1,1], ['qwe','reg', 'qwe','REG'],
                [32,32.1,32.0,-123], [1,2,1,1,3,4,5,4,6,'2',7,8,9,0,1,2,3,4,5]]

    for test in test_set:
        print(clean_list(test))

