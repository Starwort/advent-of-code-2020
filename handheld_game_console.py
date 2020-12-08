class HandheldGameConsole:
    def __init__(self, instructions: list[tuple[str, int]]) -> None:
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
                (opc, int(opr))
                for opc, opr in [line.split() for line in instructions.splitlines()]
            ]
        )

    def acc(self, operand: int) -> None:
        self.accumulator += operand
        self.ip += 1

    def jmp(self, operand: int) -> None:
        self.ip += operand

    def nop(self, _: int) -> None:
        self.ip += 1

    def step(self) -> None:
        opc, opr = self.instructions[self.ip]
        self.last_instruction = opc
        getattr(self, opc)(opr)

    def run_until(self, opcode: str) -> None:
        self.step()  # ensure that we run at least one instruction
        while self.last_instruction != opcode and not self.halted:
            self.step()

    def run_until_complete(self) -> None:
        while not self.halted:
            self.step()
