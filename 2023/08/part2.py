import re

class Node:
    network = {}
    starting_nodes = []

    def __init__(self, address, left, right):
        self.address = address
        self.left = left
        self.right = right
        Node.network[address] = self
        if address[-1] == 'A':
            Node.starting_nodes.append(self)

    def move(self, direction):
        if direction == 'L':
            return Node.network[self.left]
        if direction == 'R':
            return Node.network[self.right]

    @classmethod
    def navigate(cls, directions):
        current_nodes = Node.starting_nodes
        steps = 0
        while True:
            for direction in directions:
                steps += 1
                new_nodes = []
                for node in current_nodes:
                    new_nodes.append(node.move(direction))
                for node in new_nodes:
                    if node.address[-1] != 'Z':
                        break
                else:
                    return steps
                current_nodes = new_nodes

    @classmethod
    def navigate_left(cls):
        current_nodes = cls.starting_nodes
        steps = 0
        while True:
            steps += 1
            new_nodes = []
            for node in current_nodes:
                new_nodes.append(node.move('L'))
            for node in new_nodes:
                if node.address[-1] != 'Z':
                    break
            else:
                return steps
            current_nodes = new_nodes

    @classmethod
    def navigate_right(cls):
        current_nodes = cls.starting_nodes
        steps = 0
        while True:
            steps += 1
            new_nodes = []
            for node in current_nodes:
                new_nodes.append(node.move('R'))
                print(new_nodes)
            for node in new_nodes:
                if node.address[-1] != 'Z':
                    break
            else:
                return steps
            current_nodes = new_nodes

with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

directions = lines[0]

r = re.compile(r'\s\=\s\(|\,\s|\)')
for line in lines[2:]:
    Node(*r.split(line)[:-1])

steps = []

for node in Node.starting_nodes:
    current = node
    step = 0
    while current.address[-1] != 'Z':
        for direction in directions:
            step += 1
            current = current.move(direction)
            if current.address[-1] == 'Z':
                break
    steps.append(step)

prod = 1
for step in steps:
    prod *= step / 283

print(prod)