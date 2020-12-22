def main():
    with open("data/day9.txt") as f:
        numbers = [int(line) for line in f.readlines()]

    part1(numbers)
    part2(numbers)


def part1(numbers):
    print("Day 9 Part 1: %d" % get_invalid_entry(numbers))


def part2(numbers):
    target_total = get_invalid_entry(numbers)
    print("Day 9 Part 2: %d" % get_encryption_weakness(numbers, target_total))


def get_invalid_entry(numbers):
    index = 0
    while check_window(numbers[index:index + 25], numbers[index + 25]):
        index += 1

    return numbers[index + 25]


def check_window(numbers, total):
    seen = set()
    for n in numbers:
        if total - n in seen:
            return True

        seen.add(n)

    return False


def get_encryption_weakness(numbers, target_total):
    start_index = 0
    end_index = 0
    while True:
        total = sum(numbers[start_index:end_index])
        if total == target_total:
            break
        elif total > target_total:
            start_index += 1
        else:
            end_index += 1

    target_range = numbers[start_index:end_index]
    return min(target_range) + max(target_range)


if __name__ == "__main__":
    main()
