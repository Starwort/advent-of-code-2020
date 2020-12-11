import re

import aoc_helper

HEIGHT = re.compile(r"(\d+)(cm|in)")
COLOUR = re.compile(r"#[0-9a-f]{6}")
PID = re.compile(r"\d{9}")

raw = aoc_helper.fetch(4, year=2020)
# print(raw)
FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def parse_raw():
    passports = raw.split("\n\n")
    fields = [passport.split() for passport in passports]
    return [
        {field.split(":")[0]: field.split(":")[1] for field in fields_}
        for fields_ in fields
    ]


data = parse_raw()


def part_one():
    valid = 0
    for passport in data:
        if set(passport.keys()) & FIELDS == FIELDS:
            valid += 1
    return valid


def part_two():
    valid = 0
    for passport in data:
        if set(passport.keys()) & FIELDS == FIELDS:
            if not (1920 <= int(passport["byr"]) <= 2002):
                continue
            if not (2010 <= int(passport["iyr"]) <= 2020):
                continue
            if not (2020 <= int(passport["eyr"]) <= 2030):
                continue
            if not (
                (match := HEIGHT.fullmatch(passport["hgt"]))
                and (
                    (150 <= int(match[1]) <= 193)
                    if match[2] == "cm"
                    else (59 <= int(match[1]) <= 76)
                )
            ):
                continue
            if not COLOUR.fullmatch(passport["hcl"]):
                continue
            if not passport["ecl"] in "amb blu brn gry grn hzl oth".split():
                continue
            if not PID.fullmatch(passport["pid"]):
                continue
            valid += 1
    return valid


aoc_helper.lazy_submit(day=4, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=4, year=2020, solution=part_two)
