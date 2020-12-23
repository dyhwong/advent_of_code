def main():
    with open("data/day24.txt") as f:
        lines = [parse_line(line.strip()) for line in f.readlines()]

    part1(lines)
    part2(lines)


def part1(lines):
    black_tiles = get_black_tiles(lines)
    answer = len(black_tiles)
    print("Day 24 Part 1: %s" % answer)


def part2(lines):
    black_tiles = get_black_tiles(lines)
    game = GameOfLife(black_tiles)

    for _ in range(100):
        game.next()

    answer = game.num_black_tiles
    print("Day 24 Part 2: %s" % answer)


def parse_line(line):
    directions = []
    index = 0
    while index < len(line):
        if line[index] == "n":
            directions.append(line[index:index + 2])
            index += 2
        elif line[index] == "s":
            directions.append(line[index:index + 2])
            index += 2
        elif line[index] == "w":
            directions.append(line[index])
            index += 1
        elif line[index] == "e":
            directions.append(line[index])
            index += 1
        else:
            raise ValueError("Unable to parse line %s" % line[index:])

    return directions


def get_coordinates(directions):
    order = {direction: i for i, direction in enumerate(["e", "ne", "nw", "w", "sw", "se"])}

    coordinates = (0, 0)
    for direction in directions:
        if direction == "e":
            coordinates = (coordinates[0] + 2, coordinates[1])
        elif direction == "w":
            coordinates = (coordinates[0] - 2, coordinates[1])
        elif direction == "ne":
            coordinates = (coordinates[0] + 1, coordinates[1] + 1)
        elif direction == "nw":
            coordinates = (coordinates[0] - 1, coordinates[1] + 1)
        elif direction == "se":
            coordinates = (coordinates[0] + 1, coordinates[1] - 1)
        elif direction == "sw":
            coordinates = (coordinates[0] - 1, coordinates[1] - 1)
        else:
            raise ValueError("Unknown direction %s" % direction)

    return coordinates


def get_black_tiles(lines):
    black_tiles = set()
    for line in lines:
        coordinates = get_coordinates(line)
        if coordinates in black_tiles:
            black_tiles.remove(coordinates)
        else:
            black_tiles.add(coordinates)

    return black_tiles


class GameOfLife:
    def __init__(self, black_tiles):
        self.black_tiles = black_tiles
        self.relative_coordinates = [(-1, 1), (-2, 0), (-1, -1), (1, -1), (2, 0), (1, 1)]

    def next(self):
        radius = max(get_radius(x, y) for x, y in self.black_tiles)

        black_tiles = set()
        if self.is_black_in_next_state((0, 0)):
            black_tiles.add((0, 0))

        for i in range(1, radius + 2):
            current = (i * 2, 0)

            for relative_x, relative_y in self.relative_coordinates:
                for _ in range(i):
                    current = (current[0] + relative_x, current[1] + relative_y)
                    if self.is_black_in_next_state(current):
                        black_tiles.add(current)

            assert current == (i * 2, 0)

        self.black_tiles = black_tiles

    def get_neighbors(self, coordinates):
        x, y = coordinates
        return [(x + dx, y + dy) for dx, dy in self.relative_coordinates]

    def is_black_in_next_state(self, coordinates):
        black_neighbors = sum(1 for neighbor in self.get_neighbors(coordinates) if neighbor in self.black_tiles)
        return (coordinates in self.black_tiles and black_neighbors in {1, 2}) or (coordinates not in self.black_tiles and black_neighbors == 2)

    @property
    def num_black_tiles(self):
        return len(self.black_tiles)


def get_radius(x, y):
    x, y = abs(x), abs(y)
    radius = min(x, y)
    if x > y:
        radius += (x - y) / 2
    else:
        radius += y - x

    return int(radius)


if __name__ == "__main__":
    main()
