package main

import (
	"bytes"
	"errors"
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
	program := make([]int, len(numbers))
	copy(program, numbers)

	program = run_program_with_inputs(program, 12, 2)

	answer := program[0]
	fmt.Printf("Part 1: %v\n", answer)
}

func part2(numbers []int) {
	noun, verb, err := find_inputs(numbers)
	if err != nil {
		panic(err.Error())
	}

	answer := 100*noun + verb
	fmt.Printf("Part 2: %v\n", answer)
}

func parse_data_from_file(filename string) []int {
	raw_data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	data := string(bytes.TrimSpace(raw_data))
	entries := strings.Split(data, ",")
	numbers := make([]int, len(entries))
	for i, entry := range entries {
		number, _ := strconv.Atoi(entry)
		numbers[i] = number
	}

	return numbers
}

func run_program(program []int) []int {
	index := 0
	for program[index] != 99 {
		value1 := program[program[index+1]]
		value2 := program[program[index+2]]
		destination := program[index+3]

		switch program[index] {
		case 1:
			program[destination] = value1 + value2
		case 2:
			program[destination] = value1 * value2
		default:
			panic(fmt.Sprintf("Found unknown opcode %v\n", program[index]))
		}

		index += 4
	}

	return program
}

func run_program_with_inputs(program []int, noun int, verb int) []int {
	program[1] = noun
	program[2] = verb

	return run_program(program)
}

func find_inputs(program []int) (int, int, error) {
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			copied_program := make([]int, len(program))
			copy(copied_program, program)

			output := run_program_with_inputs(copied_program, i, j)[0]
			if output == 19690720 {
				return i, j, nil
			}
		}
	}

	return 0, 0, errors.New("Could not find inputs for program")
}
