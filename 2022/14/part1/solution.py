with open('input.txt', 'r') as f:
    walls = [[[int(coordinate) for coordinate in coordinates.split(',')] for coordinates in line.split(' -> ')] for line in f.read().split('\n')]

occupied = {}
max_depth = 0

for wall in walls:
    x, y = wall[0]
    if y > max_depth:
        max_depth = y
    occupied[(x, y)] = True
    for coordinates in wall[1:]:
        new_x, new_y = coordinates
        while x != new_x:
            delta_x = new_x - x
            x += int(abs(delta_x) / delta_x)
            occupied[(x, y)] = True
        while y != new_y:       
            delta_y = new_y - y
            y += int(abs(delta_y)/ delta_y)
            if y > max_depth:
                max_depth = y
            occupied[(x, y)] = True

count = 0
while True:
    x, y = 500, 0
    while y < max_depth:
        if not occupied.get((x, y + 1)):
            y += 1
        elif not occupied.get((x - 1, y + 1)):
            x -= 1
            y += 1
        elif not occupied.get((x + 1, y + 1)):
            x += 1
            y += 1
        else:
            occupied[(x, y)] = True
            break
    if y >= max_depth:
        print(count)
        break
    count += 1