import re

from allDays.read_input import open_file_to_list


def day6part1(path):
    declaration = open_file_to_list(path)
    count = 0
    chars = []

    for form in declaration:

        if re.findall('\w+\\n', form):
            for char in form:
                if not chars.count(char):
                    if char != '\n':
                        chars.append(char)
        else:
            count = count + len(chars)
            chars = []
            continue
    count = count + len(chars)
    return count


def day6part2(path):
    declaration = open_file_to_list(path)
    count = 0
    chars = []
    form_count = 0
    for form in declaration:

        if re.findall('\w+\\n', form):
            for char in form:
                chars.append(char)
            form_count = form_count + 1
        else:
            for i in chars:
                if i == '\n':
                    break
                if chars.count(i) == form_count:
                    count = count + 1
            form_count = 0
            chars = []
            continue

    for i in chars:
        if i == '\n':
            break
        if chars.count(i) == form_count:
            count = count + 1
    return count
