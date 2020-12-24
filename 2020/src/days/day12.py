import math


def main():
    with open("data/day12.txt") as f:
        directions = [(line[0], int(line[1:])) for line in f.readlines()]

    part1(directions)
    part2(directions)


def part1(directions):
    position = (0, 0)
    orientation = 0
    for command, amount in directions:
        if command == "W":
            position = (position[0] - amount, position[1])
        elif command == "E":
            position = (position[0] + amount, position[1])
        elif command == "N":
            position = (position[0], position[1] + amount)
        elif command == "S":
            position = (position[0], position[1] - amount)
        elif command == "R":
            orientation -= amount
        elif command == "L":
            orientation += amount
        elif command == "F":
            orientation_rads = orientation * math.pi / 180
            position = (position[0] + round(amount * math.cos(orientation_rads)), position[1] + round(amount * math.sin(orientation_rads)))
        else:
            raise ValueError("Unknown command %s" % command)

    distance = abs(position[0]) + abs(position[1])

    print("Day 12 Part 1: %s" % distance)


def part2(directions):
    ship_position = (0, 0)
    waypoint_position = (10, 1)
    for command, amount in directions:
        if command == "W":
            waypoint_position = (waypoint_position[0] - amount, waypoint_position[1])
        elif command == "E":
            waypoint_position = (waypoint_position[0] + amount, waypoint_position[1])
        elif command == "N":
            waypoint_position = (waypoint_position[0], waypoint_position[1] + amount)
        elif command == "S":
            waypoint_position = (waypoint_position[0], waypoint_position[1] - amount)
        elif command == "R":
            radians = (360 - amount) * math.pi / 180
            waypoint_position = (round(waypoint_position[0] * math.cos(radians) - waypoint_position[1] * math.sin(radians)), round(waypoint_position[0] * math.sin(radians) + waypoint_position[1] * math.cos(radians)))
        elif command == "L":
            radians = amount * math.pi / 180
            waypoint_position = (round(waypoint_position[0] * math.cos(radians) - waypoint_position[1] * math.sin(radians)), round(waypoint_position[0] * math.sin(radians) + waypoint_position[1] * math.cos(radians)))
        elif command == "F":
            ship_position = (ship_position[0] + amount * waypoint_position[0], ship_position[1] + amount * waypoint_position[1])
        else:
            raise ValueError("Unknown command %s" % command)

    distance = abs(ship_position[0]) + abs(ship_position[1])

    print("Day 12 Part 2: %s" % distance)


if __name__ == "__main__":
    main()
