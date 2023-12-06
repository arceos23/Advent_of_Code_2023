# Get engine schematic
file = open('day3_input.txt', 'r')
engine_schematic = file.readlines()
file.close()

ROWS = len(engine_schematic)

# Up, down, left, right, up-left, up-right, down-left, down-right
ADJ_DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

# Calculate the sum of all part numbers in the engine schematic
sum_part_nums = 0
for i, line in enumerate(engine_schematic):
    line = line.strip()
    j, cols = 0, len(line)
    while j < cols:
        part_num = 0
        is_symbol_adj = False
        while j < cols and line[j].isdecimal():
            # Build part number
            part_num *= 10
            part_num += int(line[j])

            # Check if at least one digit of the part number is adjacent to a symbol: non-digit and not a '.'
            if not is_symbol_adj:
                for row_move, col_move in ADJ_DIRS:
                    adj_i, adj_j = i + row_move, j + col_move
                    if adj_i < 0 or adj_j < 0 or adj_i >= ROWS or adj_j >= cols:
                        continue
                    if engine_schematic[adj_i][adj_j].isdecimal() or engine_schematic[adj_i][adj_j] == '.':
                        continue
                    is_symbol_adj = True
                    break

            j += 1

        if is_symbol_adj:
            sum_part_nums += part_num
        
        j += 1

print(sum_part_nums) # My puzzle answer: 554003