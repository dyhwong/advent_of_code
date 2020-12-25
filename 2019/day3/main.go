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
	wire1, wire2 := parse_data_from_file("data.txt")

	part1(wire1, wire2)
	part2(wire1, wire2)
}

func part1(wire1 []Vector, wire2 []Vector) {
	answer := get_min_distance(wire1, wire2)
	fmt.Printf("Part 1: %v\n", answer)
}

func part2(wire1 []Vector, wire2 []Vector) {
	answer := get_min_wire_distance(wire1, wire2)
	fmt.Printf("Part 2: %v\n", answer)
}

func parse_data_from_file(filename string) ([]Vector, []Vector) {
	raw_data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}

	data := string(bytes.TrimSpace(raw_data))
	paths := strings.Split(data, "\n")
	wire1 := parse_path(strings.Split(paths[0], ","))
	wire2 := parse_path(strings.Split(paths[1], ","))

	return wire1, wire2
}

func parse_path(path []string) []Vector {
	directions := make([]Vector, len(path))
	for i, segment := range path {
		magnitude, err := strconv.Atoi(segment[1:])
		if err != nil {
			log.Fatal(err)
		}

		directions[i] = Vector{
			direction: string(segment[0]),
			magnitude: magnitude,
		}
	}

	return directions
}

type Vector struct {
	direction string
	magnitude int
}

type Point struct {
	x int
	y int
}

type WirePoint struct {
	x         int
	y         int
	distance1 int
	distance2 int
}

func get_intersections(wire1 []Vector, wire2 []Vector) []WirePoint {
	distance := 0
	current := Point{0, 0}
	wire1_distances := map[Point]int{}
	for _, segment := range wire1 {
		direction := get_direction_coordinates(segment.direction)
		for i := 0; i < segment.magnitude; i++ {
			distance += 1
			current = Point{current.x + direction[0], current.y + direction[1]}
			wire1_distances[current] = distance
		}
	}

	distance = 0
	current = Point{0, 0}
	wire2_distances := map[Point]int{}
	var intersections []Point
	for _, segment := range wire2 {
		direction := get_direction_coordinates(segment.direction)
		for i := 0; i < segment.magnitude; i++ {
			distance += 1
			current = Point{current.x + direction[0], current.y + direction[1]}
			wire2_distances[current] = distance
			if _, ok := wire1_distances[current]; ok {
				intersections = append(intersections, current)
			}
		}
	}

	wire_intersections := make([]WirePoint, len(intersections))
	for i, intersection := range intersections {
		wire_intersections[i] = WirePoint{intersection.x, intersection.y, wire1_distances[intersection], wire2_distances[intersection]}
	}

	return wire_intersections
}

func get_direction_coordinates(direction string) [2]int {
	var coordinates [2]int

	switch direction {
	case "L":
		coordinates = [2]int{-1, 0}
	case "R":
		coordinates = [2]int{1, 0}
	case "U":
		coordinates = [2]int{0, 1}
	case "D":
		coordinates = [2]int{0, -1}
	default:
		panic(fmt.Sprintf("Found unknown direction %v\n", direction))
	}

	return coordinates
}

func abs(n int) int {
	if n < 0 {
		return -n
	}

	return n
}

func get_min_distance(wire1 []Vector, wire2 []Vector) int {
	intersections := get_intersections(wire1, wire2)

	distances := make([]int, len(intersections))
	for i, intersection := range intersections {
		distances[i] = abs(intersection.x) + abs(intersection.y)
	}

	min_distance := distances[0]
	for _, distance := range distances {
		if distance < min_distance {
			min_distance = distance
		}
	}

	return min_distance
}

func get_min_wire_distance(wire1 []Vector, wire2 []Vector) int {
	intersections := get_intersections(wire1, wire2)

	distances := make([]int, len(intersections))
	for i, intersection := range intersections {
		distances[i] = intersection.distance1 + intersection.distance2
	}

	min_distance := distances[0]
	for _, distance := range distances {
		if distance < min_distance {
			min_distance = distance
		}
	}

	return min_distance
}
