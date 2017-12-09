
# python 3

import sys
from itertools import groupby


def define_students(n_pupil):
    student_dict = {}
    for i in range(n_pupil):
        name = input('Enter student name: ')
        count_lang = int(input('Enter numbers of lang: '))
        student_dict[name] = [input('lang: ') for i in range(count_lang)]
    return student_dict


def lang_output(student_dict):
    total_lang_list = []

    for val in student_dict.values():
        total_lang_list.extend(val)

    lang_dict = {lang+'\n':len(list(lang_list)) for lang,lang_list
                 in groupby(sorted(total_lang_list))}

    well_know_lang = [lang+'\n' for lang,count in lang_dict.items()
                      if count == len(student_dict)]

    return (well_know_lang, set(list(lang_dict.keys())))



if __name__ == "__main__":
    pupil = int(input("Enter number of students: "))

    student = define_students(pupil)
    well_lang, dif_lang = lang_output(student)

    print("Evreone students know {} language(-s):\n{}".format(str(len(well_lang)), ''.join(well_lang)))
    print("All language(-s) in student group is {}:\n{}".format(str(len(dif_lang)), ''.join(dif_lang)))


