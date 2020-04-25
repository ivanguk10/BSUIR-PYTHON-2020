from tempfile import TemporaryFile
from re import findall
from random import random


def merge_files(file_1, file_2, result):
    line_from_file_1 = file_1.readline()
    line_from_file_2 = file_2.readline()

    while line_from_file_1 != '' and line_from_file_2 != '':

        number_1 = int(line_from_file_1[0:-1])
        number_2 = int(line_from_file_2[0:-1])

        if number_1 < number_2:
            result.write(line_from_file_1)
            line_from_file_1 = file_1.readline()
        else:
            result.write(line_from_file_2)
            line_from_file_2 = file_2.readline()

    while line_from_file_1 == '' and line_from_file_2 != '':
        result.write(line_from_file_2)
        line_from_file_2 = file_2.readline()

    while line_from_file_1 != '' and line_from_file_2 == '':
        result.write(line_from_file_1)
        line_from_file_1 = file_1.readline()

    result.seek(0)


def is_end_character(char: str):
    return char == '\n' or char == ' ' or char == ''


class ExternalSorter:
    def __init__(self, sorted_file, output_file_name='output.txt',
                 max_temp_files=10000, block_size=1024):
        self.sorted_file = sorted_file
        self.output_file_name = output_file_name
        self.max_temp_files = max_temp_files
        self.block_size = block_size

        self._file_is_read = False
        self._temp_files = list()

    def __read_block(self):
        string = self.sorted_file.read(self.block_size)

        while not is_end_character(char := self.sorted_file.read(1)):
            string += char
        else:
            string += char
            if char == '':
                self._file_is_read = True

        array = [int(i) for i in findall(r'(-?[\d]+)', string)]
        return array

    def __sort_insert_block(self):
        array = self.__read_block()
        array.sort()

        temp_file = TemporaryFile(mode='r+')
        if len(array) != 0:
            temp_file.write('\n'.join(str(i) for i in array) + '\n')

        temp_file.seek(0)
        self._temp_files.insert(0, temp_file)

    def __merge_two_temp_files(self):
        result = TemporaryFile(mode='r+')

        merge_files(self._temp_files[0], self._temp_files[1], result)

        self._temp_files[0].close()
        self._temp_files[1].close()

        del self._temp_files[1]
        del self._temp_files[0]

        self._temp_files.append(result)

    def external_sort(self):
        while not self._file_is_read:
            while len(self._temp_files) < self.max_temp_files and not self._file_is_read:
                self.__sort_insert_block()

            current_len = len(self._temp_files) // 2

            for i in range(current_len):
                self.__merge_two_temp_files()

        while len(self._temp_files) > 1:
            self.__merge_two_temp_files()

        with open(self.output_file_name, 'w+') as output_file:
            while line := self._temp_files[0].readline():
                output_file.write(line)
