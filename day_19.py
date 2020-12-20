import aoc_helper
import regex as re

raw = aoc_helper.fetch(19, year=2020)
# print(raw)
# raw = """42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1

# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


def resolve(item, tree, idx, p2):
    out = ""
    for possibility in item:
        for part in possibility:
            if part.isnumeric():
                if p2 and idx == "8":
                    out += resolve(tree[part], tree, part, p2)
                    out += "+"
                else:
                    out += resolve(tree[part], tree, part, p2)
            else:
                out += part[1]
        out += "|"
    return "(" + out.strip("|") + ")"


def parse_raw():
    rules, messages = raw.split("\n\n")
    split_rules = [i.split(": ") for i in rules.splitlines()]
    parsed_rules = {k: [i.split() for i in v.split(" | ")] for k, v in split_rules}
    r_1 = (re.compile(resolve(parsed_rules["0"], parsed_rules, "0", False)),)
    for i in range(11_00, 12_00):  # hack
        parsed_rules[str(i)] = [["42", "31"], ["42", str(i + 1), "31"]]
    parsed_rules["1200"] = [["42", "31"]]
    parsed_rules["11"] = [["42", "31"], ["42", "1100", "31"]]
    return (
        r_1,
        re.compile(resolve(parsed_rules["0"], parsed_rules, "0", True)),
        messages.splitlines(),
    )


rule, rule_2, messages = parse_raw()


def part_one():
    return len([msg for msg in messages if rule.fullmatch(msg)])


def part_two():
    return len([msg for msg in messages if rule_2.fullmatch(msg)])


aoc_helper.lazy_submit(day=19, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=19, year=2020, solution=part_two)
