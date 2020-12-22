from copy import deepcopy


def main():
    with open("data/day11.txt") as f:
        grid = [list(line) for line in f.readlines()]

    part1(grid)
    part2(grid)


def part1(grid):
    while True:
        next_state = get_next_state(grid)
        if all(row1 == row2 for row1, row2 in zip(grid, next_state)):
            break

        grid = next_state

    total_occupied = sum(row.count("#") for row in grid)

    print("Day 11 Part 1: %s" % total_occupied)


def part2(grid):
    while True:
        next_state = get_next_state2(grid)
        if all(row1 == row2 for row1, row2 in zip(grid, next_state)):
            break

        grid = next_state

    total_occupied = sum(row.count("#") for row in grid)

    print("Day 11 Part 2: %s" % total_occupied)


def get_next_state(grid):
    next_state = deepcopy(grid)

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            occupied_seats = get_num_adjacent_occupied_seats(grid, r, c)
            if grid[r][c] == "L" and not occupied_seats:
                next_state[r][c] = "#"
            elif grid[r][c] == "#" and occupied_seats >= 4:
                next_state[r][c] = "L"
            else:
                next_state[r][c] = grid[r][c]

    return next_state


def get_num_adjacent_occupied_seats(grid, row, col):
    occupied_seats = -1 if grid[row][col] == "#" else 0
    for r in range(max(0, row - 1), min(row + 2, len(grid))):
        for c in range(max(0, col - 1), min(col + 2, len(grid[r]))):
            if grid[r][c] == "#":
                occupied_seats += 1

    return occupied_seats


def get_next_state2(grid):
    next_state = deepcopy(grid)

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == ".":
                next_state[r][c] = grid[r][c]
                continue
            occupied_seats = get_num_visible_occupied_seats(grid, r, c)
            if grid[r][c] == "L" and not occupied_seats:
                next_state[r][c] = "#"
            elif grid[r][c] == "#" and occupied_seats >= 5:
                next_state[r][c] = "L"
            else:
                next_state[r][c] = grid[r][c]

    return next_state


def get_num_visible_occupied_seats(grid, row, col):
    directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
    occupied_seats = 0
    for direction_x, direction_y in directions:
        steps = 1
        while True:
            row_to_check, col_to_check = (row + direction_y * steps, col + direction_x * steps)
            if not is_valid(grid, row_to_check, col_to_check):
                break

            if grid[row_to_check][col_to_check] == "L":
                break
            elif grid[row_to_check][col_to_check] == "#":
                occupied_seats += 1
                break

            steps += 1

    return occupied_seats


def is_valid(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


if __name__ == "__main__":
    main()
