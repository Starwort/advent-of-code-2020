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


def format_bag_list(bags: list[tuple[float, str]]) -> str:
    return ", ".join(f"{num} {kind} bag{'s' if num != 1 else ''}" for num, kind in bags)


def format_rule(rule: tuple[str, list[tuple[float, str]]]) -> str:
    name, contains = rule
    if not contains:
        return f"{name} bags contain no other bags."
    else:
        return f"{name} bags contain {format_bag_list(contains)}."


def random_amount() -> float:
    ipart = random.randrange(-5000, 5000)
    fpart = int(random.random() * 4) / 4
    return (ipart + (fpart or 0)) or 1


def generate_input() -> str:
    used_bags = set()
    rules_dict = {}
    for bag in ALL_BAGS:
        contains = random.randint(0, len(used_bags))
        rules_dict[bag] = [
            (random_amount(), i) for i in random.sample(used_bags, contains)
        ]
        used_bags.add(bag)
    rules = [format_rule(i) for i in rules_dict.items()]
    for _ in range(7):
        random.shuffle(rules)
    return "\n".join(rules)


(pathlib.Path(__file__).parent / "07.in").write_text(generate_input())
