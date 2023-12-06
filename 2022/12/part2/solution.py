from string import ascii_lowercase
import heapq

class Node:
    def __init__(self, elevation):
        self.elevation = elevation
        self.distance = float('inf')
        self.neighbors = []
        self.visited = False

    def traverse(self, distance):
        if self.distance > distance:
            self.distance = distance

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def visit(self):
        self.visited = True
        for neighbor in self.neighbors:
            neighbor.traverse(self.distance + 1)

    def __lt__(self, other):
        return self.distance < other.distance

elevation_codes = {'S': 0, 'E': 25}
for i, letter in enumerate(ascii_lowercase):
    elevation_codes[letter] = i

with open('input.txt', 'r') as data:
    lines = data.read().split('\n')

nodes = []
unvisited = []
a_nodes = []

for line in lines:
    row = []
    nodes.append(row)
    for letter in line:
        new_node = Node(elevation_codes[letter])
        row.append(new_node)
        if letter == 'S':
            start = new_node
        elif letter == 'E':
            new_node.distance = 0
        elif letter == 'a':
            a_nodes.append(new_node)
        heapq.heappush(unvisited, new_node)       

for y, row in enumerate(nodes):
    for x, node in enumerate(row):
        if x > 0 and row[x - 1].elevation <= node.elevation + 1:
            row[x - 1].add_neighbor(node)
        if x < len(row) - 1 and row[x + 1].elevation <= node.elevation + 1:
            row[x + 1].add_neighbor(node)
        if y > 0 and nodes[y - 1][x].elevation <= node.elevation + 1:
            nodes[y - 1][x].add_neighbor(node)
        if y < len(nodes) - 1 and nodes[y + 1][x].elevation <= node.elevation + 1:
            nodes[y + 1][x].add_neighbor(node)

current = heapq.heappop(unvisited)

while current.distance < float('inf') and len(unvisited) > 0:
    current.visit()
    heapq.heapify(unvisited)
    current = heapq.heappop(unvisited)

print(min([node.distance for node in a_nodes]))