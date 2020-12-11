import aoc_helper

raw = aoc_helper.fetch(8, year=2020)
# print(raw)


def parse_raw():
    return [
        (instruction.split(" ")[0], int(instruction.split(" ")[1]))
        for instruction in raw.splitlines()
    ]


data = parse_raw()


def part_one():
    ip = 0
    acc = 0
    executed_lines = set()
    while True:
        if ip in executed_lines:
            return acc
        executed_lines.add(ip)
        opcode, operand = data[ip]
        if opcode == "acc":
            acc += operand
        elif opcode == "jmp":
            ip += operand - 1
        ip += 1


def part_two():
    for i, (opc, opr) in enumerate(data):
        modified_data = data.copy()
        if opc == "nop":
            modified_data[i] = ("jmp", opr)
        elif opc == "jmp":
            modified_data[i] = ("nop", opr)
        else:
            continue
        ip = 0
        acc = 0
        clock = 0
        while ip < len(modified_data) and clock < 1000:
            clock += 1
            opcode, operand = modified_data[ip]
            if opcode == "acc":
                acc += operand
            elif opcode == "jmp":
                ip += operand - 1
            ip += 1
        if ip >= len(modified_data):
            return acc


aoc_helper.lazy_submit(day=8, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=8, year=2020, solution=part_two)
