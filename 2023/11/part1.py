with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

vertical_nonexpansion = {}
horizontal_nonexpansion = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            vertical_nonexpansion[i] = 0
            horizontal_nonexpansion[j] = 0

galaxies = []
vertical_expansion = 0
for i, line in enumerate(lines):
    vertical_expansion += vertical_nonexpansion.get(i, 1)
    horizontal_expansion = 0
    for j, char in enumerate(line):
        horizontal_expansion += horizontal_nonexpansion.get(j, 1)
        if char == '#':
            galaxies.append((j + horizontal_expansion, i + vertical_expansion))


total_distance = 0
for i, galaxy_one in enumerate(galaxies[:-1]):
    for galaxy_two in galaxies[i + 1:]:
        distance = abs(galaxy_one[0] - galaxy_two[0]) + abs(galaxy_one[1] - galaxy_two[1])
        total_distance += distance

print(total_distance)