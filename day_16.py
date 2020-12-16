import aoc_helper
from tqdm import tqdm

raw = aoc_helper.fetch(16, year=2020)


def parse(value):
    r1, r2 = value.split(" or ")
    a, b = r1.split("-")
    c, d = r2.split("-")
    return set(range(int(a), int(b) + 1)) | set(range(int(c), int(d) + 1))


def parse_raw():
    fields, ticket, nearby_tickets = (
        raw.replace("your ticket:\n", "").replace("nearby tickets:\n", "").split("\n\n")
    )
    split_fields = [i.split(": ") for i in fields.splitlines()]
    parsed_fields = {k: parse(v) for k, v in split_fields}
    parsed_ticket = list(map(int, ticket.split(",")))
    parsed_nearby = [
        list(map(int, ticket.split(","))) for ticket in nearby_tickets.splitlines()
    ]
    return parsed_fields, parsed_ticket, parsed_nearby


fields, my_ticket, nearby = parse_raw()


def part_one():
    inv = 0
    for ticket in nearby:
        for value in ticket:
            if not any(value in values for values in fields.values()):
                inv += value
    return inv


def part_two():
    valid_tickets = []
    for ticket in nearby:
        valid = True
        for value in ticket:
            if not any(value in values for values in fields.values()):
                valid = False
        if valid:
            valid_tickets.append(ticket)
    valid_positions = {key: set() for key in fields}
    for i, values in tqdm(enumerate(zip(*valid_tickets)), total=len(fields)):
        for key, valid in fields.items():
            if all(value in valid for value in values):
                valid_positions[key].add(i)
    field_positions = {}
    used_positions = set()
    for key, positions in sorted(valid_positions.items(), key=lambda i: len(i[1])):
        (position,) = positions - used_positions
        used_positions.add(position)
        field_positions[position] = key
    prod = 1
    for index, field in field_positions.items():
        if field.startswith("departure"):
            prod *= my_ticket[index]
    return prod


aoc_helper.lazy_submit(day=16, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=16, year=2020, solution=part_two)
