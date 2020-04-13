import tempfile
import os

class HeapqMerging:

    heap = []
    heapsize = 0

    def heapify(self, i: int):
        left_child, right_child = 2*i + 1, 2*i + 2

        if left_child < self.heapsize and self.heap[left_child][0] < self.heap[i][0]:
            self.heap[i], self.heap[left_child] = self.heap[left_child], self.heap[i]
            self.heapify(left_child)
        if right_child < self.heapsize and self.heap[right_child][0] < self.heap[i][0]:
            self.heap[i], self.heap[right_child] = self.heap[right_child], self.heap[i]
            self.heapify(right_child)

    def heap_push_pop(self):
        while self.heapsize > 1:
            returned_value = self.heap[0][0]
            next_value = next(self.heap[0][1])
            self.heap[0] = next_value, self.heap[0][1]
            self.heapify(0)
            yield returned_value

    def push(self, iter):
            next_value = next(iter)
            self.heap.append(tuple([next_value, iter]))
            self.heapsize += 1
            position = self.heapsize - 1
            while True:
                root_position = int((position - 1)/2) if position % 2 == 1 else int((position - 2)/2)
                if root_position < 0:
                    return True
                else:
                    if self.heap[root_position][0] > self.heap[position][0]:
                        self.heap[root_position], self.heap[position] = self.heap[position], self.heap[root_position]
                        position = root_position
                    else:
                        return True

    def __init__(self, *args):
        for iter in list(args):
            self.push(iter)

    def __iter__(self):
        return self.heap_push_pop()


class ExternalSort:
    ITERS = []

    # <editor-fold desc="Merging">

    def intsfromfile(f):
        try:
            while True:
                yield int(f.readline())
        except Exception:
            f.close()
            raise StopIteration

    def merging(resultPath: str):
        with open(resultPath, 'w') as result_file:
            result_list = []
            try:
                for x in HeapqMerging(*ExternalSort.ITERS):
                    result_list.append(str(x))
                    if len(result_list) >= 1000:
                        result_file.write('\n'.join(result_list))
                        result_file.write('\n')
                        result_list = []
            except RuntimeError:
                if len(result_list) != 0:
                    result_file.write('\n'.join(result_list))
            finally:
                result_file.close()
        return


    # </editor-fold>

    # <editor-fold desc="Sorting">

    def sort_and_save(integer_list: list):
        integer_list.sort(key=lambda i: int(i))
        t_f = tempfile.TemporaryFile()
        for i in integer_list:
            t_f.write(b'%i\n' % int(i))
        t_f.seek(0)
        ExternalSort.ITERS.append(ExternalSort.intsfromfile(t_f))

    def sorting(filePath: str):
        with open(filePath, 'r') as f:
            integer_list = []
            for line in f:
                if len(integer_list) != 250000:
                    integer_list.append(line)
                else:
                    ExternalSort.sort_and_save(integer_list)
                    integer_list.clear()
            else:
                ExternalSort.sort_and_save(integer_list)

    # </editor-fold>

    def sort_external(file_path, result_path):
        if not (os.path.exists(file_path)):
            raise FileNotFoundError('file not found')
        ExternalSort.sorting(file_path)
        ExternalSort.merging(result_path)