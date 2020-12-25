SUBJECT_NUMBER = 7
MODULO = 20201227


def main():
    with open("data/day25.txt") as f:
        public_key1, public_key2 = [int(line.strip()) for line in f.readlines()]

    part1(public_key1, public_key2)


def part1(public_key1, public_key2):
    loop_size = determine_loop_size(public_key1)

    encryption_key = 1
    for _ in range(loop_size):
        encryption_key *= public_key2
        encryption_key %= MODULO
    print("Day 25 Part 1: %s" % encryption_key)


def determine_loop_size(public_key):
    loops = 0
    current = 1
    while current != public_key:
        loops += 1
        current *= SUBJECT_NUMBER
        current %= MODULO

    return loops


if __name__ == "__main__":
    main()
