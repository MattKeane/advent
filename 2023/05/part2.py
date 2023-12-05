with open('input.txt', 'r') as file:
    map_inputs = file.read().split('\n\n')

seed_inputs = [int(seed) for seed in map_inputs[0].split(' ')[1:]]
seed_ranges = [(seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]) for i in range(0, len(seed_inputs), 2)]

class GardenMap:
    def __init__(self, dest_start, source_start, length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.source_end = source_start + length
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

dest_ranges = seed_ranges

for garden_map_set in garden_maps:
    new_dest_ranges = []
    for dest_range in dest_ranges:
        i = dest_range[0]
        while i < dest_range[1]:
            for garden_map in garden_map_set:
                if garden_map.contains_source(i):
                    if dest_range[1] < garden_map.source_end:
                        new_dest_ranges.append((garden_map.get_dest(i), garden_map.get_dest(dest_range[1])))
                        i = dest_range[1]
                        break
                    else:
                        new_dest_ranges.append((garden_map.get_dest(i), garden_map.get_dest(garden_map.source_end)))
                        i = garden_map.source_end
                        break
            else:
                next_lowest = dest_range[1]
                for garden_map in garden_map_set:
                    if garden_map.source_start > i and garden_map.source_start < next_lowest:
                        next_lowest = garden_map.source_start
                new_dest_ranges.append((i, next_lowest))
                i = next_lowest
    dest_ranges = new_dest_ranges

print(min([dest_range[0] for dest_range in dest_ranges]))