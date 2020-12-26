package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRunProgramWithOpCode1(t *testing.T) {
	program := []int{1, 0, 0, 0, 99}
	expected := []int{2, 0, 0, 0, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithOpCode2(t *testing.T) {
	program := []int{2, 3, 0, 3, 99}
	expected := []int{2, 3, 0, 6, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithOpCode3(t *testing.T) {
	program := []int{3, 0, 99}
	input := 123
	expected := []int{input, 0, 99}

	output := run_program(program, input)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithOpCode4(t *testing.T) {
	program := []int{4, 2, 99}
	expected := []int{4, 2, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, []int{99}, output)
}

func TestRunProgramHalts(t *testing.T) {
	program := []int{2, 4, 4, 5, 99, 0}
	expected := []int{2, 4, 4, 5, 99, 9801}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithModes(t *testing.T) {
	program := []int{1002, 4, 3, 4, 33}
	expected := []int{1002, 4, 3, 4, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithInputsAndOutputs(t *testing.T) {
	program := []int{3, 0, 4, 0, 99}
	input := 123
	expected := []int{input, 0, 4, 0, 99}

	output := run_program(program, input)
	assert.Equal(t, expected, program)
	assert.Equal(t, []int{input}, output)
}

func TestRunProgramWithOutputModes(t *testing.T) {
	program := []int{104, 0, 99}
	expected := []int{104, 0, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, []int{0}, output)
}

func TestRunProgramWithNegativeValues(t *testing.T) {
	program := []int{1101, 100, -1, 4, 0}
	expected := []int{1101, 100, -1, 4, 99}

	output := run_program(program, 0)
	assert.Equal(t, expected, program)
	assert.Equal(t, 0, len(output))
}

func TestRunProgramWithPositionModeJump(t *testing.T) {
	program := []int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}
	output := run_program(program, 0)

	assert.Equal(t, []int{0}, output)

	program = []int{3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9}
	output = run_program(program, 123)

	assert.Equal(t, []int{1}, output)
}

func TestRunProgramWithImmediateModeJump(t *testing.T) {
	program := []int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}
	output := run_program(program, 0)

	assert.Equal(t, []int{0}, output)

	program = []int{3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1}
	output = run_program(program, 123)

	assert.Equal(t, []int{1}, output)
}

func TestRunProgramLarge(t *testing.T) {
	program := []int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
		1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
		999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}
	output := run_program(program, 3)

	assert.Equal(t, []int{999}, output)

	program = []int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
		1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
		999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}

	output = run_program(program, 8)
	assert.Equal(t, []int{1000}, output)

	program = []int{3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
		1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
		999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99}

	output = run_program(program, 25)
	assert.Equal(t, []int{1001}, output)
}
