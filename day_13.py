from functools import reduce

import aoc_helper

raw = aoc_helper.fetch(13, year=2020)
# print(raw)
# raw = """939
# 7,13,x,x,59,x,31,19"""


def parse_raw():
    timestamp = int(raw.splitlines()[0])
    service = list(int(i) if i != "x" else -1 for i in raw.splitlines()[1].split(","))
    return timestamp, service


timestamp, services = parse_raw()


def part_one():
    time = timestamp
    while True:
        for service in services:
            if service == -1:
                continue
            if time % service == 0:
                return (time - timestamp) * service
        time += 1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part_two():
    # chinese remainder theorem???
    service_map = [(i, ((i - (n % i)) % i)) for n, i in enumerate(services) if i != -1]
    return chinese_remainder([n for n, i in service_map], [i for n, i in service_map])


# print(part_two(0))
aoc_helper.lazy_submit(day=13, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=13, year=2020, solution=part_two)
