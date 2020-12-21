use std::fs;


pub fn solve() {
    println!("Day 3 Part 1: {}", part1());
    println!("Day 3 Part 2: {}", part2());
}

struct Slope {
    x: usize,
    y: usize,
}

fn part1() -> u32 {
    let map = fs::read_to_string("data/day3.txt").expect("File could not be read");
    let grid: Vec<Vec<char>> = map.lines().map(|row| row.chars().collect()).collect();

    let slope = Slope{x: 3, y: 1};
    get_tree_count(&grid, &slope)
}

fn part2() -> u32 {
    let map = fs::read_to_string("data/day3.txt").expect("File could not be read");
    let grid: Vec<Vec<char>> = map.lines().map(|row| row.chars().collect()).collect();

    let slopes: [Slope; 5] = [Slope{x:1, y:1}, Slope{x:3, y:1}, Slope{x:5, y:1}, Slope{x:7, y:1}, Slope{x:1, y:2}];
    let mut product = 1;
    for slope in slopes.iter() {
        product *= get_tree_count(&grid, slope);
    }

    product
}

fn get_tree_count(grid: &[Vec<char>], slope: &Slope) -> u32 {
    let mut index = 0;
    let mut trees = 0;
    for row in grid.iter().step_by(slope.y) {
        if row[index] == '#' {
            trees += 1;
        }

        index = (index + slope.x) % row.len();
    }

    trees
}
