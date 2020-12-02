from allDays.read_input import open_file_to_list


def day2part1(path):
    list1 = open_file_to_list(path)
    counter = 0
    for i in list1:
        pw_split = i.split()
        min_max_split = pw_split[0].split('-')
        if int(min_max_split[0]) <= pw_split[2].count(pw_split[1][0]) <= int(min_max_split[1]):
            counter += 1
    return counter
