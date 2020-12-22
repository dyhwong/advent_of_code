def main():
    part1()
    part2()


def part1():
    print("Day 15 Part 1: %s" % run_game(2020))


def part2():
    print("Day 15 Part 2: %s" % run_game(30000000))


def run_game(num_turns):
    numbers = [0, 12, 6, 13, 20, 1, 17]
    turns = {number: i + 1 for i, number in enumerate(numbers)}

    prev_number = numbers[-1]
    for turn_index in range(len(numbers) + 1, num_turns + 1):
        number_to_update = prev_number
        if prev_number not in turns:
            prev_number = 0
        else:
            prev_number = turn_index - 1 - turns[prev_number]
        turns[number_to_update] = turn_index - 1

    return prev_number


if __name__ == "__main__":
    main()
