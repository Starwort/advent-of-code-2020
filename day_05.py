import aoc_helper

raw = aoc_helper.fetch(5, year=2020)
# print(raw)


def parse_raw():
    return [
        int(seat.translate(str.maketrans("FBLR", "0101")), 2)
        for seat in raw.splitlines()
    ]


data = parse_raw()


def part_one():
    return max(y * 8 + x for x, y in data)


def part_two():
    sdata = sorted([y * 8 + x for x, y in data])
    last_id = sdata[0]
    for id in sdata[1:]:
        if id == last_id + 2:
            return last_id + 1
        last_id = id


aoc_helper.lazy_submit(day=5, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=5, year=2020, solution=part_two)
