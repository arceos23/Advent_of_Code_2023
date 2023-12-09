import re

# Get almanac
file = open('day5_input.txt', 'r')
almanac = file.readlines()
file.close()

# Get seed ranges
i, ROWS = 0, len(almanac)
seed_line = re.sub('seeds:\s+', '', almanac[i]).strip().split()
seed_to_range = dict()
for j in range(0, len(seed_line), 2):
    seed_to_range[int(seed_line[j])] = int(seed_line[j + 1])

# Mapping names
seed_to_soil = "seed-to-soil"
soil_to_fertilizer = "soil-to-fertilizer"
fertilizer_to_water = "fertilizer-to-water"
water_to_light = "water-to-light"
light_to_temperature = "light-to-temperature"
temperature_to_humidity = "temperature-to-humidity"
humidity_to_location = "humidity-to-location"
mapping_names = {seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
                 light_to_temperature, temperature_to_humidity, humidity_to_location}

# Mappings
seed_to_soil_map = dict()
soil_to_fertilizer_map = dict()
fertilizer_to_water_map = dict()
water_to_light_map = dict()
light_to_temperature_map = dict()
temperature_to_humidity_map = dict()
humidity_to_location_map = dict()
mappings = (seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map,
            light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map)

# Loads mappings with their respective lists of source to (destination, range) pairs
def load_mapping(mapping, start):
    for i in range(start, ROWS):
        line = almanac[i].strip().split()
        if not line:
            break
        dest, src, _range = int(line[0]), int(line[1]), int(line[2])
        mapping[src] = (dest, _range)

# Create mappings from the almanac
while i < ROWS:
    first_word = almanac[i].split(maxsplit=1)[0] if almanac[i].split(maxsplit=1) else ''
    if first_word and first_word in mapping_names:
        i += 1
        match first_word:
            case "seed-to-soil":
                load_mapping(seed_to_soil_map, i)
            case "soil-to-fertilizer":
                load_mapping(soil_to_fertilizer_map, i)
            case "fertilizer-to-water":
                load_mapping(fertilizer_to_water_map, i)
            case "water-to-light":
                load_mapping(water_to_light_map, i)
            case "light-to-temperature":
                load_mapping(light_to_temperature_map, i)
            case "temperature-to-humidity":
                load_mapping(temperature_to_humidity_map, i)
            case "humidity-to-location":
                load_mapping(humidity_to_location_map, i)
    i += 1

# Find the lowest location number by starting with a seed and traversing over each map to get its location
lowest_location_num = float('inf')
for seed_start, seed_range in seed_to_range.items():
    for seed in range(seed_start, seed_start + seed_range):
        location = seed
        for map in mappings:
            for src, pair in map.items():
                dest, _range = pair
                if location >= src and location <= src + _range:
                    location += dest - src
                    break
        lowest_location_num = min(lowest_location_num, location)

print(lowest_location_num) # My puzzle answer: 63179500