use std::collections::HashSet;
use std::fs;


pub fn solve() {
    println!("Day 8 Part 1: {}", part1());
    println!("Day 8 Part 2: {}", part2());
}

fn part1() -> u32 {
    let contents = fs::read_to_string("data/day8.txt").expect("File could not be read");
    let lines: Vec<&str> = contents.lines().collect();

    let mut next_instruction: i32 = 0;
    let mut visited: HashSet<i32> = HashSet::new();

    let mut accumulator: i32 = 0;

    while !visited.contains(&next_instruction) {
        visited.insert(next_instruction);
        let args: Vec<&str> = lines[next_instruction as usize].split_whitespace().collect();
        match args[0] {
            "acc" => {
                accumulator += args[1].parse::<i32>().unwrap();
                next_instruction += 1;
            },
            "jmp" => {
                next_instruction += args[1].parse::<i32>().unwrap();
            },
            "nop" => {
                next_instruction += 1;
            },
            _ => panic!("Found illegal instruction {0}", lines[next_instruction as usize]),
        }
    }

    accumulator as u32
}

fn part2() -> u32 {
    0
}


