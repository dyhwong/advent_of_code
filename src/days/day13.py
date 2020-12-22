from functools import reduce
from itertools import tee


def main():
	with open("data/day13.txt") as f:
		depart_ts = int(f.readline())
		buses = [int(bus_id) if bus_id != "x" else bus_id for bus_id in f.readline().split(",")]

	part1(depart_ts, [bus_id for bus_id in buses if bus_id != "x"])
	part2(buses)


def part1(depart_ts, buses):
	wait_time = 0
	while True:
		eligible_buses = [bus for bus in buses if (depart_ts + wait_time) % bus == 0]
		if eligible_buses:
			break
		wait_time += 1

	answer = wait_time * eligible_buses[0]

	print("Day 13 Part 1: %d" % answer)


def part2(buses):
    remainders = [
        (-i % bus_id, bus_id)
        for i, bus_id in enumerate(buses)
        if bus_id != "x"
    ]

    buses = [bus_id for bus_id in buses if bus_id != "x"]
    product = reduce(lambda x, y: x * y, buses)

    answer = sum(remainder * product // modulo * modinv(product // modulo, modulo) for remainder, modulo in remainders) % product

    print("Day 13 Part 2: %d" % answer)


def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m


def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)

    g, y, x = extended_euclidean(b % a, a)
    return (g, x - (b // a) * y, y)


if __name__ == "__main__":
	main()
