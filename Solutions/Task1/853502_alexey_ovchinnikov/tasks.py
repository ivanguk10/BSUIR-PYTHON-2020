import random
import argparse
import re


def word_count(text: str) -> dict:
    words = re.split('[^a-zA-Zа-яА-Я0-9]', text)
    stats = dict()
    for word in words:
        if word.lower() in stats.keys():
            stats[word.lower()] += 1
        else:
            stats[word.lower()] = 1
    stats.pop('')
    return stats

def repeat(words: dict) -> str:
    sorted_values = [value[0] for value in sorted(words.items(), key=lambda x: x[1], reverse=True)]
    sorted_values[0] = sorted_values[0].capitalize()
    sorted_values[len(sorted_values)-1] += '.'
    return ' '.join(sorted_values)

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
parser.add_argument('-p','--problem', choices=['count', 'sort', 'fibonacci'], default='count')
parser.add_argument('-s','--sort', choices=['quick', 'merge'])
parser.add_argument('-fn', '--filename', choices=['text_data.txt', 'data.txt'], default='data.text')
parser.add_argument('-fib', '--fibonacci', choices=['20', '50', '100', '150'], default='8')
args = parser.parse_args()
problem = args.problem
fib_num = args.fibonacci
sort = args.sort
file_name = args.filename

if problem == 'count' or problem == 'repeat':
    string = open_text(file_name)
    if problem == 'count':
        stats = word_count(string)
    for (key, value) in stats.items():
            print(key, ':', value)
    print('Sentence made of the most common words in sequence:', repeat(stats))
elif problem == 'sort':
    arr = open_data(file_name)
    if sort == 'quick':
        if arr[0] > arr[len(arr)-1]:
            arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
        quick_sort(arr, arr[0], len(arr)-1)
        print(arr)
    else:
        arr = merge_sort(arr)
        print(arr)  
elif problem == 'fibonacci':
    # num = random.randint(20,25)
    for n in fibonacci(int(fib_num)):
        print(n)

