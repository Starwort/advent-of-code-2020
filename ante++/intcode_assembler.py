from typing import List


MNEMONICS = {
    "NOP": [0, 0],
    "ADD": [1, 3],
    "MUL": [2, 3],
    "INP": [3, 1],
    "OUT": [4, 1],
    "BNZ": [5, 2],
    "BRZ": [6, 2],
    "TLT": [7, 3],
    "TEQ": [8, 3],
    "HALT": [99, 0],
}

program_tape: List[int] = []
print(
    "Enter instructions, on individual lines, followed by a trailing newline"
    " to end your code. Any line beginning with a # character will be ignored."
)
for instruction in iter(input, ""):
    if instruction.startswith("#"):
        continue
    opcode, *params = instruction.split(" ")
    if opcode != "DAT":
        if opcode not in MNEMONICS:
            print("Invalid opcode:", opcode)
            exit()
        value, param_length = MNEMONICS[opcode]
        if len(params) != param_length:
            print(
                "Too {} parameters for {}; {} expected but {} given".format(
                    "many" if len(params) > param_length else "few",
                    opcode,
                    param_length,
                    len(params),
                )
            )
            exit()
    new_params: List[int] = []
    for param_no, param in enumerate(params):
        if opcode != "DAT":
            if param.startswith("#"):
                value += 10 ** (param_no + 2)
                param = param[1:]
        base = 10
        if param.startswith("$"):
            base = 16
            param = param[1:]
        new_params.append(int(param, base))
    if opcode != "DAT":
        program_tape.append(value)
    program_tape.extend(new_params)
print(",".join(map(str, program_tape)))
