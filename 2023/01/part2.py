import re

with open('input.txt', 'r') as data:
    lines = data.read().split('\n')

def get_calibration_value(line):
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    if re.match(r'\d', digits[0]):
        first_digit = digits[0]
    else:
        first_digit = numbers[digits[0]]

    if re.match(r'\d', digits[-1]):
        last_digit = digits[-1]
    else:
        last_digit = numbers[digits[-1]]

    return int(first_digit + last_digit)

total = sum([get_calibration_value(line) for line in lines])

print(total)