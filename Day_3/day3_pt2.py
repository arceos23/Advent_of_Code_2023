# Get engine schematic
file = open('day3_input.txt', 'r')
engine_schematic = file.readlines()
file.close()

ROWS = len(engine_schematic)

# Up, down, left, right, up-left, up-right, down-left, down-right
ADJ_DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

# Mapping of location of an asterisk to its status as a gear and gear ratio
gear_to_ratio = dict() # (i, j) -> [False | True, gear ratio]

# Update gear_to_ratio mapping based on engine schematic
for i, line in enumerate(engine_schematic):
    line = line.strip()
    j, cols = 0, len(line)
    while j < cols:
        part_num = 0
        asterisk_locations = set()
        while j < cols and line[j].isdecimal():
            # Build part number
            part_num *= 10
            part_num += int(line[j])

            # Track all astericks adjacent to the part number
            if not asterisk_locations:
                for row_move, col_move in ADJ_DIRS:
                    adj_i, adj_j = i + row_move, j + col_move
                    if adj_i < 0 or adj_j < 0 or adj_i >= ROWS or adj_j >= cols:
                        continue
                    if engine_schematic[adj_i][adj_j] == '*':
                        asterisk_locations.add((adj_i, adj_j))
                        break

            j += 1

        # Update asterisk status and gear ratio for all asterisks found adjacent to the part number
        for asterisk_location in asterisk_locations:
            if asterisk_location not in gear_to_ratio.keys():
                gear_to_ratio[asterisk_location] = [False, part_num]
            else:
                gear_to_ratio[asterisk_location][0] = True
                gear_to_ratio[asterisk_location][1] *= part_num
        
        j += 1

# Calculate sum of all gear ratios
sum_gear_ratios = 0
for is_gear, gear_ratio in gear_to_ratio.values():
    if is_gear:
        sum_gear_ratios += gear_ratio

print(sum_gear_ratios) # My puzzle answer: 87263515