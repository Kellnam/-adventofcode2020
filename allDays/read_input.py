def open_file_to_list(path):
    with open(path, 'r') as numbers:
        list1 = []
        for line in numbers:
            list1.append(line)
    return list1
