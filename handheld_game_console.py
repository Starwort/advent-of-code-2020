class Arg:
    def __init__(self, value: str) -> None:
        self._value = value

    def value(self, computer: "HandheldGameConsole") -> int:
        return int(self._value)


class HandheldGameConsole:
    def __init__(self, instructions: list[tuple[str, list[Arg]]]) -> None:
        self.accumulator = 0
        self.ip = 0
        self.instructions = instructions
        self.last_instruction = ""

    @property
    def halted(self) -> bool:
        return self.ip >= len(self.instructions)

    @classmethod
    def load_from_string(cls, instructions: str):
        return cls(
            [
                (opc, list(map(Arg, opr.split(","))))
                for opc, opr in [
                    line.split(maxsplit=1) for line in instructions.splitlines()
                ]
            ]
        )

    def acc(self, operand: Arg) -> None:
        self.accumulator += operand.value(self)
        self.ip += 1

    def jmp(self, operand: Arg) -> None:
        self.ip += operand.value(self)

    def nop(self, _: Arg) -> None:
        self.ip += 1

    def step(self) -> None:
        opc, opr = self.instructions[self.ip]
        self.last_instruction = opc
        getattr(self, opc)(*opr)

    def run_until(self, opcode: str) -> None:
        self.step()  # ensure that we run at least one instruction
        while self.last_instruction != opcode and not self.halted:
            self.step()

    def run_until_complete(self) -> None:
        while not self.halted:
            self.step()
