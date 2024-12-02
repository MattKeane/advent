import re

with open('input.txt', 'r') as puzzle_input:
    left_numbers, right_numbers = [], []
    for line in puzzle_input.read().split('\n'):
        left, right = re.split(r'\s+', line)
        left_numbers.append(int(left))
        right_numbers.append(int(right))

sorted_left_numbers = sorted(left_numbers)
sorted_right_numbers = sorted(right_numbers)

sum = 0

for i in range(len(sorted_left_numbers)):
    sum += abs(sorted_left_numbers[i] - sorted_right_numbers[i])

print(sum)