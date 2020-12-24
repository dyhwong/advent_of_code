use std::fs;


pub fn solve() {
    println!("Day 5 Part 1: {}", part1());
    println!("Day 5 Part 2: {}", part2());
}

fn part1() -> u32 {
    let contents = fs::read_to_string("data/day5.txt").expect("File could not be read");
    let max_seat_id = contents.lines().map(|s| get_seat_id(s)).max().unwrap();
    max_seat_id
}

fn part2() -> u32 {
    let contents = fs::read_to_string("data/day5.txt").expect("File could not be read");
    let seats: Vec<u32> = contents.lines().map(|s| get_seat_id(s)).collect();
    let max_id = seats.iter().max().unwrap();
    let min_id = seats.iter().min().unwrap();
    let sum: u32 = seats.iter().sum();

    max_id * (max_id + 1) / 2 - min_id * (min_id - 1) / 2 - sum
}

fn get_seat_id(s: &str) -> u32 {
    let mut id = 0;
    for c in s.chars() {
        id <<= 1;
        if c == 'B' || c == 'R' {
            id += 1;
        }
    }

    id
}

