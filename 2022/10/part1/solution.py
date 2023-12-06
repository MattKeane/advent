with open('input.txt', 'r') as data:
    instructions = [instruction.split(' ') for instruction in data.read().split('\n')]

registers = [1]

for instruction in instructions:
    registers.append(registers[-1])
    if instruction[0] == 'addx':
        registers.append(registers[-1] + int(instruction[1]))

total = 0

for i in range(19, 220, 40):
    total += registers[i] * (i + 1)

print(total)