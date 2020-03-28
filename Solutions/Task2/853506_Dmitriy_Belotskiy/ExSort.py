import tempfile
import random
from collections import deque


class ExSort:

    def __init__(self, lf, lr):
        self.Q = deque()
        self.LINES_IN_FILE = lf
        self.LINES_TO_READ = lr

    def create_file(self):
        numbers = [random.randint(-1000000, 1000000) for _ in range(self.LINES_IN_FILE)]
        with open('numbers.txt', 'w') as f:
            f.writelines('{}\n'.format(number) for number in numbers)

    def split_file(self):
        with open('numbers.txt', 'r') as file:
            lines = self.read_lines(file)
            for numbers in lines:
                temp = tempfile.TemporaryFile(mode='w+t')
                self.Q.append(temp)
                temp.writelines(["".join([str(num), '\n']) for num in sorted(numbers)])

    def read_lines(self, file):  # Генератор
        offset = 0
        while True:
            lines = []
            file.seek(offset)
            i = 0
            while i < self.LINES_TO_READ:
                temp_str = file.readline()
                i += 1
                if temp_str == '' or temp_str == '\n':
                    i = self.LINES_TO_READ
                    break
                lines.append(temp_str)
            offset = file.tell()
            if lines:
                numbers = [int(line) for line in lines if line != '']
                yield numbers
            else:
                file.close()
                return

    def merge_files(self, file1, file2):
        line_gen1 = self.read_lines(file1)
        line_gen2 = self.read_lines(file2)
        lines1 = next(line_gen1)
        lines2 = next(line_gen2)
        temp = tempfile.TemporaryFile(mode='w+t')
        self.Q.append(temp)
        i, j = 0, 0
        while True:
            new_list = []
            while i < len(lines1) and j < len(lines2):
                if lines1[i] < lines2[j]:
                    new_list.append(lines1[i])
                    i += 1
                else:
                    new_list.append(lines2[j])
                    j += 1
            temp.writelines([''.join([str(s), '\n']) for s in new_list])
            if len(lines1) != i:
                try:
                    lines2 = next(line_gen2)
                    j = 0
                except StopIteration:
                    temp.writelines([''.join([str(s), '\n']) for s in lines1[i:]])
                    for lines in line_gen1:
                        temp.writelines([''.join([str(s), '\n']) for s in lines])
                    return
            elif len(lines2) != j:
                try:
                    lines1 = next(line_gen1)
                    i = 0
                except StopIteration:
                    temp.writelines([''.join([str(s), '\n']) for s in lines2[j:]])
                    for lines in line_gen2:
                        temp.writelines([''.join([str(s), '\n']) for s in lines])
                    return

    def merge_sort(self):
        while len(self.Q) >= 2:
            self.merge_files(self.Q.popleft(), self.Q.popleft())
        with open('result', 'w') as f:
            line_gen = self.read_lines(self.Q.popleft())
            for lines in line_gen:
                f.writelines([''.join([str(s), '\n']) for s in lines])
                if not lines:
                    return