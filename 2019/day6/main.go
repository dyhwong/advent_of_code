package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	orbits := parse_data_from_file("data.txt")

	part1(orbits)
	part2(orbits)
}

func part1(orbits map[string]string) {
	answer := get_total_orbits(orbits)
	fmt.Printf("Part 1: %v\n", answer)
}

func part2(orbits map[string]string) {
	answer := get_orbital_transfers(orbits, "YOU", "SAN")
	fmt.Printf("Part 2: %v\n", answer)
}

func parse_data_from_file(filename string) map[string]string {
	raw_data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	data := strings.Split(string(bytes.TrimSpace(raw_data)), "\n")

	orbits := make(map[string]string)
	for _, line := range data {
		objects := strings.Split(line, ")")
		orbits[objects[1]] = objects[0]
	}

	return orbits
}

func get_total_orbits(orbits_map map[string]string) int {
	object_to_orbiters := make(map[string][]string)
	for orbiter, object := range orbits_map {
		object_to_orbiters[object] = append(object_to_orbiters[object], orbiter)
	}

	objects := []string{"COM"}
	object_to_num_orbits := make(map[string]int)
	for len(objects) > 0 {
		object := objects[0]
		objects = append(objects[1:], object_to_orbiters[object]...)

		if _, ok := orbits_map[object]; ok {
			object_to_num_orbits[object] = object_to_num_orbits[orbits_map[object]] + 1
		}
	}

	total_orbits := 0
	for _, num_orbits := range object_to_num_orbits {
		total_orbits += num_orbits
	}

	return total_orbits
}

func get_orbital_transfers(orbits_map map[string]string, start string, end string) int {
	ancestors := make(map[string]int)
	current := orbits_map[start]
	for current != "COM" {
		ancestors[orbits_map[current]] = ancestors[current] + 1
		current = orbits_map[current]
	}

	current = orbits_map[end]
	transfer_count := 0
	for current != "COM" {
		if _, ok := ancestors[current]; ok {
			return ancestors[current] + transfer_count
		}

		current = orbits_map[current]
		transfer_count += 1
	}

	panic("Start and end do not share any ancestors")
}
