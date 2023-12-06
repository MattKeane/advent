with open('input.txt', 'r') as data:
    instructions = [instruction.split(' ') for instruction in data.read().split('\n')]

registers = [1]

for instruction in instructions:
    registers.append(registers[-1])
    if instruction[0] == 'addx':
        registers.append(registers[-1] + int(instruction[1]))

lines = []
for i in range(0, len(registers) - 40, 40):
    new_line = []
    for j in range(i, i + 40):
        sprite_pos = registers[j]
        pixel_pos = j - i
        if abs(sprite_pos - pixel_pos) < 2:
            new_line.append('#')
        else:
            new_line.append('.')
    lines.append(new_line)

for line in lines:
    print(''.join(line))

print(len(lines[0]))