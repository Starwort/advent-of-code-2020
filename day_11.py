from copy import deepcopy

import aoc_helper

raw = aoc_helper.fetch(11, year=2020)
# print(raw)
# raw = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL"""


def parse_raw():
    return [
        ["L", *["L" for _ in raw.splitlines()[0]], "L"],
        *[["L", *[i for i in row], "L"] for row in raw.splitlines()],
        ["L", *["L" for _ in raw.splitlines()[0]], "L"],
    ]


data = parse_raw()


def life(state, visibility_fn, neighbour_constant):
    next_state = deepcopy(state)
    for y, row in enumerate(state[1:-1], start=1):
        for x, cell in enumerate(row[1:-1], start=1):
            visible = [
                visibility_fn(dy, dx, state, y, x)
                for dy in range(-1, 2)
                for dx in range(-1, 2)
                if not (dy == dx == 0)
            ]
            if cell == "L" and sum(cell == "#" for cell in visible) == 0:
                next_state[y][x] = "#"
            elif (
                cell == "#"
                and sum(cell == "#" for cell in visible) >= neighbour_constant
            ):
                next_state[y][x] = "L"
    return next_state


def get_visible(dy, dx, state, y, x):
    x += dx
    y += dy
    return state[y][x]


def get_visible_2(dy, dx, state, y, x):
    x += dx
    y += dy
    while state[y][x] == ".":
        x += dx
        y += dy
    return state[y][x]


def run_with(visibility_fn, neighbour_constant):
    state = data
    while (next_state := life(state, visibility_fn, neighbour_constant)) != state:
        state = next_state
    return "\n".join("".join(row[1:-1]) for row in state[1:-1]).count("#")


def part_one():
    return run_with(get_visible, 4)


def part_two():
    return run_with(get_visible_2, 5)


aoc_helper.lazy_submit(day=11, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=11, year=2020, solution=part_two)
