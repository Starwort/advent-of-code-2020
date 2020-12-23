import aoc_helper

raw = aoc_helper.fetch(23, year=2020)
# raw = """389125467"""


def parse_raw():
    return list(map(int, raw.strip()))


data = parse_raw()


def part_one():
    pos = 0
    cups = data.copy()
    for i in range(100):
        current = cups[pos]
        position = (pos + 1) % len(cups)
        picked_up = (
            cups.pop(position),
            cups.pop(position),
            cups.pop(position),
        )
        dest = current - 1
        while dest not in cups:
            dest -= 1
            if dest < 0:
                dest = 9
        insert_at = cups.index(dest) + 1
        cups.insert(insert_at, picked_up[2])
        cups.insert(insert_at, picked_up[1])
        cups.insert(insert_at, picked_up[0])
        pos = (cups.index(current) + 1) % len(cups)
        cups = cups[pos:] + cups[:pos]
        pos = 0
    start_from = cups.index(1)
    cups = cups[start_from + 1 :] + cups[:start_from]
    return "".join(map(str, cups))


class LLNode:
    right: "LLNode"
    __slots__ = ("value", "right")

    def __init__(self, value):
        self.value = value
        self.right = None


def part_two():
    cups = [LLNode(i) for i in data]
    for i in range(max(data), 1_000_000):
        cups.append(LLNode(i + 1))
    for a, b in zip([cups[-1], *cups], cups):
        a.right = b
    node_lookup = {n.value: n for n in cups}  # search optimisation!
    curr_node = cups[0]
    for i in range(10_000_000):
        picked_up = curr_node.right
        last_pick = curr_node.right.right.right
        curr_node.right = last_pick.right
        dest = curr_node.value - 1 or 1_000_000
        while dest in (
            picked_up.value,
            picked_up.right.value,
            picked_up.right.right.value,
        ):
            dest -= 1
            if dest < 1:
                dest = 1_000_000
        place_at = node_lookup[dest]
        last_pick.right = place_at.right
        place_at.right = picked_up
        curr_node = curr_node.right
    node = node_lookup[1]
    return node.right.value * node.right.right.value


# print(part_two())
aoc_helper.lazy_submit(day=23, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=23, year=2020, solution=part_two)
