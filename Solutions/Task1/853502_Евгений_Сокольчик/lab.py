import re
import argparse

def generator(range, first = 0, second = 1):
    while second < range:
        temp = second
        second += first
        first = temp
        yield first

def fibonacci(range):
    f = generator(range)
    for num in f:
        print(num)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(list):
    if len(list) < 2:
        return list
    else:
        middle = len(list) // 2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)

def quick_sort(list, first, last):
    i,j = first, last
    pivot = list[(first + last) // 2]
    while i <= j:
        while list[i] < pivot:
            i += 1
        while list[j] > pivot:
            j -= 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    if first < j:
        quick_sort(list, first, j)
    if i < last:
        quick_sort(list, i, last)

def text(task, file, length = 0):
    with open(file, "r") as text:
        regexp = re.findall(r"\w+", text.read())
    words = dict()
    for word in regexp:
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    if task == "list":
        return words
    else:
        words = sorted(words.items(), key=lambda pair: pair[1], reverse = True)
        sentence = []
        if length > len(words):
            print("Max length is " + str(len(words)) + ".")
            length = len(words)
        elif length <= 0:
            return "Invalid length."
        for word in list(words) [:length]:
            sentence.append(word[0])
        sentence[0] = sentence[0].capitalize()
        sentence[length - 1] += "."
        return " ".join(sentence)

def sort(task, file):
    with open(file, "r") as nums:
        numbers = nums.read().split()
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    if task == "quick_sort":
        quick_sort(numbers, 0, len(numbers) - 1)
    else:
        numbers = merge_sort(numbers)
    print(numbers)

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", choices=["list", "sentence", "quick_sort", "merge_sort", "fibonacci"], default="fibonacci")
    parser.add_argument("-f", "--file", choices=["text.txt", "numbers.txt"], default="text.txt")
    parser.add_argument("-sl", "--sentence_length", default=10, type=int)
    parser.add_argument("-fr", "--fib_range", default=100, type=int)
    return parser

parser = create_parser()
params = parser.parse_args()
task = params.task
file = params.file
sentence_length = params.sentence_length
fib_range = params.fib_range
if task == "list":
    for item in text(task, file).items():
        print(str(item[1]) + " " + item[0])
elif task == "sentence":
    print(text(task, file, sentence_length))
elif task == "quick_sort" or task == "merge_sort":
    sort(task, file)
else:
    fibonacci(fib_range)
