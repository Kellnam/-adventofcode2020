from Day1.part1and2 import day1part1, day1part2
from Day2.part1and2 import day2part1, day2part2
from Day3.part1and2 import day3part1, day3part2
from Day4.part1and2 import day4part1

if __name__ == "__main__":
    print('Day 1 part1 solution: ', day1part1('Day1/numbers.txt'))
    print('Day 1 part2 solution: ', day1part2('Day1/numbers.txt'))
    print('Day 2 part1 solution: ', day2part1('Day2/password_policy.txt'))
    print('Day 2 part2 solution: ', day2part2('Day2/password_policy.txt'))
    print('Day 3 part1 solution: ', day3part1('Day3/path.txt', 3, 1))
    print('Day 3 part2 solution: ', day3part2('Day3/path.txt'))
    print('Day 4 part1 solution: ', day4part1('Day4/passports.txt'))
