package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetFuel(t *testing.T) {
	test_values := []struct {
		input    int
		expected int
	}{
		{12, 2},
		{14, 2},
		{1969, 654},
		{100756, 33583},
	}

	for _, test_value := range test_values {
		assert.Equal(t, test_value.expected, get_fuel(test_value.input))
	}
}

func TestGetTotalFuel(t *testing.T) {
	test_values := []struct {
		input    int
		expected int
	}{
		{12, 2},
		{14, 2},
		{1969, 966},
		{100756, 50346},
	}

	for _, test_value := range test_values {
		assert.Equal(t, test_value.expected, get_total_fuel(test_value.input))
	}
}
