import typing
from collections import defaultdict


class InfiniteTape:
    def __init__(self, items):
        self.data = defaultdict(int)
        for index, i in enumerate(items):
            self.data[index] = i

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.data[i] for i in range(key.start, key.stop)]
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value


class IP:
    def __init__(self):
        self.address = 0

    def set(self, new_address):
        self.address = new_address

    def get(self):
        return self.address


class Address:
    def __init__(self, tape: InfiniteTape, initial_address: int):
        self.tape = tape
        self.location = self.tape[initial_address]

    def resolve_to_address(self):
        self.value = self.tape[self.location]

    def resolve_to_value(self):
        self.value = self.location

    def resolve_to_relative(self, relative_base: int):
        self.location += relative_base
        self.resolve_to_address()

    def write(self, data: int):
        self.tape[self.location] = data


class Computer:
    def __init__(
        self,
        data: str,
        in_function: typing.Callable[[], int] = lambda: int(
            input("Program is requesting input\n>>> ")
        ),
        out_function: typing.Callable[[int], None] = print,
        relative_base: int = 0,
    ):
        self.tape = InfiniteTape(int(i) for i in data.split(","))
        self.ip = IP()

        self.in_function = in_function
        self.out_function = out_function

        self.relative_base = relative_base
        self.instructions = [
            lambda: None,
            self.add,
            self.mul,
            self.take_input,
            self.output,
            self.jnz,
            self.jz,
            self.tlt,
            self.teq,
            self.mod_base,
        ]
        self.arg_no = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
        self.halted = False
        self.last_instruction = -1

    def run_until_instruction(self, opcode: int):
        self.eval_one_instruction()
        while not (self.last_instruction == opcode or self.halted):
            self.eval_one_instruction()

    @property
    def next_instruction(self):
        return self.tape[self.ip.get()] % 100

    def eval_one_instruction(self):
        if self.halted:
            return
        ip = self.ip.get()
        opcode = self.tape[ip]
        param_modes, opcode = divmod(opcode, 100)
        self.last_instruction = opcode
        if opcode == 99:
            self.halted = True
            return
        try:
            parameters = [
                Address(self.tape, ip + i + 1) for i in range(self.arg_no[opcode])
            ]
        except:
            print(ip, param_modes, opcode)
            self.halted = True
            raise StopIteration
        param_modes = str(param_modes).zfill(self.arg_no[opcode])[::-1]
        self.ip.set(ip + self.arg_no[opcode] + 1)
        for param, mode in zip(parameters, param_modes):
            [
                param.resolve_to_address,
                param.resolve_to_value,
                lambda: param.resolve_to_relative(self.relative_base),
            ][int(mode)]()
        self.instructions[opcode](*parameters)

    def run_until_complete(self):
        while not self.halted:
            self.eval_one_instruction()

    def add(self, a, b, c):
        c.write(a.value + b.value)

    def mul(self, a, b, c):
        c.write(a.value * b.value)

    def take_input(self, a):
        a.write(self.in_function())

    def output(self, a):
        self.out_function(a.value)

    def jnz(self, a, b):
        if a.value:
            self.ip.set(b.value)

    def jz(self, a, b):
        if not a.value:
            self.ip.set(b.value)

    def tlt(self, a, b, c):
        c.write(int(a.value < b.value))

    def teq(self, a, b, c):
        c.write(int(a.value == b.value))

    def mod_base(self, a):
        self.relative_base += a.value


if __name__ == "__main__":
    import sys
    from collections import deque

    if len(sys.argv) >= 2:
        prog_file = sys.argv[1]
        with open(prog_file) as file:
            tape = file.read()
        if len(sys.argv) >= 3:
            in_file = sys.argv[2]
            with open(in_file) as file:
                data = deque(map(int, file.read().splitlines()))
            get_input = data.popleft
        else:
            get_input = lambda: int(input("Program is requesting input\n>>> "))
    else:
        tape = input("Enter the program\n>>> ")
        get_input = lambda: int(input("Program is requesting input\n>>> "))
    computer = Computer(tape, in_function=get_input)
    computer.run_until_complete()
