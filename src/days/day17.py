import copy


def main():
    with open("data/day17.txt") as f:
        grid = [[1 if char == "#" else 0 for char in line]for line in f.readlines()]

    energy_source_3d = EnergySource3D(grid)
    energy_source_4d = EnergySource4D(grid)
    part1(energy_source_3d)
    part2(energy_source_4d)


def part1(energy_source):
    energy_source.get_nth_state(6)
    print("Day 17 Part 1: %s" % energy_source.get_total_active_cubes())


def part2(energy_source):
    energy_source.get_nth_state(6)
    print("Day 17 Part 2: %s" % energy_source.get_total_active_cubes())


class EnergySource3D:
    def __init__(self, grid):
        self.dim_x = len(grid[0])
        self.dim_y = len(grid)
        self.dim_z = 1

        self.active_cubes = {
            (c, r, 0)
            for r in range(self.dim_y) for c in range(self.dim_x)
            if grid[r][c]
        }

    def is_active(self, coordinates):
        return coordinates in self.active_cubes

    def get_neighbors(self, coordinates):
        x, y, z = coordinates
        return [
            (x + dx, y + dy, z + dz)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
            if dx != 0 or dy != 0 or dz != 0
        ]

    def get_active_neighbors(self, coordinates):
        return sum([self.is_active(coordinates) for coordinates in self.get_neighbors(coordinates)])

    def get_next_state(self):
        new_active_cubes = set()
        for x in range(self.dim_x + 2):
            for y in range(self.dim_y + 2):
                for z in range(self.dim_z + 2):
                    coordinates = (x - 1, y - 1, z - 1)
                    active_neighbors = self.get_active_neighbors(coordinates)
                    if self.is_active(coordinates) and active_neighbors in {2, 3}:
                        new_active_cubes.add((x, y, z))
                    elif not self.is_active(coordinates) and active_neighbors == 3:
                        new_active_cubes.add((x, y, z))

        self.dim_x += 2
        self.dim_y += 2
        self.dim_z += 2
        self.active_cubes = new_active_cubes

    def get_nth_state(self, n=1):
        for i in range(n):
            self.get_next_state()

    def get_total_active_cubes(self):
        return len(self.active_cubes)


class EnergySource4D:
    def __init__(self, grid):
        self.dim_x = len(grid[0])
        self.dim_y = len(grid)
        self.dim_z = 1
        self.dim_w = 1

        self.active_cubes = {
            (c, r, 0, 0)
            for r in range(self.dim_y) for c in range(self.dim_x)
            if grid[r][c]
        }

    def is_active(self, coordinates):
        return coordinates in self.active_cubes

    def get_neighbors(self, coordinates):
        x, y, z, w = coordinates
        return [
            (x + dx, y + dy, z + dz, w + dw)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            for dz in range(-1, 2)
            for dw in range(-1, 2)
            if dx != 0 or dy != 0 or dz != 0 or dw != 0
        ]

    def get_active_neighbors(self, coordinates):
        return sum([self.is_active(coordinates) for coordinates in self.get_neighbors(coordinates)])

    def get_next_state(self):
        new_active_cubes = set()
        for x in range(self.dim_x + 2):
            for y in range(self.dim_y + 2):
                for z in range(self.dim_z + 2):
                    for w in range(self.dim_w + 2):
                        coordinates = (x - 1, y - 1, z - 1, w - 1)
                        active_neighbors = self.get_active_neighbors(coordinates)
                        if self.is_active(coordinates) and active_neighbors in {2, 3}:
                            new_active_cubes.add((x, y, z, w))
                        elif not self.is_active(coordinates) and active_neighbors == 3:
                            new_active_cubes.add((x, y, z, w))

        self.dim_x += 2
        self.dim_y += 2
        self.dim_z += 2
        self.dim_w += 2
        self.active_cubes = new_active_cubes

    def get_nth_state(self, n=1):
        for i in range(n):
            self.get_next_state()

    def get_total_active_cubes(self):
        return len(self.active_cubes)


if __name__ == "__main__":
    main()
