package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func main() {
	numbers := parse_data_from_file("data.txt")

	part1(numbers)
	part2(numbers)
}

func part1(numbers []int) {
	fuel := 0
	for _, mass := range numbers {
		fuel += get_fuel(mass)
	}

	fmt.Printf("Part 1: %v\n", fuel)
}

func part2(numbers []int) {
	fuel := 0
	for _, mass := range numbers {
		fuel += get_total_fuel(mass)
	}

	fmt.Printf("Part 2: %v\n", fuel)
}

func parse_data_from_file(filename string) []int {
	raw_data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	data := string(bytes.TrimSpace(raw_data))
	lines := strings.Split(data, "\n")
	numbers := make([]int, len(lines))
	for i, line := range lines {
		number, _ := strconv.Atoi(line)
		numbers[i] = number
	}

	return numbers
}

func get_fuel(mass int) int {
	return mass/3 - 2
}

func get_total_fuel(mass int) int {
	fuel := get_fuel(mass)
	additional_fuel := get_fuel(fuel)
	for additional_fuel >= 0 {
		fuel += additional_fuel
		additional_fuel = get_fuel(additional_fuel)
	}
	return fuel
}
