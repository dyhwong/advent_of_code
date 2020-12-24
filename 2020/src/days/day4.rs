use std::collections::HashMap;
use std::fs;

use regex::Regex;


pub fn solve() {
    println!("Day 4 Part 1: {}", part1());
    println!("Day 4 Part 2: {}", part2());
}

fn part1() -> u32 {
    let contents = fs::read_to_string("data/day4.txt").expect("File could not be read");
    let passports: Vec<String> = contents.split("\n\n").map(|s| s.replace("\n", " ")).collect();

    let mut valid_count = 0;
    for passport in passports {
        let mut field_names = HashMap::new();
        for field in passport.split_whitespace() {
            let field_parts: Vec<&str> = field.split(':').collect();
            let key = field_parts[0];
            let value = field_parts[1];

            if key == "cid" {
                continue;
            }

            field_names.insert(key, value);
        }

        if is_valid_passport(&field_names) {
            valid_count += 1;
        }
    }

    valid_count
}

fn part2() -> u32 {
    let contents = fs::read_to_string("data/day4.txt").expect("File could not be read");
    let passports: Vec<String> = contents.split("\n\n").map(|s| s.replace("\n", " ")).collect();

    let mut valid_count = 0;
    for passport in passports {
        let mut field_names = HashMap::new();
        for field in passport.split_whitespace() {
            let field_parts: Vec<&str> = field.split(':').collect();
            let key = field_parts[0];
            let value = field_parts[1];

            if key == "cid" {
                continue;
            }

            field_names.insert(key, value);
        }

        if is_valid_passport_strict(&field_names) {
            valid_count += 1;
        }
    }

    valid_count
}


fn is_valid_passport(fields: &HashMap<&str, &str>) -> bool {
    let required_fields = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
    for field in required_fields.iter() {
        if !fields.contains_key(field) {
            return false
        }
    }
    true
}

fn is_valid_passport_strict(fields: &HashMap<&str, &str>) -> bool {
    if !is_valid_passport(fields) {
        return false
    }

    let birth_year: usize = fields["byr"].parse().unwrap();
    if birth_year < 1920 || birth_year > 2002 {
        return false
    }

    let issue_year: usize = fields["iyr"].parse().unwrap();
    if issue_year < 2010 || issue_year > 2020 {
        return false
    }

    let expiration_year: usize = fields["eyr"].parse().unwrap();
    if expiration_year < 2020 || expiration_year > 2030 {
        return false
    }

    let height = fields["hgt"];
    if height.ends_with("cm") {
        let value: usize = height[..height.len() - 2].parse().unwrap();
        if value < 150 || value > 193 {
            return false
        }
    } else if height.ends_with("in") {
        let value: usize = height[..height.len() - 2].parse().unwrap();
        if value < 59 || value > 76 {
            return false
        }
    } else {
        return false
    }

    let hair_color = fields["hcl"];
    let hair_color_re = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
    if !hair_color_re.is_match(hair_color) {
        return false
    }

    let eye_color = fields["ecl"];
    let valid_colors = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
    if !valid_colors.iter().any(|&color| color == eye_color) {
        return false
    }

    let passport_id = fields["pid"];
    let passport_id_re = Regex::new(r"^[0-9]{9}$").unwrap();
    if !passport_id_re.is_match(passport_id) {
        return false
    }


    true
}
