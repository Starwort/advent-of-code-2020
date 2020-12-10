import functools
import pathlib
import re
from collections import defaultdict

import tqdm

raw = (pathlib.Path(__file__).parent / "07.in").read_text()

CONTAINS = re.compile(r"(.*?) bags contain (.*?)\.")
BAG = re.compile(r"((-|\+)?\d+(\.\d+)?) (.*?) bags?")
NOT_CONTAIN = re.compile(r"(.*?) bags contain no other bags\.")


def parse_raw():
    rules = defaultdict(list)
    inverse_rules = defaultdict(list)
    for line in tqdm.tqdm(raw.splitlines(), leave=False):
        line: str = line.strip(".")
        bag, contains = line.split(" bags contain ")
        if contains == "no other bags":
            rules[bag] = []
        else:
            bags = BAG.findall(contains)
            for num, _, _, name in tqdm.tqdm(bags, leave=False):
                # print(name, end="\r")
                rules[bag].append((int(float(num) * 4), name))
                inverse_rules[name].append(bag)
    # for bag, contains, *_ in tqdm.tqdm(CONTAINS.findall(raw)):
    #     bags = BAG.findall(contains)
    #     for num, name in tqdm.tqdm(bags):
    #         rules[bag].append((num, name))
    #         inverse_rules[name].append(bag)
    # for bag in tqdm.tqdm(NOT_CONTAIN.findall(raw)):
    #     rules[bag]
    return rules, inverse_rules


rules, inverse_rules = parse_raw()


def part_one():
    print()
    bags = set()
    new_bags = set(inverse_rules["shiny gold"])
    i = 2
    while new_bags:
        print("|/-\\"[i % 4], end="\r")
        i += 1
        bags |= new_bags
        new_new_bags = set()
        for bag in new_bags:
            new_new_bags.update(inverse_rules[bag])
        new_new_bags -= bags
        new_bags = new_new_bags
    print()
    return len(bags)


@functools.lru_cache(maxsize=None)
def contained_bags(bag: str) -> int:
    return sum(n * contained_bags(t) for n, t in tqdm.tqdm(rules[bag], leave=False)) + 1


def part_two():
    result = contained_bags("shiny gold") - 4
    return result, result / 4, result // 4


print(part_one())
print(part_two())
