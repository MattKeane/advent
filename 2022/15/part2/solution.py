class Sensor:
    def __init__(self, sensor_coords, beacon_coords):
        self.location = sensor_coords
        self.beacon = beacon_coords
        self.x, self.y = self.location
        self.beacon_distance = abs(self.x - self.beacon[0]) + abs(self.y - self.beacon[1])
        Sensor.sensors.append(self)

    def check_too_close(self, x, y):
        distance = abs(self.x - x) + abs(self.y - y)
        return distance <= self.beacon_distance

    def check_sensors(self, x, y):
        for sensor in Sensor.sensors:
            if sensor.check_too_close(x, y):
                return True

    def check_perimeter(self, max_value):
        radius = self.beacon_distance + 1
        for i in range(radius):
            x = self.x + i
            y = self.y + radius - i
            if x > max_value or y > max_value:
                continue
            if x < 0 or y < 0:
                continue
            if not self.check_sensors(x, y):
                return x, y
        for i in range(radius):
            x = self.x + radius - i
            y = self.y - i
            if x > max_value or y > max_value:
                continue
            if x < 0 or y < 0:
                continue
            if not self.check_sensors(x, y):
                return x, y
        for i in range(radius):
            x = self.x - i
            y = self.y - radius + i
            if x > max_value or y > max_value:
                continue
            if x < 0 or y < 0:
                continue
            if not self.check_sensors(x, y):
                return x, y
        for i in range(radius):
            x = self.x - radius + i
            y = self.y + i
            if x > max_value or y > max_value:
                continue
            if x < 0 or y < 0:
                continue
            if not self.check_sensors(x, y):
                return x, y

    sensors = []

                
with open('input.txt', 'r') as f:
    lines = [line.strip('Sensor at x=') for line in f.read().split('\n')]

for i, line in enumerate(lines):
    sensor_beacon = line.split(': closest beacon is at x=')
    sensor_coords = [int(coord) for coord in sensor_beacon[0].split(', y=')]
    beacon_coords = [int(coord) for coord in sensor_beacon[1].split(', y=')]
    lines[i] = (tuple(sensor_coords), tuple(beacon_coords))

for line in lines:
    Sensor(line[0], line[1])

for i, sensor in enumerate(Sensor.sensors):
    perimeter = sensor.check_perimeter(4000000)
    if perimeter:
        print(perimeter[0] * 4000000 + perimeter[1])
        break