def main():
    with open("data/day19.txt") as f:
        section0, section1 = f.read().split("\n\n")
        strings = section1.splitlines()
        rules_raw = section0.splitlines()

        rules = {}
        for rule in rules_raw:
            rule_num, rule_content = rule.split(": ")
            if '"' in rule_content:
                rules[int(rule_num)] = rule_content[1]
            else:
                parts = rule_content.split(" | ")
                rules[int(rule_num)] = [[int(num) for num in part.split(" ")] for part in parts]

    part1(rules, strings)
    part2(rules, strings)


def part1(rules, strings):
    valid_strings = [string for string in strings if match(rules, string, [0])]
    print("Day 19 Part 1: %s" % len(valid_strings))


def part2(rules, strings):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42,  31], [42, 11, 31]]
    valid_strings = [string for string in strings if match(rules, string, [0])]
    print("Day 19 Part 2: %s" % len(valid_strings))


def match(rules, string, stack):
    if len(stack) > len(string):
        return False
    if not stack or not string:
        return not stack and not string

    symbol = stack.pop()
    if isinstance(symbol, str):
        return string[0] == symbol and match(rules, string[1:], stack.copy())

    return any(match(rules, string, stack + list(reversed(rule))) for rule in rules[symbol])


if __name__ == "__main__":
    main()
