import aoc_helper

raw = aoc_helper.fetch(21, year=2020)
# print(raw)


def parse_raw():
    lines = raw.splitlines()
    rv = []
    all_ingredients = set()
    all_allergens = set()
    for line in lines:
        ingredients, allergens = line[:-1].split(" (contains ")
        these_ingredients = set(ingredients.split())
        these_allergens = set(allergens.split(", "))
        all_ingredients |= these_ingredients
        all_allergens |= these_allergens
        rv.append((these_ingredients, these_allergens))
    return rv, all_ingredients, all_allergens


foods, ingredients, allergens = parse_raw()


def part_one():
    allergen_map = {ingredient: allergens.copy() for ingredient in ingredients}
    for food_ingredients, food_allergens in foods:
        for ingredient in ingredients - food_ingredients:
            allergen_map[ingredient] -= food_allergens
    no_allergens = {k for k, v in allergen_map.items() if len(v) == 0}
    return sum(len(fi & no_allergens) for fi, fa in foods)


def get(s):
    return next(iter(s))


def part_two():
    allergen_map = {ingredient: allergens.copy() for ingredient in ingredients}
    for food_ingredients, food_allergens in foods:
        for ingredient in ingredients - food_ingredients:
            allergen_map[ingredient] -= food_allergens
    while any(len(fa) > 1 for fa in allergen_map.values()):
        for ingredient, allergen in allergen_map.items():
            if len(allergen) == 1:
                for other_ingredient in ingredients - {ingredient}:
                    allergen_map[other_ingredient] -= allergen
    cdil = sorted(
        [(fi, get(fa)) for fi, fa in allergen_map.items() if len(fa) == 1],
        key=lambda i: i[1],
    )
    return ",".join(fi for fi, fa in cdil)


aoc_helper.lazy_submit(day=21, year=2020, solution=part_one)
aoc_helper.lazy_submit(day=21, year=2020, solution=part_two)
