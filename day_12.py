import aoc_helper

raw = aoc_helper.fetch(12, year=2020)
# print(raw)


def parse_raw():
    data = []
    for line in raw.splitlines():
        magnitude = int(line[1:])
        data.append((line[0], magnitude))
    return data


data = parse_raw()


def part_one():
    facing = (1, 0)
    x, y = 0, 0
    for instruction, magnitude in data:
        if instruction == "N":
            y += magnitude
        elif instruction == "S":
            y -= magnitude
        elif instruction == "E":
            x += magnitude
        elif instruction == "W":
            x -= magnitude
        elif instruction == "L":
            if magnitude == 90:
                facing = -facing[1], facing[0]
            elif magnitude == 180:
                facing = -facing[0], -facing[1]
            elif magnitude == 270:
                facing = facing[1], -facing[0]
        elif instruction == "R":
            if magnitude == 270:
                facing = -facing[1], facing[0]
            elif magnitude == 180:
                facing = -facing[0], -facing[1]
            elif magnitude == 90:
                facing = facing[1], -facing[0]
        elif instruction == "F":
            x += facing[0] * magnitude
            y += facing[1] * magnitude
    return abs(x) + abs(y)


def part_two():
    x, y = 0, 0
    wx, wy = 10, 1
    for instruction, magnitude in data:
        if instruction == "N":
            wy += magnitude
        elif instruction == "S":
            wy -= magnitude
        elif instruction == "E":
            wx += magnitude
        elif instruction == "W":
            wx -= magnitude
        elif instruction == "L":
            if magnitude == 90:
                wx, wy = -wy, wx
            elif magnitude == 180:
                wx, wy = -wx, -wy
            elif magnitude == 270:
                wx, wy = wy, -wx
        elif instruction == "R":
            if magnitude == 270:
                wx, wy = -wy, wx
            elif magnitude == 180:
                wx, wy = -wx, -wy
            elif magnitude == 90:
                wx, wy = wy, -wx
        elif instruction == "F":
            x += wx * magnitude
            y += wy * magnitude
    return abs(x) + abs(y)


aoc_helper.lazy_submit(day=12, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=12, year=2020, solution=part_two)
