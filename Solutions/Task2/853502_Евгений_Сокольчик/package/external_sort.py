import tempfile

def merge(files, output_file):
    for (file_1, file_2) in zip(files[::2], files[1::2]):
        num_1 = file_1.readline()
        num_2 = file_2.readline()
        file = tempfile.TemporaryFile("w+t")
        while num_1 != "" or num_2 != "":
            if not num_1 and num_2:
                file.write(num_2)
                num_2 = file_2.readline()
            elif num_1 and not num_2:
                file.write(num_1)
                num_1 = file_1.readline()
            elif int(num_1) >= int(num_2):
                file.write(num_2)
                num_2 = file_2.readline()
            elif int(num_1) < int(num_2):
                file.write(num_1)
                num_1 = file_1.readline()
        file.seek(0)
        i = files.index(file_1)
        files[i].close()
        files[i + 1].close()
        files[i:i + 2] = [file]
    if len(files) > 1:
        merge(files, output_file)
    else:
        with open(output_file, "w") as result:
            lines = files[0].readlines()
            result.writelines(lines)
            files[0].close()

def to_file(nums, files):
    file = tempfile.TemporaryFile("w+t")
    for num in map(str, nums):
        file.write(num + "\n")
    file.seek(0)
    files.append(file)
    nums.clear()

def external_sort(input_file, output_file, size):
    with open(input_file) as file:
        files = []
        nums = []
        count = 0
        num = file.readline()
        while num != "":
            nums.append(int(num))
            count += 1
            if count % size == 0:
                nums.sort()
                to_file(nums, files)
                count = 0
            num = file.readline()
        nums.sort()
        to_file(nums, files)
        merge(files, output_file)