from collections import defaultdict

import aoc_helper

raw = aoc_helper.fetch(17, year=2020)
# print(raw)
# raw = """.#.
# ..#
# ###"""


def parse_raw():
    data = [[".#".index(i) for i in row] for row in raw.splitlines()]
    return defaultdict(
        bool,
        [((x, y, 0), cell) for y, row in enumerate(data) for x, cell in enumerate(row)],
    )


data = parse_raw()


def print_cube(state):
    min_x = min(x for x, y, z in state.keys())
    max_x = max(x for x, y, z in state.keys())
    min_y = min(y for x, y, z in state.keys())
    max_y = max(y for x, y, z in state.keys())
    min_z = min(z for x, y, z in state.keys())
    max_z = max(z for x, y, z in state.keys())
    for z in range(min_z, max_z + 1):
        print("z =", z)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                print(".#"[state[x, y, z]], end="")
            print()
        print()


def part_one():
    state = data.copy()
    min_x = min(x for x, y, z in state.keys())
    max_x = max(x for x, y, z in state.keys())
    min_y = min(y for x, y, z in state.keys())
    max_y = max(y for x, y, z in state.keys())
    min_z = min(z for x, y, z in state.keys())
    max_z = max(z for x, y, z in state.keys())
    for i in range(6):
        new_state = state.copy()
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    current = state[x, y, z]
                    neighbours = sum(
                        state[x + dx, y + dy, z + dz]
                        for dz in range(-1, 2)
                        for dy in range(-1, 2)
                        for dx in range(-1, 2)
                        if not (dx == dy == dz == 0)
                    )
                    if current and neighbours in (2, 3) or neighbours == 3:
                        new_state[x, y, z] = True
                        min_x = min(min_x, x)
                        max_x = max(max_x, x)
                        min_y = min(min_y, y)
                        max_y = max(max_y, y)
                        min_z = min(min_z, z)
                        max_z = max(max_z, z)
                    else:
                        new_state[x, y, z] = False
        state = new_state
    return sum(state.values())


def part_two():
    state = defaultdict(bool, {k + (0,): v for k, v in data.items()})
    min_x = min(x for x, y, z, a in state.keys())
    max_x = max(x for x, y, z, a in state.keys())
    min_y = min(y for x, y, z, a in state.keys())
    max_y = max(y for x, y, z, a in state.keys())
    min_z = min(z for x, y, z, a in state.keys())
    max_z = max(z for x, y, z, a in state.keys())
    min_a = min(a for x, y, z, a in state.keys())
    max_a = max(a for x, y, z, a in state.keys())
    for i in range(6):
        new_state = state.copy()
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    for a in range(min_a - 1, max_a + 2):
                        current = state[x, y, z, a]
                        neighbours = sum(
                            state[x + dx, y + dy, z + dz, a + da]
                            for dz in range(-1, 2)
                            for dy in range(-1, 2)
                            for dx in range(-1, 2)
                            for da in range(-1, 2)
                            if not (dx == dy == dz == da == 0)
                        )
                        if current and neighbours in (2, 3) or neighbours == 3:
                            new_state[x, y, z, a] = True
                            min_x = min(min_x, x)
                            max_x = max(max_x, x)
                            min_y = min(min_y, y)
                            max_y = max(max_y, y)
                            min_z = min(min_z, z)
                            max_z = max(max_z, z)
                            min_a = min(min_a, a)
                            max_a = max(max_a, a)
                        else:
                            new_state[x, y, z, a] = False
        state = new_state
    return sum(state.values())


# print(part_one())
aoc_helper.lazy_submit(day=17, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=17, year=2020, solution=part_two)
