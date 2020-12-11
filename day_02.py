import aoc_helper

raw = aoc_helper.fetch(2, year=2020)
# print(raw)


def parse_raw():
    lines = raw.splitlines()
    split_lines = [line.split() for line in lines]
    return [
        (int(line[0].split("-")[0]), int(line[0].split("-")[1]), line[1][0], line[2])
        for line in split_lines
    ]


data = parse_raw()


def part_one():
    valid = 0
    password: str
    for min, max, char, password in data:
        if min <= password.count(char) <= max:
            valid += 1
    return valid


def part_two():
    valid = 0
    for a, b, char, password in data:
        if [password[a - 1], password[b - 1]].count(char) == 1:
            valid += 1
    return valid


aoc_helper.lazy_submit(day=2, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=2, year=2020, solution=part_two)
