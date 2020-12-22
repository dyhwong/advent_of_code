import re

OP_REGEX = re.compile(r"(\d+) ([\+\*]) (\d+)")
PAREN_REGEX = re.compile(r"\(([\d \+\*]+)\)")
ADD_REGEX = re.compile(r"(\d+) \+ (\d+)")
MUL_REGEX = re.compile(r"(\d+) \* (\d+)")


def main():
    with open("data/day18.txt") as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)


def part1(lines):
    answer = sum(evaluate(line) for line in lines)
    print("Day 18 Part 1: %s" % answer)


def part2(lines):
    answer = sum(evaluate(line, evaluate_advanced) for line in lines)
    print("Day 18 Part 2: %s" % answer)


def evaluate_simple(line):
    while True:
        match = OP_REGEX.search(line)
        if not match:
            return line

        operation = match.group(2)
        if operation == "+":
            result = int(match.group(1)) + int(match.group(3))
        elif operation == "*":
            result = int(match.group(1)) * int(match.group(3))
        else:
            raise ValueError("Unknown operation: %s" % operation)

        line = line[:match.start(0)] + str(result) + line[match.end(0):]


def evaluate_advanced(line):
    while True:
        match = ADD_REGEX.search(line)
        if not match:
            break

        result = int(match.group(1)) + int(match.group(2))
        line = line[:match.start(0)] + str(result) + line[match.end(0):]

    while True:
        match = MUL_REGEX.search(line)
        if not match:
            break

        result = int(match.group(1)) * int(match.group(2))
        line = line[:match.start(0)] + str(result) + line[match.end(0):]

    return line


def evaluate(line, inner_evaluate=evaluate_simple):
    while True:
        match = PAREN_REGEX.search(line)
        if not match:
            break

        inner = inner_evaluate(match.group(1))
        line = line[:match.start(0)] + str(inner) + line[match.end(0):]

    return int(inner_evaluate(line))


if __name__ == "__main__":
    main()
