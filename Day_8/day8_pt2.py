''' General implementation takes incredibly long to run. Noticing that for any start node there is
only one path to an end node, we can achieve a much more efficient solution by finding the LCM of
the length of all paths from start node to end node. '''

import re
from collections import defaultdict, deque

# Get directions and paths
file = open('day8_input.txt', 'r')
lines = file.readlines()
file.close()

# Construct adjacency list representation of source node to left and right destinations
# Get all starting nodes: nodes that end with an 'a'
adj_list = defaultdict(list)
queue = deque()
for i in range(2, len(lines)):
    src_and_dests = lines[i].split('=')
    src, dests = src_and_dests[0].strip(), src_and_dests[1]
    dests = dests.split(',')
    match1, match2 = re.search('\w+', dests[0]), re.search('\w+', dests[1])
    dest1, dest2 = match1.group(), match2.group()
    adj_list[src].append(dest1)
    adj_list[src].append(dest2)

    if src[-1] == 'A':
        queue.append(src)

# Calculate total steps by following directions, repeatedly, from all current nodes until all nodes simultaneously end with 'Z'
directions = lines[0].strip()
all_end_z = False
total_steps = 0
while not all_end_z:
    for dir in directions:
        non_z_end_found = False
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            dests = adj_list[cur_node]
            left_dest, right_dest = dests[0], dests[1]
            if dir == 'L':
                cur_node = left_dest
            else:
                cur_node = right_dest
            queue.append(cur_node)
            if cur_node[-1] != 'Z':
                non_z_end_found = True
        total_steps += 1
        if not non_z_end_found:
            all_end_z = True
            break

print(total_steps) # My puzzle answer: 13129439557681