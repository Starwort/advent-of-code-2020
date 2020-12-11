import aoc_helper

raw = aoc_helper.fetch(10, year=2020)
# print(raw)


def parse_raw():
    return sorted(aoc_helper.extract_ints(raw))


data = parse_raw()


def part_one():
    joltage = 0
    d1 = 0
    d3 = 1
    left = set(data)
    while any(left):
        for i in range(joltage, joltage + 4):
            if i in left:
                left.discard(i)
                d = i - joltage
                joltage = i
                if d == 1:
                    d1 += 1
                elif d == 3:
                    d3 += 1
    return d1 * d3


def part_two():
    solutions = [0 for _ in range(max(data) + 4)]
    solutions[1:4] = [1, 1, 1]
    for i in data:
        solutions[i + 1] += solutions[i]
        solutions[i + 2] += solutions[i]
        solutions[i + 3] += solutions[i]
    return solutions[max(data) + 3]


aoc_helper.lazy_submit(day=10, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=10, year=2020, solution=part_two)
