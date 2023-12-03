import re

with open('input.txt', 'r') as data:
    schematic = data.read().split('\n')

class Item:
    schematic = {}

    def __init__(self, row, span):
        self.row = row
        self.span = span
        for i in range(span[0], span[1]):
            Item.schematic[(i, row)] = self

class PartNumber(Item):
    def __init__(self, number, row, span):
        super().__init__(row, span)
        self.number = int(number)

    def __int__(self):
        return self.number

class Asterisk(Item):   
    def get_gear_ratio(self):
        neighbors = []
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.span[0] - 1, self.span[1] + 1):
                neighbor = Item.schematic.get((j, i))
                if isinstance(neighbor, PartNumber) and neighbor not in neighbors:
                    neighbors.append(neighbor)
        if len(neighbors) == 2:
            return int(neighbors[0]) * int(neighbors[1])
        return 0

number_regex = re.compile(r'\d+')
asterisk_regex = re.compile(r'\*')

asterisks = []

for i, row in enumerate(schematic):
    for match in number_regex.finditer(row):
        PartNumber(match.group(0), i, match.span(0))
    for match in asterisk_regex.finditer(row):
        asterisks.append(Asterisk(i, match.span(0)))

print(sum([asterisk.get_gear_ratio() for asterisk in asterisks]))