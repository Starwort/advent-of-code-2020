from itertools import count

import aoc_helper

raw = aoc_helper.fetch(25, year=2020)
# print(raw)


def parse_raw():
    return aoc_helper.extract_ints(raw)


card_pky, door_pky = parse_raw()
# card_pky, door_pky = [5764801, 17807724]


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject
        value %= 20201227
    return value


def part_one():
    value = 1
    for card_ls in count(start=1):
        value *= 7
        value %= 20201227
        if value == card_pky:
            break
    return transform(door_pky, card_ls)


aoc_helper.lazy_submit(day=25, year=2020, solution=part_one)
