import time
import os
from src.create_numbers import create_files


def merge_write():
    """Merge two files into one

    Merge two files by symbols.
    """
    with open('numbers.txt', 'w') as file_a, open('numbers_merge_sort_1.txt', 'r') as file_b,\
            open('numbers_merge_sort_2.txt', 'r') as file_c:

        i = file_b.readline()
        j = file_c.readline()

        while True:

            if i == '' and j == '':
                break

            if i == '':
                file_a.write(j)
                file_a.writelines(file_c.readlines())
                break

            if j == '':
                file_a.write(i)
                file_a.writelines(file_b.readlines())
                break

            if (int(i[:-1])) < (int(j[:-1])):
                file_a.write(i)
                i = file_b.readline()

            else:
                file_a.write(j)
                j = file_c.readline()


def merge_read():
    """Write increasing subsequences

    Write increasing subsequences into two file from one.
    """
    with open('numbers.txt', 'r') as file_a, open('numbers_merge_sort_1.txt', 'w') as file_b,\
            open('numbers_merge_sort_2.txt', 'w') as file_c:

        value = file_a.readline()
        files = (file_b, file_c)

        order = 0
        files[order].write(value)
        value = int(value[:-1])

        for i in file_a.readlines():

            value_2 = int(i[:-1])
            if value <= value_2:
                files[order].write(i)
            else:
                order = 1 - order
                files[order].write(i)
            value = value_2


def merge_sort():
    """Merge sort

    Splits and merges files until it becomes
    one increasing sequence. Then delete temp files.
    """
    while True:

        merge_read()
        merge_write()

        with open('numbers_merge_sort_1.txt', 'r') as file_b, \
                open('numbers_merge_sort_2.txt', 'r') as file_c:

            if file_b.readline() == '' or file_c.readline() == '':
                break

    os.remove('numbers_merge_sort_1.txt')
    os.remove('numbers_merge_sort_2.txt')
