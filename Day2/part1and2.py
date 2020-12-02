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


def day2part2(path):
    list1 = open_file_to_list(path)
    counter = 0
    for i in list1:
        pw_split = i.split()
        min_max_split = pw_split[0].split('-')
        if pw_split[1][0] == pw_split[2][int(min_max_split[0]) - 1] or pw_split[1][0] == pw_split[2][int(min_max_split[1]) - 1]:
            if not (pw_split[1][0] == pw_split[2][int(min_max_split[0]) - 1] and pw_split[1][0] == pw_split[2][int(min_max_split[1]) - 1]):
                counter += 1
        # print('char: ',pw_split[1][0],' first char: ', pw_split[2][int(min_max_split[0]) - 1], ' second char: ', pw_split[2][int(min_max_split[1]) - 1], 'counter: ', counter)

    return counter
