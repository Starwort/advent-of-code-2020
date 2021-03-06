import functools
import re
from collections import defaultdict

import aoc_helper

raw = aoc_helper.fetch(7, year=2020)
# print(raw)

BAG = re.compile(r"(\d+) (.*?) bags?")


def parse_raw():
    rules = defaultdict(list)
    inverse_rules = defaultdict(list)
    for line in raw.splitlines():
        line: str = line.strip(".")
        bag, contains = line.split(" bags contain ")
        if contains == "no other bags":
            rules[bag] = []
        else:
            bags = BAG.findall(contains)
            for num, _, _, name in bags:
                # print(name, end="\r")
                rules[bag].append((int(float(num) * 4), name))
                inverse_rules[name].append(bag)
    return rules, inverse_rules


rules, inverse_rules = parse_raw()


def part_one():
    bags = set()
    new_bags = set(inverse_rules["shiny gold"])
    while new_bags:
        bags |= new_bags
        new_new_bags = set()
        for bag in new_bags:
            new_new_bags.update(inverse_rules[bag])
        new_new_bags -= bags
        new_bags = new_new_bags
    return len(bags)


@functools.cache
def contained_bags(bag: str) -> int:
    return sum(n * contained_bags(t) for n, t in rules[bag]) + 1


def part_two():
    return contained_bags("shiny gold") - 1


aoc_helper.lazy_submit(day=7, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=7, year=2020, solution=part_two)
