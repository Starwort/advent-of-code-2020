import string

import aoc_helper

raw = aoc_helper.fetch(6)
# print(raw)


def parse_raw():
    parts = raw.split("\n\n")
    return [[set(i) for i in part.splitlines()] for part in parts]


data = parse_raw()


def part_one():
    return sum(map(len, map(lambda i: set.union(*i), data)))


def part_two():
    return sum(map(len, map(lambda i: set.intersection(*i), data)))


aoc_helper.lazy_submit(day=6, solution=part_one)
aoc_helper.lazy_submit(day=6, solution=part_two)
