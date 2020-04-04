import tempfile


def Sort(source_file_name: str):
    try:
        with open(source_file_name, 'r') as input_file:
            print("Start sorting...")
            Simple_Merge_Sort(input_file)
    except IOError:
        print("Wrong file name")


def Simple_Merge_Sort(input_file):
    amount_of_nums = 0
    with open("result_file.txt", "w") as res_file:
        for line in input_file:
            res_file.write(line)
            amount_of_nums += 1
    source_file = open("result_file.txt", 'r+')
    k: int = 1

    while k < amount_of_nums:
        temp_file_1 = tempfile.TemporaryFile('w+')
        temp_file_2 = tempfile.TemporaryFile('w+')
        num = source_file.readline()
        while num != '':
            for _ in range(k):
                if num != '':
                    temp_file_1.write(num)
                    num = source_file.readline()
            for _ in range(k):
                if num != '':
                    temp_file_2.write(num)
                    num = source_file.readline()
        source_file.seek(0)
        temp_file_1.seek(0)
        temp_file_2.seek(0)
        num_1 = temp_file_1.readline()
        num_2 = temp_file_2.readline()
        while num_1 != '' and num_2 != '':
            i = 0
            j = 0
            try:
                while i < k and j < k and num_1 != '' and num_2 != '':
                    if int(num_1) < int(num_2):
                        source_file.write(num_1)
                        num_1 = temp_file_1.readline()
                        i += 1
                    else:
                        source_file.write(num_2)
                        num_2 = temp_file_2.readline()
                        j += 1
                while i < k and num_1 != '':
                    source_file.write(num_1)
                    num_1 = temp_file_1.readline()
                    i += 1
                while j < k and num_2 != '':
                    source_file.write(num_2)
                    num_2 = temp_file_2.readline()
                    j += 1
            except ValueError as e:
                print("\nEXCEPTION:\tValueError: You can sort only numbers! Check your file please.")
                return
        while num_1 != '':
            source_file.write(num_1)
            num_1 = temp_file_1.readline()
        while num_2 != '':
            source_file.write(num_2)
            num_2 = temp_file_2.readline()
        source_file.seek(0)
        temp_file_1.close()
        temp_file_2.close()
        k *= 2
    print("Sorting finished")


if __name__ == "__main__":
    Sort("test_numbers.txt")
