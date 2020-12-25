package main

import (
	"fmt"
	"strings"
	"strconv"
)

func main() {
	input := strings.Split("172851-675869", "-")
	min, err := strconv.Atoi(input[0])
	if err != nil {
		panic(err)
	}
	max, err := strconv.Atoi(input[1])
	if err != nil {
		panic(err)
	}

	part1(min, max)
	part2(min, max)
}

func part1(min int, max int) {
	valid_passwords := 0
	for i := min; i < max + 1; i++ {
		if is_valid_password(i) {
			valid_passwords += 1
		}
	}

	fmt.Printf("Part 1: %v\n", valid_passwords)
}

func part2(min int, max int) {
	valid_passwords := 0
	for i := min; i < max + 1; i++ {
		if is_valid_password2(i) {
			valid_passwords += 1
		}
	}

	fmt.Printf("Part 2: %v\n", valid_passwords)
}

func is_valid_password(password int) bool {
	password_string := strconv.Itoa(password)
	digits := make([]int, len(password_string))
	for i, char := range password_string {
		digit, err := strconv.Atoi(string(char))
		if err != nil {
			panic(err)
		}
		digits[i] = digit
	}

	for i := 1; i < len(digits); i++ {
		if digits[i] < digits[i - 1] {
			return false
		}
	}

	has_adjacent_matching_digits := false
	for i := 1; i < len(digits); i++ {
		if digits[i] == digits[i - 1] {
			has_adjacent_matching_digits = true
			break
		}
	}

	return has_adjacent_matching_digits
}

func is_valid_password2(password int) bool {
	password_string := strconv.Itoa(password)
	digits := make([]int, len(password_string))
	for i, char := range password_string {
		digit, err := strconv.Atoi(string(char))
		if err != nil {
			panic(err)
		}
		digits[i] = digit
	}

	for i := 1; i < len(digits); i++ {
		if digits[i] < digits[i - 1] {
			return false
		}
	}

	has_two_adjacent_matching_digits := false
	match_group_size := 1
	for i := 1; i < len(digits); i++ {
		if digits[i] == digits[i - 1] {
			match_group_size += 1
		}
		if digits[i] != digits[i - 1] || i == len(digits) - 1 {
			if match_group_size == 2 {
				has_two_adjacent_matching_digits = true
				break
			}
			match_group_size = 1
		}
	}

	return has_two_adjacent_matching_digits
}
