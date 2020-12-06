from allDays.read_input import open_file_to_list


def day4part1(path):
    list1 = open_file_to_list(path)
    start = 0
    passport_spitter = []
    for n in range(len(list1)):
        if start > 959:
            break
        index = list1.index('\n', start, len(list1))
        start = index + 1
        passport_spitter.append(index)

    count = 0
    ibegin = 0
    iend = passport_spitter[0]
    for i in range(len(passport_spitter)):  # len(passport_spitter)
        one_passport = []
        for n in range(ibegin, iend):
            arguments = list1[n].split()
            for k in arguments:
                one_passport.append(k)

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

    return count
