package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestRunProgramWithOpCode1(t *testing.T) {
	input := []int{1, 0, 0, 0, 99}
	expected := []int{2, 0, 0, 0, 99}

	assert.Equal(t, expected, run_program(input))
}

func TestRunProgramWithOpCode2(t *testing.T) {
	input := []int{2, 3, 0, 3, 99}
	expected := []int{2, 3, 0, 6, 99}

	assert.Equal(t, expected, run_program(input))
}

func TestRunProgramWithExtraInstructions(t *testing.T) {
	input := []int{2, 4, 4, 5, 99, 0}
	expected := []int{2, 4, 4, 5, 99, 9801}

	assert.Equal(t, expected, run_program(input))
}

func TestRunProgramWithMultipleOpCodes(t *testing.T) {
	input := []int{1, 1, 1, 4, 99, 5, 6, 0, 99}
	expected := []int{30, 1, 1, 4, 2, 5, 6, 0, 99}

	assert.Equal(t, expected, run_program(input))
}
