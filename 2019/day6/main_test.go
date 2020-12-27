package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetTotalOrbits(t *testing.T) {
	orbits := parse_data_from_file("test_data.txt")

	assert.Equal(t, 42, get_total_orbits(orbits))
}

func TestGetOrbitalTransfers(t *testing.T) {
	orbits := parse_data_from_file("test_transfers_data.txt")

	assert.Equal(t, 4, get_orbital_transfers(orbits, "YOU", "SAN"))
}
