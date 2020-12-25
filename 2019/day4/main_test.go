package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestIsValidPassword(t *testing.T) {
	test_values := []struct {
		input int
		expected bool
	} {
		{111111, true},
		{223450, false},
		{123789, false},
	}

	for _, test_value := range test_values {
		assert.Equal(t, test_value.expected, is_valid_password(test_value.input))
	}
}

func TestIsValidPassword2(t *testing.T) {
	test_values := []struct {
		input int
		expected bool
	} {
		{112233, true},
		{123444, false},
		{111122, true},
	}

	for _, test_value := range test_values {
		assert.Equal(t, test_value.expected, is_valid_password2(test_value.input))
	}
}
