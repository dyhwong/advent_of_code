use std::fs;


pub fn solve() {
    println!("Day 2 Part 1: {}", part1());
    println!("Day 2 Part 2: {}", part2());
}

fn part1() -> u32 {
    let contents = fs::read_to_string("data/day2.txt").expect("File could not be read");
    let lines = contents.lines();

    let mut count = 0;
    for line in lines {
        let parts: Vec<&str> = line.split_whitespace().collect();

        let letter = parts[1].chars().next().unwrap();
        let range: Vec<usize> = parts[0].split('-').map(|s| s.parse::<usize>().unwrap()).collect();

        if check_password_sled(parts[2], letter, range[0], range[1]) {
            count += 1;
        }

    }

    count
}

fn part2() -> u32 {
    let contents = fs::read_to_string("data/day2.txt").expect("File could not be read");
    let lines = contents.lines();

    let mut count = 0;
    for line in lines {
        let parts: Vec<&str> = line.split_whitespace().collect();

        let letter = parts[1].chars().next().unwrap();
        let range: Vec<usize> = parts[0].split('-').map(|s| s.parse::<usize>().unwrap()).collect();

        if check_password_tobaggan(parts[2], letter, range[0] - 1, range[1] - 1) {
            count += 1;
        }

    }

    count
}

fn check_password_sled(password: &str, letter: char, min_count: usize, max_count: usize) -> bool {
    let count = password.chars().filter(|&c| c == letter).count();
    min_count <= count && count <= max_count
}

fn check_password_tobaggan(password: &str, letter: char, index1: usize, index2: usize) -> bool {
    let matches: Vec<bool> = password.chars().map(|c| c == letter).collect();
    matches[index1] ^ matches[index2]
}
