class Node:
    grid = {}
    start = None
    shapes = {
        '-': ('W', 'E'),
        '|': ('N', 'S'),
        'L': ('N', 'E'),
        'J': ('N', 'W'),
        '7': ('W', 'S'),
        'F': ('E', 'S')
    }

    def __init__(self, shape, x, y):
        self.x = x
        self.y = y
        if shape == 'S':
            Node.start = self
        else:
            Node.grid[(x, y)] = Node.shapes[shape]

    @classmethod
    def complete_start(cls):
        connections = []
        x, y = cls.start.x, cls.start.y
        if 'S' in cls.grid.get((x, y - 1), []):
            connections.append('N')
        if 'E' in cls.grid.get((x - 1, y), []):
            connections.append('W')
        if 'W' in cls.grid.get((x + 1, y), []):
            connections.append('E')
        if 'N' in cls.grid.get((x, y + 1), []):
            connections.append('S')
        cls.grid[(x, y)] = (connections[0], connections[1])

    @classmethod
    def find_loop_length(cls):
        cls.complete_start()
        direct_dict = {
            'N': (0 , -1),
            'S': (0, 1),
            'W': (-1, 0),
            'E': (1, 0)
        }
        opposite_dict = {
            'N': 'S',
            'S': 'N',
            'W': 'E',
            'E': 'W'
        }
        count = 1
        direction_to_move = cls.grid[(cls.start.x, cls.start.y)][0]
        current = (cls.start.x + direct_dict[direction_to_move][0], cls.start.y + direct_dict[direction_to_move][1])
        while current != (cls.start.x, cls.start.y):
            count += 1
            for path in cls.grid[current]:
                if opposite_dict[direction_to_move] != path:
                    direction_to_move = path
                    current = (current[0] + direct_dict[direction_to_move][0], current[1] + direct_dict[direction_to_move][1])
                    break
        return count

with open('input.txt', 'r') as file:
    for y, line in enumerate(file.read().splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                Node(char, x, y)

print(Node.find_loop_length() // 2)