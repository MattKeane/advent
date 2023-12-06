class Knot:
    def __init__(self, next):
        self.x, self.y = 0, 0
        self.next = next

    def move_right(self):
        self.x += 1
        self.next.move_to(self.x, self.y)

    def move_left(self):
        self.x -= 1
        self.next.move_to(self.x, self.y)

    def move_down(self):
        self.y += 1
        self.next.move_to(self.x, self.y)

    def move_up(self):
        self.y -= 1
        self.next.move_to(self.x, self.y)

    def move_to(self, x, y):
        delta_x, delta_y = x - self.x, y - self.y
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            if delta_x and delta_y:
                self.x += int(delta_x / abs(delta_x))
                self.y += int(delta_y / abs(delta_y))
            elif delta_x:
                self.x += int(delta_x / abs(delta_x))
            else:
                self.y += int(delta_y /abs(delta_y))
            self.next.move_to(self.x, self.y)

class Tail:
    def __init__(self):
        self.x, self.y = 0, 0
        self.visited = {(0, 0): True}

    def move_to(self, x, y):
        delta_x, delta_y = x - self.x, y - self.y
        if abs(delta_x) > 1 or abs(delta_y) > 1:
            if delta_x and delta_y:
                self.x += int(delta_x / abs(delta_x))
                self.y += int(delta_y / abs(delta_y))
            elif delta_x:
                self.x += int(delta_x / abs(delta_x))
            else:
                self.y += int(delta_y /abs(delta_y))
            self.visited[(self.x, self.y)] = True

    @property
    def next(self):
        return None

with open('input.txt', 'r') as data:
    instructions = [instruction.split(' ') for instruction in data.read().split('\n')]

tail = Tail()
head = tail
for _ in range(9):
    new_head = Knot(head)
    head = new_head

commands = {
    'R': head.move_right,
    'L': head.move_left,
    'U': head.move_up,
    'D': head.move_down
}

for instruction in instructions:
    for _ in range(int(instruction[1])):
        commands[instruction[0]]()

print(len(tail.visited))