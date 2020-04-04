from tempfile import TemporaryFile
from re import findall


def merge_files(file_1, file_2, result):
    """Merges two temp files into one.

    Merges two sorted files file_1 and file_2 into sorted result file.
    File_1 and file_2 must be one integer one line format.

    Arguments:
        file_1(TemporaryFile): first temp file to merge.
        file_2(TemporaryFile): second file to merge.
        result(file): result file.
    """
    line_1 = file_1.readline()
    line_2 = file_2.readline()

    while line_1 != '' and line_2 != '':

        if int(line_1[0:-1]) < int(line_2[0:-1]):
            result.write(line_1)
            line_1 = file_1.readline()
        else:
            result.write(line_2)
            line_2 = file_2.readline()

    while line_1 == '' and line_2 != '':
        result.write(line_2)
        line_2 = file_2.readline()

    while line_1 != '' and line_2 == '':
        result.write(line_1)
        line_1 = file_1.readline()

    result.seek(0)


def is_end_character(char):
    """Check end of line symbol.

        Returns True, if char is end of line symbol ('\n' or ' ' or ''),
        otherwise False.

        Arguments:
            char(str): symbol to check.

        Return:
            result(bool): result of checking.
        """
    return char == '\n' or char == ' ' or char == ''


class ExternalSorter:
    """Class represents options to external sort.

     Class has methods to implement external sort.

     Attributes:
        sorted_file(file): external sorting file,
        output_file_name(str): name of resulting sorted file.
        max_temp_files(int): the biggest amount of opened at the same time files.
        block_size(int): maximum characters amount in one read block.

    """
    def __init__(self, sorted_file, output_file_name='result.txt',
                 max_temp_files=1000, block_size=1024):
        """Constructor

        Constructor sets initial data.

        Arguments:
            sorted_file(file): external sorting file,
            output_file_name(str): name of resulting sorted file.
            max_temp_files(int): the biggest amount of opened at the same time files. Default: 1000.
            block_size(int): maximum characters amount in one read block. Default: 1024.
        """
        self.sorted_file = sorted_file
        self.output_file_name = output_file_name
        self.max_temp_files = max_temp_files
        self.block_size = block_size

        self._file_is_read = False
        self._temp_files = list()

    def __read_block(self):
        """Read one block of sorted_file.

        Reads block_size characters of sorted_file and
        converses them into list of integers.

        Returns:
             array(list): list of read integers.
        """
        string = self.sorted_file.read(self.block_size)
        char = self.sorted_file.read(1)

        while not is_end_character(char):
            string += char
            char = self.sorted_file.read(1)
        else:
            string += char
            if char == '':
                self._file_is_read = True

        array = [int(i) for i in findall(r'(-?[\d]+)', string)]
        return array

    def __sort_insert_block(self):
        """Sort list of numbers.

        Sort and write in TemporaryFile list of numbers.
        Then insert TemporaryFile at list of temporary files.
        """
        array = self.__read_block()
        array.sort()

        temp_file = TemporaryFile(mode='r+')
        if len(array) != 0:
            temp_file.write('\n'.join(str(i) for i in array) + '\n')

        temp_file.seek(0)
        self._temp_files.insert(0, temp_file)

    def __merge_two_temp_files(self):
        """Merges two temp files into one.

        Merges two temp files into one.
        Deletes merged files.
        Append result file at list.
        """
        result = TemporaryFile(mode='r+')

        merge_files(self._temp_files[0], self._temp_files[1], result)

        self._temp_files[0].close()
        self._temp_files[1].close()

        del self._temp_files[1]
        del self._temp_files[0]

        self._temp_files.append(result)

    def external_sort(self):
        """
        Sorts file.

        Externally sorts file.
        Save result into output file.
        """
        while not self._file_is_read:
            while len(self._temp_files) < self.max_temp_files and not self._file_is_read:
                self.__sort_insert_block()

            current_len = len(self._temp_files) // 2

            for i in range(current_len):
                self.__merge_two_temp_files()

        while len(self._temp_files) > 1:
            self.__merge_two_temp_files()

        with open(self.output_file_name, 'w+') as output_file:

            line = self._temp_files[0].readline()
            while line:
                output_file.write(line)
                line = self._temp_files[0].readline()
