def main():
    with open("data/day8.txt") as f:
        contents = f.read().strip()

    instructions = [line.split(" ") for line in contents.split("\n")]
    instructions = [(command, int(value)) for command, value in instructions]

    for i in range(len(instructions)):
        command, value = instructions[i]
        if command == "acc":
            continue

        print("Checking instruction %d..." % i, end="")
        if command == "jmp":
            halt_value = halts(instructions[:i] + [("nop", value)] + instructions[i + 1:])
            if halt_value:
                print("halts with value %d" % halt_value)
                return halt_value

        if command == "nop":
            halt_value = halts(instructions[:i] + [("jmp", value)] + instructions[i + 1:])
            if halt_value:
                print("halts with value %d" % halt_value)
                return halt_value

        print("doesn't halt")


def halts(instructions):
    visited = set()
    next_ptr = 0
    accumulator = 0

    while next_ptr not in visited:
        visited.add(next_ptr)
        if next_ptr == len(instructions):
            return accumulator
        command, value = instructions[next_ptr]

        if command == "acc":
            accumulator += value
            next_ptr += 1
        elif command == "nop":
            next_ptr += 1
        elif command == "jmp":
            next_ptr += value
        else:
            raise ValueError("Found unexpected command: %s", command)

    return False

if __name__ == "__main__":
    main()

