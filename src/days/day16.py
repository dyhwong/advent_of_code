import itertools
import re


def main():
    field_regex = re.compile(r"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")
    with open("data/day16.txt") as f:
        contents = f.read().strip()
        sections = contents.split("\n\n")

        field_matches = [field_regex.match(line) for line in sections[0].split("\n")]
        fields = [(match.group(1), [(int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))]) for match in field_matches]

        my_ticket = [int(value) for value in sections[1].split("\n")[1].split(",")]
        other_tickets = [[int(value) for value in line.split(",")] for line in sections[2].split("\n")[1:]]

    part1(fields, other_tickets)
    part2(fields, other_tickets, my_ticket)


def part1(fields, tickets):
    invalid_ticket_values = []
    for ticket in tickets:
        for value in ticket:
            valid_ranges = itertools.chain.from_iterable([field[1] for field in fields])
            could_be_valid = any(lower <= value <= upper for lower, upper in valid_ranges)
            if not could_be_valid:
                invalid_ticket_values.append(value)
                break

    print("Day 16 Part 1: %s" % sum(invalid_ticket_values))


def part2(fields, tickets, my_ticket):
    valid_tickets = get_valid_tickets(fields, tickets)

    field_to_possible_positions = {}
    for field in fields:
        possible_positions = {i for i in range(len(valid_tickets[0])) if is_column_valid(field, get_column(valid_tickets, i))}
        field_to_possible_positions[field[0]] = possible_positions

    field_to_position = {}
    for field, possible_positions in sorted(field_to_possible_positions.items(), key=lambda entry: len(entry[1])):
        field_to_position[field] = list(possible_positions - set(field_to_position.values()))[0]

    answer = 1
    for field, position in field_to_position.items():
        if "departure" in field:
            answer *= my_ticket[position]

    print("Day 16 Part 2: %s" % answer)


def get_valid_tickets(fields, tickets):
    return [ticket for ticket in tickets if is_valid_ticket_values(fields, ticket)]


def is_valid_ticket_values(fields, ticket):
    for value in ticket:
        valid_ranges = itertools.chain.from_iterable([field[1] for field in fields])
        could_be_valid = any(lower <= value <= upper for lower, upper in valid_ranges)
        if not could_be_valid:
            return False

    return True


def is_column_valid(field, values):
    return all(is_field_valid(field, value) for value in values)


def is_field_valid(field, value):
    return any(lower <= value <= upper for lower, upper in field[1])


def get_column(tickets, i):
    return [ticket[i] for ticket in tickets]


if __name__ == "__main__":
    main()
