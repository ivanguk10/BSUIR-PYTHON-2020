import random
import tempfile
import sys


def create_file(filename) -> None:
    n = 50000
    with open(filename, 'w+') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(n))


class ExternalMergeSort:
    _small_file_size = 1000

    def __init__(self, filename):
        self.filename = filename
        self._small_files_list = []

    def __del__(self):
        for file in self._small_files_list:
            file.close()

    def _split_files(self) -> None:
        try:
            with open(self.filename, 'r') as file:
                while lines := file.readlines(self._small_file_size):
                    t_file = tempfile.NamedTemporaryFile('w+t', prefix='t_')
                    t_file.writelines(sorted(lines, key=lambda x: int(x.strip())))
                    self._small_files_list.append(t_file)
        except:
            print('Exception' + str(sys.exc_info()[0]) + 'occured.')

    def _merge(self) -> None:
        numbers = {}
        try:
            with open(self.filename, 'w') as file:
                for small_file in self._small_files_list:
                    small_file.seek(0)
                    numbers.update({int(small_file.readline().strip()): small_file})
                while numbers:
                    min_number = min(numbers.keys())
                    min_file = numbers[min_number]
                    if new_number := min_file.readline().strip():
                        numbers.update({int(new_number): min_file})
                    file.write(str(min_number) + '\n')
                    del numbers[min_number]
        except:
            print('Exception ' + str(sys.exc_info()[0]) + ' occured.')

    def merge_sort(self) -> None:
        self._split_files()
        self._merge()

    pass


if __name__ == '__main__':
    filename = 'numbers.txt'
    create_file(filename)
    obj = ExternalMergeSort(filename)
    obj.merge_sort()
