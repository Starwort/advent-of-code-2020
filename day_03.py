import aoc_helper

raw = aoc_helper.fetch(3)
# print(raw)


def parse_raw():
    return [[char == "#" for char in i] for i in raw.splitlines()]


data = parse_raw()


def part_one():
    x, y = (0, 0)
    trees = 0
    while y < len(data):
        if data[y][x % len(data[0])]:
            trees += 1
        x += 3
        y += 1
    return trees


def one_slope(dx, dy):
    x, y = (0, 0)
    trees = 0
    while y < len(data):
        if data[y][x % len(data[0])]:
            trees += 1
        x += dx
        y += dy
    return trees


def part_two():
    return (
        one_slope(1, 1)
        * one_slope(3, 1)
        * one_slope(5, 1)
        * one_slope(7, 1)
        * one_slope(1, 2)
    )


aoc_helper.lazy_submit(day=3, solution=part_one)
aoc_helper.lazy_submit(day=3, solution=part_two)
