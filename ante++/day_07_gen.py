# be sure to count all of the bags, even if the nesting becomes topologically impractical!
# :)

import pathlib
import random

MODIFIERS = set(
    (pathlib.Path(__file__).parent / "modifiers.txt").read_text().splitlines()
)
COLOURS = set((pathlib.Path(__file__).parent / "colours.txt").read_text().splitlines())
ALL_BAGS = [modifier + " " + colour for modifier in MODIFIERS for colour in COLOURS]
for _ in range(7):
    random.shuffle(ALL_BAGS)
TOTAL_BAGS = len(ALL_BAGS)


def format_rule(rule: tuple[str, list[tuple[float, str]]]) -> str:
    name, contains = rule
    if not contains:
        return f"{name} bags contain no other bags."


def random_amount() -> float:
    ipart = random.randrange(-5000, 5000)
    fpart = random.random()
    return ipart + fpart


def generate_input():
    used_bags = set()
    rules = {}
    for bag in ALL_BAGS:
        contains = random.randint(0, len(used_bags))
        rules[bag] = [(random_amount(), i) for i in random.sample(used_bags, contains)]
