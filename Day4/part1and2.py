import re

from allDays.read_input import open_file_to_list


def is_good(key):
    argument = key.split(':')
    if argument[0] == 'byr' and 1920 <= int(argument[1]) <= 2002:
        return True
    if argument[0] == 'iyr' and 2010 <= int(argument[1]) <= 2020:
        return True
    if argument[0] == 'eyr' and 2020 <= int(argument[1]) <= 2030:
        return True
    if argument[0] == 'hgt':
        if re.findall("\\d{2}in", argument[1]):
            if 59 <= int(argument[1].replace("in", "")) <= 76:
                return True
        if re.findall("\\d{3}cm", argument[1]):
            if 150 <= int(argument[1].replace("cm", "")) <= 193:
                return True

    if argument[0] == 'hcl' and re.findall("#([a-f]|[0-9]){6}", argument[1]):
        return True
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if argument[0] == 'ecl' and (argument[1] in colors):
        return True
    if argument[0] == 'pid' and re.findall("^\\d{9}$", argument[1]):
        return True
    return False


def day4part1(path, part):
    list1 = open_file_to_list(path)
    start = 0
    passport_spitter = []
    for n in range(len(list1)):
        if start > 959:
            break
        index = list1.index('\n', start, len(list1))
        start = index + 1
        passport_spitter.append(index)

    ibegin = 0
    iend = passport_spitter[0]
    all_passport = []
    count = 0
    count_2 = 0
    for i in range(len(passport_spitter)):  # len(passport_spitter)
        one_passport = []
        for n in range(ibegin, iend):
            arguments = list1[n].split()
            for k in arguments:
                one_passport.append(k)
        all_passport.append(one_passport)
        all_conditions = []
        for u in one_passport:
            condition = u.split(':')
            all_conditions.append(condition[0])

        keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        if all(key in all_conditions for key in keys):
            count += 1

        ibegin = iend + 1
        if i + 1 >= len(passport_spitter):
            break
        iend = passport_spitter[i + 1]
    if part == 1:
        return count

    count_keys = 0
    for passport in all_passport:
        for keys in passport:
            if is_good(keys):
                count_keys += 1
        if count_keys == 7:
            count_2 += 1

        count_keys = 0
    return count_2
