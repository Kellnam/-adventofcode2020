def open_file_to_list(path):
    with open(path, 'r') as numbers:
        list1 = []
        for line in numbers:
            list1.append(line)
    return list1


def day1part1(path):
    """
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
    :param path:
    :return:
    """
    list1 = open_file_to_list(path)
    for left in list1:
        for walk in list1:
            if int(left) + int(walk) == 2020:
                return int(left) * int(walk)


def day1part2(path):
    """
    They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
    :param path:
    :return:
    """
    list1 = open_file_to_list(path)
    for a in list1:
        for b in list1:
            for c in list1:
                if int(a) + int(b) + int(c) == 2020:
                    return int(a) * int(b) * int(c)


if __name__ == "__main__":
    print('Day 1 part1 solution: ', day1part1('numbers'))
    print('Day 1 part2 solution: ', day1part2('numbers'))
