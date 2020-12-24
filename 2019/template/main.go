package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	parse_data_from_file("data.txt")

	part1()
	part2()
}

func part1() {
	answer := 0
	fmt.Printf("Part 1: %v\n", answer)
}

func part2() {
	answer := 0
	fmt.Printf("Part 2: %v\n", answer)
}

func parse_data_from_file(filename string) {
	raw_data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	data := string(bytes.TrimSpace(raw_data))
}
