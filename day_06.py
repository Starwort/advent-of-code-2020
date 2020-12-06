import string

import aoc_helper

raw = aoc_helper.day(6)
# print(raw)


def parse_raw():
    parts = raw.split("\n\n")
    return [set(i) - {"\n"} for i in parts]


def parse_raw_2():
    parts = raw.split("\n\n")
    rv = []
    for part in parts:
        out = set(string.ascii_lowercase)
        for line in part.split("\n"):
            out &= set(line)
        rv.append(out)
    return rv


data = parse_raw()


def part_one():
    return sum(map(len, data))


def part_two():
    return sum(map(len, parse_raw_2()))


aoc_helper.submit(day=6, solution=part_one)
aoc_helper.submit(day=6, solution=part_two)
