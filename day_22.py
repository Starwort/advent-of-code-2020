from collections import deque

import aoc_helper

raw = aoc_helper.fetch(22, year=2020)
# print(raw)
# raw = """Player 1:
# 9
# 2
# 6
# 3
# 1

# Player 2:
# 5
# 8
# 4
# 7
# 10"""
raw = """Player 1:
43
19

Player 2:
2
29
14"""


def parse_raw():
    p1, p2 = raw.split("\n\n")
    return aoc_helper.extract_ints(p1)[1:], aoc_helper.extract_ints(p2)[1:]


p1, p2 = parse_raw()
print(p1, p2)


def part_one():
    a, b = deque(p1), deque(p2)
    while a and b:
        # for i in range(29):
        card_a, card_b = a.popleft(), b.popleft()
        if card_a > card_b:
            a.append(card_a)
            a.append(card_b)
        else:
            b.append(card_b)
            b.append(card_a)
        # print(i, a, b)
    winner = a or b
    return sum(i * n for i, n in enumerate(reversed(winner), start=1))


def recursive_combat(deck_1, deck_2, depth=0):
    a, b = deque(deck_1), deque(deck_2)
    previous_states = []
    rounds = 0
    while a and b:
        # print(depth, rounds, a, b, (a, b) in previous_states)
        rounds += 1
        if (a, b) in previous_states:
            return 1, 0
        previous_states.append((a.copy(), b.copy()))
        card_a, card_b = a.popleft(), b.popleft()
        # print(card_a < len(a), card_b < len(b))
        if card_a <= len(a) and card_b <= len(b):
            value_a, value_b = recursive_combat(
                list(a)[:card_a], list(b)[:card_b], depth + 1
            )
        else:
            value_a = card_a
            value_b = card_b
        if value_a > value_b:
            a.append(card_a)
            a.append(card_b)
        else:
            b.append(card_b)
            b.append(card_a)
    return sum(i * n for i, n in enumerate(reversed(a), start=1)), sum(
        i * n for i, n in enumerate(reversed(b), start=1)
    )


def part_two():
    a, b = recursive_combat(p1, p2)
    return a or b


print(part_two())
aoc_helper.lazy_submit(day=22, year=2020, solution=part_one)
# aoc_helper.lazy_submit(day=22, year=2020, solution=part_two)
