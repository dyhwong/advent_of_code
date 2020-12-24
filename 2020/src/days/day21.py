from collections import defaultdict, namedtuple

import re

INGREDIENT_RE = re.compile(r"([\w ]+) \(contains")
ALLERGEN_RE = re.compile(r"contains ([\w ,]+)")
Food = namedtuple("Food", ("ingredients", "allergens"))


def main():
    with open("data/day21.txt") as f:
        lines = f.readlines()
        foods = [parse_food(line) for line in lines]

    part1(foods)
    part2(foods)


def part1(foods):
    allergen_to_ingredient = get_allergen_to_ingredient(foods)

    answer = sum(sum(1 for i in food.ingredients if i not in allergen_to_ingredient.values()) for food in foods)
    print("Day 21 Part 1: %s" % answer)


def part2(foods):
    allergen_to_ingredient = get_allergen_to_ingredient(foods)
    ingredients = sorted(allergen_to_ingredient.items(), key=lambda item: item[0])
    answer = ",".join(i[1] for i in ingredients)
    print("Day 21 Part 2: %s" % answer)


def get_allergen_to_ingredient(foods):
    allergen_to_candidate_ingredient_lists = defaultdict(list)
    for food in foods:
        for allergen in food.allergens:
            allergen_to_candidate_ingredient_lists[allergen].append(set(food.ingredients))

    allergen_to_ingredient = {}
    while len(allergen_to_ingredient) != len(allergen_to_candidate_ingredient_lists):
        for allergen, candidate_ingredient_lists in allergen_to_candidate_ingredient_lists.items():
            if allergen in allergen_to_ingredient:
                continue

            candidate_ingredients = set.intersection(*candidate_ingredient_lists)
            candidates = [i for i in candidate_ingredients if i not in allergen_to_ingredient.values()]
            if len(candidates) == 1:
                allergen_to_ingredient[allergen] = candidates[0]

    return allergen_to_ingredient


def parse_food(line):
    return Food(
        ingredients=INGREDIENT_RE.search(line).group(1).split(" "),
        allergens=ALLERGEN_RE.search(line).group(1).split(", "),
    )


if __name__ == "__main__":
    main()
