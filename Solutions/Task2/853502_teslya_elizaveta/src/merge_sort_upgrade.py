import os


def splitting():
    """Merge two strings until gets result.

    Merge two strings and append result this file.
    """
    n = 1
    with open('numbers.txt', 'r+') as f:
        f.readline()
        seek_2 = f.tell()
    seek_1 = 0

    while seek_1 != seek_2:
        print(n)
        n += 1
        with open('numbers.txt', 'r+') as f, open('numbers.txt', 'r+') as f_2:
            f.seek(seek_1)
            f_2.seek(seek_2)
            seek_1, seek_2 = merge(f, f_2)

    make_result_file(seek_1)


def merge(left, right):
    """Merge two strings by symbols.

    Merge two strings until it meets symbol '\n'

    Arguments:
        left(file): the first file pointer
        right(file): the second file pointer

    Return:
        files[0].tell()(int): the first index for file[0].seek()
        files[1].tell()(int): the first index for file[1].seek()

    """
    with open('numbers.txt', 'a+') as sorted_numbers, open('numbers.txt', 'r+') as f, open('numbers.txt', 'r+') as f_2:

        files = [f, f_2]
        files[0].seek(left.tell())
        files[1].seek(right.tell())

        strings = ['', '']

        sym1 = files[0].read(1)
        sym2 = files[1].read(1)
        symbols = [sym1, sym2]

        while True:

            while symbols[0] != ' ' and symbols[0] != '\n':
                strings[0] += symbols[0]
                symbols[0] = files[0].read(1)

            while symbols[1] != ' ' and symbols[1] != '\n':
                strings[1] += symbols[1]
                symbols[1] = files[1].read(1)

            if int(strings[0]) <= int(strings[1]):
                index = 0
            else:
                index = 1

            strings[index] += ' '
            sorted_numbers.write(strings[index])
            strings[index] = ''

            if symbols[index] != '\n':
                symbols[index] = files[index].read(1)
            else:
                sorted_numbers.write(strings[1 - index])
                while symbols[1 - index] != '\n':
                    sorted_numbers.write(symbols[1 - index])
                    symbols[1 - index] = files[1 - index].read(1)

                sorted_numbers.write(symbols[1 - index])
                symbols[1 - index] = files[1 - index].read(1)
                break

        files[0].readline()
        files[1].readline()
        return files[0].tell(), files[1].tell()


def make_result_file(seek_file):
    """Write result

    Write result in result file and delete temp file.

    Arguments:
        seek_file(int):
    """
    with open('numbers.txt', 'r') as f, open('result.txt', 'w') as result_file:
        f.seek(seek_file)
        result_file.write(f.readline().replace(' ', '\n'))
    os.remove('numbers.txt')
