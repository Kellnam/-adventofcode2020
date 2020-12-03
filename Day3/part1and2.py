from allDays.read_input import open_file_to_list


def day3part1(path, row, column):
    list1 = open_file_to_list(path)
    list_start = 0
    x = 0
    counter = 0
    for n in range(list_start, list1.__len__(), column):
        # print(list1[n][x], ' and n: ', n, 'x: ', x)
        if list1[n][x] == '#':
            counter += 1
        x += row
        if x > 30:
            x = x % 31
    return counter


def day3part2(path):
    x1 = day3part1(path, 1, 1)
    x2 = day3part1(path, 3, 1)
    x3 = day3part1(path, 5, 1)
    x4 = day3part1(path, 7, 1)
    x5 = day3part1(path, 1, 2)

    return x1 * x2 * x3 * x4 * x5
