''' General implementation takes incredibly long to run. Noticing that for any start node there is
only one path to an end node, we can achieve a much more efficient solution by finding the LCM of
the length of all paths from start node to end node. '''

import re
from collections import defaultdict, deque
from math import lcm

# Get directions and paths
file = open('day8_input.txt', 'r')
lines = file.readlines()
file.close()

# Construct adjacency list representation of source node to left and right destinations
# Get all starting nodes: nodes that end with an 'A'
adj_list = defaultdict(list)
start_nodes = deque()
for i in range(2, len(lines)):
    src_and_dests = lines[i].split('=')
    src, dests = src_and_dests[0].strip(), src_and_dests[1]
    dests = dests.split(',')
    match1, match2 = re.search('\w+', dests[0]), re.search('\w+', dests[1])
    dest1, dest2 = match1.group(), match2.group()
    adj_list[src].append(dest1)
    adj_list[src].append(dest2)

    if src[-1] == 'A':
        start_nodes.append(src)

# Find the length of all paths from start to end nodes where an end node is a node that ends in 'Z'
directions = lines[0].strip()
start_to_end_len = dict()
for start_node in start_nodes:
    steps = 0
    cur_node = start_node
    end_found = False
    while not end_found:
        for dir in directions:
            dests = adj_list[cur_node]
            left_dest, right_dest = dests[0], dests[1]
            if dir == 'L':
                cur_node = left_dest
            else:
                cur_node = right_dest
            steps += 1
            if cur_node[-1] == 'Z':
                start_to_end_len[start_node] = steps
                end_found = True
                break

# Find the LCM of all path lengths
print(lcm(*start_to_end_len.values())) # My puzzle answer: 13129439557681