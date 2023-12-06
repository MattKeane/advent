from collections import deque

class Monkey:
    def __init__(self, note, monkey_group):
        self.monkey_group = monkey_group
        notes = note.split('\n')
        self.items = deque(int(item) for item in notes[1].strip('Starting items: ').split(', '))
        operation_instructions = notes[2].lstrip('Operation: new = old ').split(' ')
        if operation_instructions[0] == '+':
            self.operate = lambda item: item + int(operation_instructions[1])
        elif operation_instructions[1] == 'old':
            self.operate = lambda item: item ** 2
        else:
            self.operate = lambda item: item * int(operation_instructions[1])
        self.divisible_test = int(notes[3].strip('Test: divisible by '))
        self.if_true = int(notes[4].strip('  If true: throw to monkey '))
        self.if_false = int(notes[5].strip('  If false: throw to monkey '))
        self.inspected = 0

    def receive(self, item):
        self.items.append(item)

    def take_turn(self):
        while len(self.items) > 0:
            self.items[0] = (self.operate(self.items[0])) // 3
            if self.items[0] % self.divisible_test == 0:
                self.monkey_group[self.if_true].receive(self.items.popleft())
            else:
                self.monkey_group[self.if_false].receive(self.items.popleft())
            self.inspected += 1
            

with open('input.txt', 'r') as data:
    notes = data.read().split('\n\n')

monkeys = []

for note in notes:
    monkeys.append(Monkey(note, monkeys))

for _ in range(20):
    for monkey in monkeys:
        monkey.take_turn()

largest = 0
second_largest = 0

for monkey in monkeys:
    if monkey.inspected > largest:
        second_largest = largest
        largest = monkey.inspected
    elif monkey.inspected > second_largest:
        second_largest = monkey.inspected

print(largest * second_largest)