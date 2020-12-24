from collections import deque

import time


def main():
    cups = [9, 6, 3, 2, 7, 5, 4, 8, 1]
    part1(cups[:])
    part2(cups[:])


def part1(cup_values):
    current_value = cup_values[0]
    cups = LinkedList(cup_values)
    for _ in range(10):
        perform_move(cups, current_value)
        current_value = cups.value_to_node[current_value].next.value

    values = cups.values_starting_at(1)
    answer = "".join(str(n) for n in values[1:])
    print("Day 23 Part 1: %s" % answer)


def part2(cup_values):
    cup_values.extend(range(len(cup_values) + 1, 1000001))
    current_value = cup_values[0]
    cups = LinkedList(cup_values)
    start = time.time()
    for _ in range(10000000):
        perform_move(cups, current_value)
        current_value = cups.value_to_node[current_value].next.value

    values = cups.values_starting_at(1)
    answer = values[1] * values[2]
    print("Day 23 Part 2: %s" % answer)


class LinkedList:
    def __init__(self, values):
        self.value_to_node = {value: Node(value) for value in values}
        for i in range(len(values)):
            current_value = values[i]
            next_value = values[(i + 1) % len(self.value_to_node)]
            current_node = self.value_to_node[current_value]
            next_node = self.value_to_node[next_value]
            current_node.next = next_node

    @property
    def length(self):
        return len(self.value_to_node)

    def get_by_value(self, value):
        return self.value_to_node[value]

    def pop_after_value(self, value, n=3):
        popped_nodes = [self.value_to_node[value].next]
        for _ in range(n - 1):
            popped_nodes.append(popped_nodes[-1].next)

        self.value_to_node[value].next = popped_nodes[-1].next

        return popped_nodes

    def insert_after_value(self, value, nodes):
        current_node = self.value_to_node[value]
        next_node = current_node.next

        nodes[-1].next = next_node
        current_node.next = nodes[0]

    def values_starting_at(self, value):
        node = self.value_to_node[value]
        nodes = [node]
        for _ in range(len(self.value_to_node) - 1):
            nodes.append(nodes[-1].next)

        return [node.value for node in nodes]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def perform_move(cups, current_value):
    max_cup_value = cups.length
    removed_nodes = cups.pop_after_value(current_value)

    destination_value = max_cup_value if current_value == 1 else current_value - 1
    while destination_value in {node.value for node in removed_nodes}:
        destination_value = max_cup_value if destination_value == 1 else destination_value - 1

    cups.insert_after_value(destination_value, removed_nodes)


if __name__ == "__main__":
    main()
