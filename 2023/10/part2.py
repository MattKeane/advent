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
    loop = {}

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
        cls.n_bound = cls.start.y
        cls.s_bound = cls.start.y
        cls.e_bound = cls.start.x
        cls.w_bound = cls.start.x

    @classmethod
    def draw_loop(cls):
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
        cls.loop[(cls.start.x, cls.start.y)] = cls.grid[(cls.start.x, cls.start.y)]
        direction_to_move = cls.grid[(cls.start.x, cls.start.y)][0]
        current = (cls.start.x + direct_dict[direction_to_move][0], cls.start.y + direct_dict[direction_to_move][1])
        while current != (cls.start.x, cls.start.y):
            cls.loop[(current)] = cls.grid[(current)]
            if current[0] < cls.w_bound:
                cls.w_bound = current[0]
            if current[0] > cls.e_bound:
                cls.e_bound = current[0]
            if current[1] < cls.n_bound:
                cls.n_bound = current[1]
            if current[1] > cls.s_bound:
                cls.s_bound = current[1]
            for path in cls.grid[current]:
                if opposite_dict[direction_to_move] != path:
                    direction_to_move = path
                    current = (current[0] + direct_dict[direction_to_move][0], current[1] + direct_dict[direction_to_move][1])
                    break

    @classmethod
    def get_inner_area(cls):
        area = 0
        for x in range(cls.w_bound + 1, cls.e_bound):
            horizontal = {
                'W': False,
                'E': False
            }
            for y in range(cls.n_bound, cls.s_bound):
                shape = cls.loop.get((x, y))
                if not shape:
                    if horizontal['W'] and horizontal['E']:
                        area += 1
                else:
                    if 'E' in shape:
                        horizontal['E'] = not horizontal['E']
                    if 'W' in shape:
                        horizontal['W'] = not horizontal['W']
        return area

with open('input.txt', 'r') as file:
    for y, line in enumerate(file.read().splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                Node(char, x, y)

Node.complete_start()
Node.draw_loop()
print(Node.get_inner_area())