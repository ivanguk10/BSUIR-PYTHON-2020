from random import randint


def create_files(number):
    """Generate random number sequence in file
        Create result file
    """

    with open('numbers.txt', 'w') as f, open('result.txt', 'w+'):
        f.writelines('{}\n'.format(randint(-1000000, 1000000)) for x in range(number))
