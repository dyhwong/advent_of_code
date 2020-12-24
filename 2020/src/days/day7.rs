use std::collections::{HashMap, HashSet};
use std::fs;

use regex::Regex;


pub fn solve() {
    println!("Day 7 Part 1: {}", part1());
    println!("Day 7 Part 2: {}", part2());
}

const START: &str = "shiny gold";

fn part1() -> u32 {
    let dependencies = parse_dependency_graph();

    let mut queue: Vec<String> = vec![START.to_string()];
    let mut visited = HashSet::new();

    while !queue.is_empty() {
        let node = queue.pop().unwrap();

        if visited.contains(&node) {
            continue;
        }

        visited.insert(node.clone());
        match dependencies.get(&node) {
            Some(neighbors) => queue.extend(neighbors.clone()),
            None => continue,
        };

    }

    visited.remove(START);

    visited.len() as u32
}

fn part2() -> u32 {
    let dependencies = parse_reverse_dependency_graph();

    let mut queue: Vec<(u32, String)> = vec![(1, START.to_string())];
    let mut total_bags = 0;
    while !queue.is_empty() {
        let (count, node) = queue.pop().unwrap();
        total_bags += count;
        match dependencies.get(&node) {
            Some(neighbors) => {
                let neighbors: Vec<(u32, String)> = neighbors.iter().cloned().map(|(c, n)| (c * count, n)).collect();
                queue.extend(neighbors);
            },
            None => continue,
        };
    }

    total_bags -= 1;
    total_bags
}

fn parse_dependency_graph() -> HashMap<String, Vec<String>> {
    let contents = fs::read_to_string("data/day7.txt").expect("File could not be read");

    let mut dependencies: HashMap<String, Vec<String>> = HashMap::new();

    let re = Regex::new(r"(\w+ \w+) bag").unwrap();
    for line in contents.lines() {
        let caps: Vec<String> = re
            .captures_iter(line)
            .map(|cap| cap[1].to_string())
            .collect();

        let (node, others) = caps.split_at(1);
        let node = &node[0];

        for other in others {
            dependencies.entry(other.to_string()).or_insert_with(Vec::new).push(node.to_string());
        }
    }

    dependencies
}

fn parse_reverse_dependency_graph() -> HashMap<String, Vec<(u32, String)>> {
    let contents = fs::read_to_string("data/day7.txt").expect("File could not be read");

    let mut dependencies: HashMap<String, Vec<(u32, String)>> = HashMap::new();

    let outer_re = Regex::new(r"(\w+ \w+) bags contain").unwrap();
    let inner_re = Regex::new(r"(\d+) (\w+ \w+) bag").unwrap();
    for line in contents.lines() {
        if line.contains("no other bags") {
            continue;
        }
        let outer_bag = outer_re.captures(line).unwrap().get(1).unwrap().as_str();
        let inner_bags = inner_re.captures_iter(line);
        for cap in inner_bags {
            dependencies.entry(outer_bag.to_string()).or_insert_with(Vec::new).push((cap[1].parse::<u32>().unwrap(), cap[2].to_string()));
        }
    }

    dependencies
}