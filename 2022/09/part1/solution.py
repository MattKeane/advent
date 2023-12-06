class Knot:
    def __init__(self, head=(0, 0), tail=None):
        self.head_x = head[0]
        self.head_y = head[1]
        if tail:
            self.tail_x = tail[0]
            self.tail_y = tail[1]
        else:
            self.tail_x, self.tail_y = self.head_x, self.head_y
        self.visited_by_tail = {}

    def move_right(self, distance):
        for _ in range(distance):
            self.head_x += 1
            if self.head_x > self.tail_x + 1:
                self.tail_x = self.head_x - 1
                self.tail_y = self.head_y
            self.visited_by_tail[self.tail] = True
        
    def move_left(self, distance):
        for _ in range(distance):
            self.head_x -= 1
            if self.head_x < self.tail_x - 1:
                self.tail_x = self.head_x + 1
                self.tail_y = self.head_y
            self.visited_by_tail[self.tail] = True

    def move_down(self, distance):
        for _ in range(distance):
            self.head_y += 1
            if self.head_y > self.tail_y + 1:
                self.tail_y = self.head_y - 1
                self.tail_x = self.head_x
            self.visited_by_tail[self.tail] = True

    def move_up(self, distance):
        for _ in range(distance):
            self.head_y -= 1
            if self.head_y < self.tail_y - 1:
                self.tail_y = self.head_y + 1
                self.tail_x = self.head_x
            self.visited_by_tail[self.tail] = True

    @property
    def tail(self):
        return self.tail_x, self.tail_y

with open('input.txt', 'r') as data:
    instructions = [instruction.split(' ') for instruction in data.read().split('\n')]
    knot = Knot()
    commands = {
        'R': knot.move_right,
        'L': knot.move_left,
        'U': knot.move_up,
        'D': knot.move_down,       
    }
    for instruction in instructions:
        commands[instruction[0]](int(instruction[1]))
    print(len(knot.visited_by_tail))
