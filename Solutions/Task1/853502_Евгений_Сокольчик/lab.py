import re
import argparse

def generator(first = 0, second = 1):
    while second < 100:
        temp = second
        second += first
        first = temp
        yield first

def fibonacci():
    f = generator()
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
        while list[i] < pivot and i < last:
            i += 1
        while list[j] > pivot and j > first:
            j -= 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i += 1
            j -= 1
    if first < j:
        quick_sort(list, first, j)
    if i < last:
        quick_sort(list, i, last)

def text(task, file):
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
        for item in words.items():
            print(str(item[1]) + " " + item[0])
    else:
        words = sorted(words.items(), key=lambda pair: pair[1], reverse = True)
        sentence = []
        for word in list(words) [:10]:
            sentence.append(word[0])
        sentence[0] = sentence[0].capitalize()
        sentence[9] += "."
        print(" ".join(sentence))

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
    parser.add_argument("-f", "--file", default="text.txt")
    return parser

parser = create_parser()
params = parser.parse_args()
task = params.task
file = params.file
if task == "list" or task == "sentence":
    text(task, file)
elif task == "quick_sort" or task == "merge_sort":
    sort(task, file)
else:
    fibonacci()