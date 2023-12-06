import re

def create_stacks(crate_input):
    stacks = {}
    rows = crate_input.split('\n')[-2::-1]
    row_length = int((len(rows[0]) + 1) / 4)
    for i in range(row_length):
        stacks[i] = []
    for row in rows:
        for i in range(0, len(row), 4):
            if row[i] != ' ':
                stack_number = int(i / 4)
                stacks[stack_number].append(row[i + 1])
    return stacks

def parse_instructions(instructions_input):
    instructions = []
    for row in instructions_input.split('\n'):
        instructions.append(([int(i) for i in re.split(r'\D+', row)[1:]]))
    return instructions

def execute_instructions(stacks, instructions):
    for instruction in instructions:
        for i in range(instruction[0]):
            stacks[instruction[2] - 1].append(stacks[instruction[1] - 1].pop())

with open('input.txt', 'r') as data:
    [stack_input, instruction_input] = data.read().split('\n\n')
    stacks = create_stacks(stack_input)
    instructions = parse_instructions(instruction_input)
    execute_instructions(stacks, instructions)
    print(''.join([stack[-1] for stack in stacks.values()]))