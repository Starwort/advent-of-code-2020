import aoc_helper

raw = aoc_helper.fetch(1)
# print(raw)


def parse_raw():
    return list(map(int, raw.splitlines()))


data = parse_raw()


def part_one():
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j


def part_two():
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k


aoc_helper.lazy_submit(day=1, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=1, year=2020, solution=part_two)
