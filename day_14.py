from collections import defaultdict

import aoc_helper

raw = aoc_helper.fetch(14, year=2020)
# print(raw)


def parse_raw():
    return [line.split(" = ") for line in raw.splitlines()]


data = parse_raw()


def part_one():
    mask = ""
    mem = defaultdict(int)
    for lval, val in data:
        if lval == "mask":
            mask = val
        else:
            addr = int(lval[4:-1])
            str_val = bin(int(val))[2:].zfill(36)
            mem[addr] = int(
                "".join(
                    bit if mask_bit == "X" else mask_bit
                    for bit, mask_bit in zip(str_val, mask)
                ),
                base=2,
            )
    return sum(mem.values())


def decode(addr: str, mask: str, bit: int = 0):
    if bit < 35:
        if mask[bit] == "0":
            for rest in decode(addr, mask, bit + 1):
                yield addr[bit] + rest
        elif mask[bit] == "1":
            for rest in decode(addr, mask, bit + 1):
                yield "1" + rest
        elif mask[bit] == "X":
            for rest in decode(addr, mask, bit + 1):
                yield "0" + rest
                yield "1" + rest
    else:
        if mask[bit] == "0":
            yield addr[bit]
        elif mask[bit] == "1":
            yield "1"
        elif mask[bit] == "X":
            yield "0"
            yield "1"


def part_two():
    mask = ""
    mem = defaultdict(int)
    for lval, val in data:
        if lval == "mask":
            mask = val
        else:
            addr = int(lval[4:-1])
            str_addr = bin(addr)[2:].zfill(36)
            for addr_str in decode(str_addr, mask):
                mem[int(addr_str, base=2)] = int(val)
    return sum(mem.values())


aoc_helper.lazy_submit(day=14, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=14, year=2020, solution=part_two)
