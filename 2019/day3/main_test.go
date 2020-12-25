package main

import (
	"github.com/stretchr/testify/assert"
	"strings"
	"testing"
)

func TestMinDistance1(t *testing.T) {
	wire1 := parse_path(strings.Split("R8,U5,L5,D3", ","))
	wire2 := parse_path(strings.Split("U7,R6,D4,L4", ","))

	assert.Equal(t, 6, get_min_distance(wire1, wire2))
}

func TestMinDistance2(t *testing.T) {
	wire1 := parse_path(strings.Split("R75,D30,R83,U83,L12,D49,R71,U7,L72", ","))
	wire2 := parse_path(strings.Split("U62,R66,U55,R34,D71,R55,D58,R83", ","))

	assert.Equal(t, 159, get_min_distance(wire1, wire2))
}

func TestMinDistance3(t *testing.T) {
	wire1 := parse_path(strings.Split("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", ","))
	wire2 := parse_path(strings.Split("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", ","))

	assert.Equal(t, 135, get_min_distance(wire1, wire2))
}

func TestMinWireDistance1(t *testing.T) {
	wire1 := parse_path(strings.Split("R8,U5,L5,D3", ","))
	wire2 := parse_path(strings.Split("U7,R6,D4,L4", ","))

	assert.Equal(t, 30, get_min_wire_distance(wire1, wire2))
}

func TestMinWireDistance2(t *testing.T) {
	wire1 := parse_path(strings.Split("R75,D30,R83,U83,L12,D49,R71,U7,L72", ","))
	wire2 := parse_path(strings.Split("U62,R66,U55,R34,D71,R55,D58,R83", ","))

	assert.Equal(t, 610, get_min_wire_distance(wire1, wire2))
}

func TestMinWireDistance3(t *testing.T) {
	wire1 := parse_path(strings.Split("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", ","))
	wire2 := parse_path(strings.Split("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7", ","))

	assert.Equal(t, 410, get_min_wire_distance(wire1, wire2))
}
