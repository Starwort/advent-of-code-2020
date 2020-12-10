import pathlib

from tqdm import tqdm

# raw = aoc_helper.fetch(10)
raw = (pathlib.Path(__file__).parent / "10.in").read_text()
# print(raw)


def parse_raw():
    return sorted(map(int, tqdm(raw.splitlines())))


data = parse_raw()


def part_one():
    d1 = 0
    d3 = 1
    last = 0
    for i in tqdm(data):
        d = i - last
        if d == 1:
            d1 += 1
        elif d == 3:
            d3 += 1
        last = i
    return d1 * d3


def part_two():
    solutions = [1 for _ in range(4)]
    last = 0
    for i in tqdm(data):
        for j in range(last, i):
            solutions[j % 4] = 0
        last = i
        solutions[(i + 1) % 4] += solutions[i % 4]
        solutions[(i + 2) % 4] += solutions[i % 4]
        solutions[(i + 3) % 4] += solutions[i % 4]
        solutions[i % 4] = 0
    answer = solutions[(data[-1] + 3) % 4]
    while answer % 10 == 0:
        answer //= 10
    return answer % 10_000_000_000


print(part_one())
print(part_two())
