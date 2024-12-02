import re
from collections import Counter

with open('input.txt', 'r') as puzzle_input:
    left_numbers, right_numbers = [], []
    for line in puzzle_input.read().split('\n'):
        left, right = re.split(r'\s+', line)
        left_numbers.append(int(left))
        right_numbers.append(int(right))

right_numbers_count = Counter(right_numbers)

sum = 0

for num in left_numbers:
    sum += num * right_numbers_count[num]

print(sum)