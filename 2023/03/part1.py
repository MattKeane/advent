import re

with open('input.txt', 'r') as data:
    schematic = data.read().split('\n')

class PartNumber:
    def __init__(self, number, row, span):
        self.number = int(number)
        self.row = row
        self.span = span

    def __int__(self):
        return self.number
    
    schematic = schematic

    def is_valid(self):
        symbol_regex = re.compile(r'[^\d\.]')       

        previous_row = self.row - 1
        if previous_row >= 0:
            for i in range(self.span[0] - 1, self.span[1] + 1):
                if i >= 0 and i < len(self.schematic[previous_row]):
                    if symbol_regex.fullmatch(self.schematic[previous_row][i]):
                        return True

        if self.span[0] - 1 >= 0:
            if symbol_regex.fullmatch(self.schematic[self.row][self.span[0] - 1]):
                return True
        if self.span[1] < len(self.schematic[self.row]):
            if symbol_regex.fullmatch(self.schematic[self.row][self.span[1]]):
                return True

        next_row = self.row + 1
        if next_row < len(self.schematic):
            for i in range(self.span[0] - 1, self.span[1] + 1):
                if i >= 0 and i < len(self.schematic[next_row]):
                    if symbol_regex.fullmatch(self.schematic[next_row][i]):
                        return True

        return False


number_regex = re.compile(r'\d+')

part_numbers = []

for i, row in enumerate(schematic):
    for match in number_regex.finditer(row):
        part_numbers.append(PartNumber(match.group(0), i, match.span(0)))

total = 0
for part_number in part_numbers:
    if part_number.is_valid():
        total += int(part_number)

print(total)