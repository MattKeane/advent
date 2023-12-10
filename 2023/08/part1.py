import re

class Node:
    network = {}

    def __init__(self, address, left, right):
        self.address = address
        self.left = left
        self.right = right
        Node.network[address] = self

    def move(self, direction):
        if direction == 'L':
            return Node.network[self.left]
        if direction == 'R':
            return Node.network[self.right]

    @classmethod
    def navigate(cls, directions):
        current = Node.network['AAA']
        steps = 0
        while current.address != 'ZZZ':
            for direction in directions:
                print(steps)
                steps += 1
                current = current.move(direction)
                if current.address == 'ZZZ':
                    return steps

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

directions = lines[0]

r = re.compile(r'\s\=\s\(|\,\s|\)')
for line in lines[2:]:
    Node(*r.split(line)[:-1])

print(Node.navigate(directions))