import aoc_helper

raw = aoc_helper.fetch(18, year=2020)
# print(raw)
# raw = """1 + 2 * 3 + 4 * 5 + 6"""


def parse_raw():
    return [i for i in raw.splitlines()]


data = parse_raw()


def evaluate_expression(expression: str):
    total = 0
    token = ""
    operation = ""
    in_brackets = 0
    for char in expression + " ":
        if char == " " and not in_brackets:
            # print(total, operation, token)
            if token.isnumeric():
                if operation == "":
                    total = int(token)
                elif operation == "+":
                    total += int(token)
                elif operation == "*":
                    total *= int(token)
            else:
                operation = token
            token = ""
        elif char == "(":
            in_brackets += 1
            token += "("
        elif char == ")":
            token += ")"
            in_brackets -= 1
            if not in_brackets:
                token = str(evaluate_expression(token[1:-1]))
        else:
            token += char
    return total


def part_one():
    return sum(evaluate_expression(line) for line in data)


import rply

lg = rply.LexerGenerator()
lg.add("NUM", r"\d+")
lg.add("ADD", r"\+")
lg.add("MUL", r"\*")
lg.add("LPAREN", r"\(")
lg.add("RPAREN", r"\)")
lg.ignore("\s+")
lexer = lg.build()
pg = rply.ParserGenerator(
    ["NUM", "ADD", "MUL", "LPAREN", "RPAREN"], [("left", ["MUL"]), ("left", ["ADD"])]
)


@pg.production("expr : NUM")
def _(tokens):
    return int(tokens[0].value)


@pg.production("expr : expr ADD expr")
def _(tokens):
    return tokens[0] + tokens[2]


@pg.production("expr : expr MUL expr")
def _(tokens):
    return tokens[0] * tokens[2]


@pg.production("expr : LPAREN expr RPAREN")
def _(tokens):
    return tokens[1]


parser = pg.build()


def part_two():
    return sum(parser.parse(lexer.lex(line)) for line in data)


# print(part_one())
aoc_helper.lazy_submit(day=18, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=18, year=2020, solution=part_two)
