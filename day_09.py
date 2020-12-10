import aoc_helper

raw = aoc_helper.fetch(9)
# print(raw)


def parse_raw():
    return [int(line) for line in raw.splitlines()]


data = parse_raw()


def get_number_pair(search, sum):
    for i in search:
        if sum - i in search:
            return i, sum - i


PREAMBLE = 25


def part_one():
    last_25 = data[:PREAMBLE]
    idx = PREAMBLE
    while get_number_pair(last_25, data[idx]):
        last_25[idx % PREAMBLE] = data[idx]
        idx += 1
    return data[idx]


def part_two():
    target = part_one()
    for start in range(len(data)):
        for end in range(start + 2, len(data) + 1):
            if sum(short := data[start:end]) == target:
                return min(short) + max(short)


aoc_helper.lazy_submit(day=9, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=9, year=2020, solution=part_two)
