import aoc_helper

raw = aoc_helper.day(5)
# print(raw)


def decode_seat(seat):
    lower_y, upper_y = 0, 127
    lower_x, upper_x = 0, 7
    for char in seat:
        mid_y = (upper_y + lower_y) // 2
        mid_x = (upper_x + lower_x) // 2
        if char == "F":
            upper_y = mid_y
        elif char == "B":
            lower_y = mid_y
        elif char == "L":
            upper_x = mid_x
        else:
            lower_x = mid_x
    return upper_x, upper_y


def parse_raw():
    return [decode_seat(seat) for seat in raw.splitlines()]


data = parse_raw()


def part_one():
    return max(y * 8 + x for x, y in data)


def part_two():
    sdata = sorted([y * 8 + x for x, y in data])
    last_id = sdata[0]
    for id in sdata[1:]:
        if id == last_id + 2:
            return last_id + 1
        last_id = id


aoc_helper.submit(day=5, solution=part_one)
aoc_helper.submit(day=5, solution=part_two)
