from collections import defaultdict, namedtuple

import math
import re


TILE_ID_REGEX = re.compile(r"Tile (\d+):")
Tile = namedtuple("Tile", ("id", "pattern"))
Sides = namedtuple("Sides", ("north", "east", "south", "west"))


def main():
    with open("data/day20.txt") as f:
        raw_tiles = [tile.splitlines() for tile in f.read().split("\n\n")]
        tiles = [
            Tile(
                id=int(TILE_ID_REGEX.search(raw_tile[0]).group(1)),
                pattern=raw_tile[1:],
            )
            for raw_tile in raw_tiles
        ]

    part1(tiles)
    part2(tiles)


def part1(tiles):
    sides_to_tiles = defaultdict(list)
    for tile in tiles:
        for side in tile.sides:
            if side in sides_to_tiles:
                sides_to_tiles[side].append(tile.id)
            else:
                side = side[::-1]
                sides_to_tiles[side].append(tile.id)

    tiles_with_no_side_match = [tiles[0] for tiles in sides_to_tiles.values() if len(tiles) == 1]
    duplicates = []
    seen = set()
    for tile_id in tiles_with_no_side_match:
        if tile_id not in seen:
            seen.add(tile_id)
        else:
            duplicates.append(tile_id)

    assert len(duplicates) == 4
    answer = duplicates[0] * duplicates[1] * duplicates[2] * duplicates[3]

    print("Day 20 Part 1: %s" % answer)


def part2(tiles):
    grid = get_grid(tiles)

    answer = get_roughness(grid)

    total = 0
    for tile in tiles:
        total += sum(sum(1 for char in row if char == "#") for row in tile.image)

    print("Day 20 Part 2: %s" % answer)


class Tile:
    def __init__(self, id, pattern):
        self.id = id
        self.pattern = pattern

    def rotate(self):
        self.pattern = [
            "".join(reversed([row[col] for row in self.pattern]))
            for col in range(len(self.pattern[0]))
        ]

    def flip(self):
        self.pattern = [row[::-1] for row in self.pattern]

    @property
    def north_side(self):
        return self.pattern[0]

    @property
    def east_side(self):
        return "".join([row[-1] for row in self.pattern])

    @property
    def south_side(self):
        return self.pattern[-1]

    @property
    def west_side(self):
        return "".join([row[0] for row in self.pattern])

    @property
    def sides(self):
        return [self.north_side, self.east_side, self.south_side, self.west_side]

    @property
    def image(self):
        return [row[1:-1] for row in self.pattern[1:-1]]

    def __str__(self):
        return "\n".join(self.pattern)


def get_grid(tiles):
    id_to_tile = {tile.id: tile for tile in tiles}

    sides_to_tiles = defaultdict(list)
    for tile in tiles:
        for side in tile.sides:
            if side in sides_to_tiles:
                sides_to_tiles[side].append(tile.id)
            else:
                side = side[::-1]
                sides_to_tiles[side].append(tile.id)

    tiles_with_no_side_match = [tiles[0] for tiles in sides_to_tiles.values() if len(tiles) == 1]
    seen = set()
    for tile_id in tiles_with_no_side_match:
        if tile_id not in seen:
            seen.add(tile_id)
        else:
            corner = id_to_tile[tile_id]
            break

    used_tiles = {corner.id}
    grid = [[orient_top_left(sides_to_tiles, corner)]]

    # Fill the first column.
    for _ in range(1, int(math.sqrt(len(tiles)))):
        edge = grid[-1][0].south_side
        candidate_tile_ids = sides_to_tiles[edge] or sides_to_tiles[edge[::-1]]
        next_tile_id = [tile_id for tile_id in candidate_tile_ids if tile_id not in used_tiles][0]
        used_tiles.add(next_tile_id)

        grid.append([orient_tile_below(edge, id_to_tile[next_tile_id])])

    # Fill the rest of the rows.
    for row in range(int(math.sqrt(len(tiles)))):
        for _ in range(1, int(math.sqrt(len(tiles)))):
            edge = grid[row][-1].east_side
            candidate_tile_ids = sides_to_tiles[edge] or sides_to_tiles[edge[::-1]]
            next_tile_id = [tile_id for tile_id in candidate_tile_ids if tile_id not in used_tiles][0]
            used_tiles.add(next_tile_id)

            grid[row].append(orient_tile_right(edge, id_to_tile[next_tile_id]))

    image_grid = []
    for row in grid:
        for i in range(len(row[0].image)):
            image_grid.append("".join([tile.image[i] for tile in row]))

    return image_grid


def orient_top_left(sides_to_tiles, tile):
    for _ in range(2):
        for _ in range(4):
            if (len(sides_to_tiles[tile.north_side]) == 1 or len(sides_to_tiles[tile.north_side[::-1]]) == 1) and (len(sides_to_tiles[tile.west_side]) == 1 or len(sides_to_tiles[tile.west_side[::-1]]) == 1):
                return tile

            tile.rotate()
        tile.flip()

    raise ValueError("Tile %d is not the top left corner" % tile.id)


def orient_tile_below(edge, tile):
    for _ in range(2):
        for _ in range(4):
            if tile.north_side == edge:
                return tile

            tile.rotate()
        tile.flip()

    raise ValueError("Tile %d does not match edge %s" % (tile.id, edge))


def orient_tile_right(edge, tile):
    for _ in range(2):
        for _ in range(4):
            if tile.west_side == edge:
                return tile

            tile.rotate()
        tile.flip()

    raise ValueError("Tile %d does not match edge %s" % (tile.id, edge))


def find_sea_monsters(tile):
    grid = tile.pattern
    sea_monster_coordinates = [
        (0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 1), (19, 1), (18, 0)
    ]
    bounding_box = (max(coordinates[0] for coordinates in sea_monster_coordinates), max(coordinates[1] for coordinates in sea_monster_coordinates))

    sea_monsters = 0
    for r in range(len(grid) - bounding_box[1]):
        for c in range(len(grid[0]) - bounding_box[0]):
            if all(grid[r + coord[1]][c + coord[0]] == "#" for coord in sea_monster_coordinates):
                for dc, dr in sea_monster_coordinates:
                    index_to_replace = c + dc
                    grid[r + dr] = grid[r + dr][:index_to_replace] + "O" + grid[r + dr][index_to_replace + 1:]
                sea_monsters += 1

    return sea_monsters


def get_roughness(grid):
    giant_tile = Tile(0, grid)
    for _ in range(2):
        for _ in range(4):
            if find_sea_monsters(giant_tile):
                return sum(sum(1 for char in row if char == "#") for row in giant_tile.pattern)
            giant_tile.rotate()
        giant_tile.flip()

    raise ValueError("Did not find sea monsters in any tile rotation")


if __name__ == "__main__":
    main()
