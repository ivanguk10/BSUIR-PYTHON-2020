import random
import argparse
import re


def word_count(task, string):
    dict_ = {}
    lst = string.replace('.', ' ').split()
    # lst = re.split('[^a-zA-Zа-яА-Я0-9]', string)
    for i in lst:
        dict_[i] = 0
        for j in lst:
            if i == j:
                dict_[i] += 1
    if task == 'count':
        print(dict_.items())
    elif task == 'repeat':
        for j in range(len(dict_)):
            if j == 10:
                break
            max = lst[0]
            for i in dict_:
                if dict_[max] <= dict_[i]:
                    max = i
                else:
                    while lst.count(max):
                        lst.remove(max)
            print(str(max) + '->' + str(dict_[max]))
            dict_.pop(max)

def quick_sort(arr, fst, lst):
    f = fst
    l = lst
    pivo = arr[(fst + lst) // 2]
    while f <= l:
        while arr[f] < pivo:
            f += 1
        while arr[l] > pivo:
            l -= 1
        if f <= l:
            arr[f], arr[l] = arr[l], arr[f]
            f += 1
            l -= 1
    if fst < l:
        quick_sort(arr, fst, l)
    if lst > f:
        quick_sort(arr, f, lst)

def merge(left, right):
    answer = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            answer.append(left[i])
            i += 1
        else:
            answer.append(right[j])
            j += 1
    while i < len(left):
        answer.append(left[i])
        i += 1
    while j < len(right):
        answer.append(right[j])
        j += 1
    return answer

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        avg = len(arr) // 2
        left = merge_sort(arr[:avg])
        right = merge_sort(arr[avg:])
        return merge(left, right)

def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

def open_text(file_name):
    with open(file_name) as file:
        string = file.read()
    return string

def open_data(file_name):
    arr = []
    with open(file_name) as file:
        for line in file:
            arr = arr + list(map(int, line.split()))
    return arr

parser = argparse.ArgumentParser()
parser.add_argument('-p','--problem', choices=['count', 'repeat', 'quick_sort', 'merge_sort', 'fibonacci'])
parser.add_argument('-fn', '--filename', choices=['text_data.txt', 'data.txt'], default='data.text')
args = parser.parse_args()
problem = args.problem
file_name = args.filename

if problem == 'count' or problem == 'repeat':
    string = open_text(file_name)
    if problem == 'count':
        word_count(problem, string)
    else:
        word_count(problem, string)
elif problem == 'quick_sort' or problem == 'merge_sort':
    arr = open_data(file_name)
    if problem == 'quick_sort':
        if arr[0] > arr[len(arr)-1]:
            arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
        quick_sort(arr, arr[0], len(arr)-1)
        print(arr)
    else:
        arr = merge_sort(arr)
        print(arr)
elif problem == 'fibonacci':
    num = random.randint(5,15)
    for n in fibonacci(num):
        print(n)
