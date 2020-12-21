use std::collections::HashSet;
use std::fs;
use std::iter::FromIterator;

use itertools::Itertools;


pub fn solve() {
    println!("Day 6 Part 1: {}", part1());
    println!("Day 6 Part 2: {}", part2());
}

fn part1() -> u32 {
    let contents = fs::read_to_string("data/day6.txt").expect("File could not be read");
    let groups = contents.split("\n\n").map(|s| s.replace("\n", ""));
    let unique_counts: u32 = groups.map(get_unique_characters).sum();
    unique_counts
}

fn part2() -> u32 {
    let contents = fs::read_to_string("data/day6.txt").expect("File ocould not be read");
    let groups = contents.split("\n\n");
    let counts: u32 = groups.map(|s| get_intersection(s.to_string())).sum();
    counts
}

fn get_unique_characters(s: String) -> u32 {
    s.chars().unique().count() as u32
}

fn get_intersection(s: String) -> u32 {
    let mut sets: Vec<HashSet<char>> = s.split_whitespace().map(|line| HashSet::from_iter(line.chars())).collect();
    let (intersection, others) = sets.split_at_mut(1);
    let intersection = &mut intersection[0];
    for other in others {
        intersection.retain(|e| other.contains(e));
    }

    intersection.len() as u32
}
