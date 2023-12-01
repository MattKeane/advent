import re

with open('input.txt', 'r') as data:
    lines = data.read().split('\n')

def get_calibration_value(line):
    digits = re.findall(r'\d', line)
    return int(digits[0] + digits[-1])

sum = 0

for line in lines:
    sum += get_calibration_value(line)

print(sum)