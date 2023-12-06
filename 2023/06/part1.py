import re
import math

ws_regex = re.compile(r'\s+')

with open('input.txt', 'r') as file:
    lines = [ws_regex.split(line)[1:] for line in file.read().splitlines()]
    
races = []

for i in range(len(lines[0])):
    race = {
        'time': int(lines[0][i]),
        'dist': int(lines[1][i])
    }
    races.append(race)

def get_bp_lengths(time, dist):
    length_one = (-time + math.sqrt(time ** 2 + 4 * -dist)) / -2
    length_two = (-time - math.sqrt(time ** 2 + 4 * -dist)) / -2
    return math.floor(min(length_one, length_two)) + 1, math.ceil(max(length_one, length_two))

product = 1
for race in races:
    bp_length_range = get_bp_lengths(race['time'], race['dist'])
    diff = bp_length_range[1] - bp_length_range[0]
    product *= diff

print(product)