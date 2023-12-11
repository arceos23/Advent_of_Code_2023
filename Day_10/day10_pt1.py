from collections import deque

# Get tiles
file = open('day10_input.txt', 'r')
tiles = file.readlines()
file.close()

# Tile symbols
VERT   = '|'
HORI   = '-'
NE     = 'L'
NW     = 'J'
SW     = '7'
SE     = 'F'
GROUND = '.'
S      = 'S'

# Pipes
PIPES = set([VERT, HORI, NE, NW, SW, SE])

# Directions
LEFT  = (0, -1)
RIGHT = (0, 1)
UP    = (-1, 0)
DOWN  = (1, 0)

# Pipes to directions
PIPE_TO_DIRS = {VERT: (UP, DOWN),
                HORI: (LEFT, RIGHT),
                NE:   (UP, RIGHT),
                NW:   (UP, LEFT),
                SE:   (DOWN, RIGHT),
                SW:   (DOWN, LEFT)}

# Find starting pipe
m, n = len(tiles), len(tiles[0])
start = None
for i in range(m):
    for j in range(len(tiles[i])):
        if tiles[i][j] == S:
            start = (i, j)
            break

# Calculate number of steps along the loop from the starting position to the point farthest from the starting position
# Initialize queue with valid pipes connecting to the starting pipe
i, j = start
queue = deque([start])
visited = set([start])
for row_move, col_move in [UP, DOWN, LEFT, RIGHT]:
    adj_i, adj_j = i + row_move, j + col_move
    if adj_i < 0 or adj_j < 0 or adj_i >= m or adj_j >= len(tiles[i]):
        continue
    for row_move, col_move in PIPE_TO_DIRS[tiles[adj_i][adj_j]]:
        if adj_i + row_move == i and adj_j + col_move == j:
            next_cell = (adj_i, adj_j)
            if next_cell not in visited:
                visited.add(next_cell)
                queue.append(next_cell)

# BFS until the the last pipe has been traversed, counting the number of steps
max_num_steps = 0
while queue:
    for _ in range(len(queue)):
        cell = queue.popleft()
        i, j = cell
        tile = tiles[i][j]
        if tile == GROUND or tile == 'S':
            continue
        for row_move, col_move in PIPE_TO_DIRS[tile]:
            adj_i, adj_j = i + row_move, j + col_move
            next_cell = (adj_i, adj_j)
            if next_cell not in visited:
                visited.add(next_cell)
                queue.append(next_cell)
    max_num_steps += 1

print(max_num_steps) # My puzzle answer: 6714