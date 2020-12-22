from collections import defaultdict
from itertools import chain, tee


def main():
    with open("data/day10.txt") as f:
        numbers = [int(line) for line in f.readlines()]

    part1(numbers)
    part2(numbers)


def part1(numbers):
    # Add in the seat joltage and device joltage.
    adapter_joltages = sorted(numbers)
    joltages = chain([0], adapter_joltages, [adapter_joltages[-1] + 3])

    iter1, iter2 = tee(joltages)
    next(iter2)
    differences = [curr - prev for prev, curr in zip(iter1, iter2)]

    answer = differences.count(1) * differences.count(3)

    print("Day 10 Part 1: %d" % answer)


def part2(numbers):
    # Add in the seat joltage and device joltage.
    adapter_joltages = sorted(numbers)
    joltages = chain([0], adapter_joltages, [adapter_joltages[-1] + 3])

    memo = defaultdict(int)
    memo[0] = 1
    next(joltages)

    combinations = 0
    for joltage in joltages:
        combinations = memo[joltage - 1] + memo[joltage - 2] + memo[joltage - 3]
        memo[joltage] = combinations

    print("Day 10 Part 2: %d" % combinations)

if __name__ == "__main__":
    main()
