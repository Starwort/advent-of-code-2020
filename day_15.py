from collections import defaultdict

import aoc_helper
from tqdm import tqdm

raw = aoc_helper.fetch(15, year=2020)
# print(raw)
# raw = "0,3,6"


def parse_raw():
    return list(map(int, raw.split(",")))


data = parse_raw()


def find(num, spoken):
    found = 0
    for i, n in enumerate(spoken[:-1], start=1):
        if n == num:
            found = i
    return found


def part_one():
    spoken = defaultdict(int)
    last = 0
    for turn in range(2020):
        if turn < len(data):
            now = data[turn]
        elif last not in spoken:
            now = 0
        else:
            now = turn - 1 - spoken[last]
        spoken[last] = turn - 1
        last = now
    return last


def part_two():
    spoken = defaultdict(int)
    last = 0
    for turn in tqdm(range(30000000)):
        if turn < len(data):
            now = data[turn]
        elif last not in spoken:
            now = 0
        else:
            now = turn - 1 - spoken[last]
        spoken[last] = turn - 1
        last = now
    return last


# print(part_one())
aoc_helper.lazy_submit(day=15, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=15, year=2020, solution=part_two)
