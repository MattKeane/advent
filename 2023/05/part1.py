with open('input.txt', 'r') as file:
    map_inputs = file.read().split('\n\n')

seeds = [int(seed) for seed in map_inputs[0].split(' ')[1:]]

class GardenMap:
    def __init__(self, dest_start, source_start, length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.source_range = range(source_start, source_start + length)

    def contains_source(self, source):
        return source in self.source_range

    def get_dest(self, source):
        source_diff = source - self.source_start
        return self.dest_start + source_diff

    @classmethod
    def parse_map_input(cls, map_input):
        g_map = map_input.split('\n')[1:]
        g_map = [cls(*[int(num) for num in line.split(' ')]) for line in g_map]
        return g_map

garden_maps = [GardenMap.parse_map_input(map_input) for map_input in map_inputs[1:]]

locations = []

for seed in seeds:
    source = seed
    for garden_map_set in garden_maps:
        for garden_map in garden_map_set:
            if garden_map.contains_source(source):
                source = garden_map.get_dest(source)
                break
    locations.append(source)

print(min(locations))