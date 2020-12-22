import re

MASK_REGEX = re.compile(r"mask = ([X01]+)")
MEMORY_REGEX = re.compile(r"mem\[(\d+)\] = (\d+)")

def main():
    with open("data/day14.txt") as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)


def part1(lines):
    memory = {}
    for line in lines:
        if "mask" in line:
            mask = get_mask(line)
        if "mem" in line:
            location, value = get_memset(line)
            memory[location] = apply_mask_to_value(mask, value)

    answer = sum(memory.values())
    print("Day 14 Part 1: %s" % answer)


def part2(lines):
    memory = {}
    for line in lines:
        if "mask" in line:
            mask = get_mask(line)
        if "mem" in line:
            location, value = get_memset(line)
            masked_locations = apply_mask_to_location(mask, location)
            updated_memory = {masked_location: value for masked_location in masked_locations}
            memory.update(updated_memory)

    answer = sum(memory.values())
    print("Day 14 Part 2: %s" % answer)


def get_mask(line):
    match = MASK_REGEX.match(line)
    return match.group(1)


def get_memset(line):
    match = MEMORY_REGEX.match(line)
    return int(match.group(1)), int(match.group(2))


def apply_mask_to_value(mask, value):
    for index in range(len(mask)):
        char = mask[index]
        if char == "0":
            value &= 2 ** len(mask) - 1 - 2 ** (len(mask) - index - 1)
        elif char == "1":
            value |= 2 ** (len(mask) - index - 1)

    return value


def apply_mask_to_location(mask, location):
    locations = [location]
    for index in range(len(mask)):
        char = mask[index]
        if char == "1":
            locations = [location | 2 ** (len(mask) - index - 1) for location in locations]
            pass
        elif char == "X":
            locations0 = [location & 2 ** len(mask) - 1 - 2 ** (len(mask) - index - 1) for location in locations]
            locations1 = [location | 2 ** (len(mask) - index - 1) for location in locations]
            locations = locations0 + locations1

    return locations


if __name__ == "__main__":
    main()
