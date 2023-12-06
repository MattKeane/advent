from string import ascii_lowercase
import heapq

class Node:
    def __init__(self, elevation):
        self.elevation = elevation
        self.distance = float('inf')
        self.neighbors = []
        self.visited = False

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def add_up(self, node):
        self.up = node

    def add_down(self, node):
        self.down = node

    def add_neighbor(self, node):
        self.neighbors.append(node)

    # def traverse(self, distance=0):
    #     if not self.distance or self.distance > distance:
    #         self.distance = distance
    #         if self.up:
    #             self.up.traverse(self.distance + 1)
    #         if self.down:         
    #             self.down.traverse(self.distance + 1)
    #         if self.right:
    #             self.right.traverse(self.distance + 1)
    #         if self.left:
    #             self.left.traverse(self.distance + 1)
    def traverse(self, distance):
        if self.distance > distance:
            self.distance = distance

    def visit(self):
        self.visited = True

    def __lt__(self, other):
        return self.distance < other.distance

elevation_codes = {'S': 0, 'E': 25}
for i, letter in enumerate(ascii_lowercase):
    elevation_codes[letter] = i

with open('input.txt', 'r') as data:
    lines = data.read().split('\n')

start = None
end = None
nodes = []
unvisited = []

for line in lines:
    row = []
    nodes.append(row)
    for letter in line:
        new_node = Node(elevation_codes[letter])
        row.append(new_node)
        if letter == 'S':
            new_node.distance = 0
            start = new_node
        elif letter == 'E':
            end = new_node
        heapq.heappush(unvisited, new_node)


for y, row in enumerate(nodes):
    for x, node in enumerate(row):
        if x > 0 and row[x - 1].elevation <= node.elevation + 1:
            node.add_neighbor(row[x - 1])
        if x < len(row) - 1 and row[x + 1].elevation <= node.elevation + 1:
            node.add_neighbor(row[x + 1])
        if y > 0 and nodes[y - 1][x].elevation <= node.elevation + 1:
            node.add_neighbor(nodes[y - 1][x])
        if y < len(nodes) - 1 and nodes[y + 1][x].elevation <= node.elevation + 1:
            node.add_neighbor(nodes[y + 1][x])

while not end.visited:    
    current = heapq.heappop(unvisited)
    current.visit()
    for node in current.neighbors:
        node.traverse(current.distance + 1)
    heapq.heapify(unvisited)

print(end.distance)