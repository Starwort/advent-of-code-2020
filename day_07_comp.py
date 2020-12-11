import re
from collections import defaultdict

import aoc_helper

raw = aoc_helper.fetch(7, year=2020)
# print(raw)

CONTAINS = re.compile(r"(.*?) bags contain (.*?)\.")
BAG = re.compile(r"(\d+) (.*?) bags?")
NOT_CONTAIN = re.compile(r"(.*?) bags contain no other bags\.")


def parse_raw():
    rules = {}
    inverse_rules = defaultdict(list)
    for bag, contains, *_ in CONTAINS.findall(raw):
        bags = BAG.findall(contains)
        rules[bag] = [(int(bag_[0]), bag_[1]) for bag_ in bags]
        for _, name in bags:
            inverse_rules[name].append(bag)
    for bag in NOT_CONTAIN.findall(raw):
        rules[bag] = []
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


def contained_bags(bag: str) -> int:
    return sum(n * contained_bags(t) for n, t in rules[bag]) + 1


def part_two():
    return contained_bags("shiny gold") - 1


aoc_helper.lazy_submit(day=7, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=7, year=2020, solution=part_two)
