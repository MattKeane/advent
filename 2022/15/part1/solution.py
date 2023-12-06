with open('input.txt', 'r') as f:
    lines = [line.strip('Sensor at x=') for line in f.read().split('\n')]

for i, line in enumerate(lines):
    sensor_beacon = line.split(': closest beacon is at x=')
    sensor_coords = [int(coord) for coord in sensor_beacon[0].split(', y=')]
    beacon_coords = [int(coord) for coord in sensor_beacon[1].split(', y=')]
    lines[i] = (tuple(sensor_coords), tuple(beacon_coords))

target_y = 2000000

has_beacon = {}

for line in lines:
    has_beacon[line[1]] = True

cant_have_beacon = {}

for line in lines:
    sensor_x, sensor_y = line[0]
    beacon_x, beacon_y = line[1]
    beacon_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    target_distance = abs(sensor_y - target_y)
    if target_distance <= beacon_distance:
        x_range = beacon_distance - target_distance
        for x in range(sensor_x - x_range, sensor_x + x_range + 1):
            if not has_beacon.get((x, target_y)):
                cant_have_beacon[x] = True

print(len(cant_have_beacon))