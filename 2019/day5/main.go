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
	program := make([]int, len(numbers))
	copy(program, numbers)

	outputs := run_program(program, 1)

	answer := outputs[len(outputs)-1]
	fmt.Printf("Part 1: %v\n", answer)
}

func part2(numbers []int) {
	program := make([]int, len(numbers))
	copy(program, numbers)

	outputs := run_program(program, 5)

	answer := outputs[len(outputs)-1]
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

func run_program(program []int, input int) []int {
	index := 0
	var outputs []int
	for program[index] != 99 {
		opcode := get_opcode(program[index])
		modes := get_modes(program[index])

		switch opcode {
		case 1:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])
			program[program[index+3]] = value1 + value2
			index += 4
		case 2:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])
			program[program[index+3]] = value1 * value2
			index += 4
		case 3:
			program[program[index+1]] = input
			index += 2
		case 4:
			output := get_value(program, program[index+1], modes[0])
			outputs = append(outputs, output)
			index += 2
		case 5:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])

			if value1 != 0 {
				index = value2
			} else {
				index += 3
			}
		case 6:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])

			if value1 == 0 {
				index = value2
			} else {
				index += 3
			}
		case 7:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])

			if value1 < value2 {
				program[program[index+3]] = 1
			} else {
				program[program[index+3]] = 0
			}
			index += 4
		case 8:
			value1 := get_value(program, program[index+1], modes[0])
			value2 := get_value(program, program[index+2], modes[1])

			if value1 == value2 {
				program[program[index+3]] = 1
			} else {
				program[program[index+3]] = 0
			}
			index += 4
		default:
			panic(fmt.Sprintf("Found unknown opcode %v\n", program[index]))
		}
	}

	return outputs
}

func get_opcode(instruction int) int {
	return instruction % 100
}

func get_modes(instruction int) []int {
	modes := make([]int, 2)
	modes[0] = instruction / 100 % 2
	modes[1] = instruction / 1000 % 2
	return modes
}

func get_value(program []int, parameter int, mode int) int {
	if mode == 1 {
		return parameter
	}

	return program[parameter]
}
