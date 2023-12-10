import re
from collections import defaultdict

# Get directions and paths
file = open('day8_input.txt', 'r')
lines = file.readlines()
file.close()

# Construct adjacency list representation of source node to left and right destinations
adj_list = defaultdict(list)
for i in range(2, len(lines)):
    src_and_dests = lines[i].split('=')
    src, dests = src_and_dests[0].strip(), src_and_dests[1]
    dests = dests.split(',')
    match1, match2 = re.search('\w+', dests[0]), re.search('\w+', dests[1])
    dest1, dest2 = match1.group(), match2.group()
    adj_list[src].append(dest1)
    adj_list[src].append(dest2)

# Follow directions, repeatedly, until a path is found from node 'AAA' to node 'ZZZ'
directions = lines[0].strip()
cur_node, end_node = 'AAA', 'ZZZ'
total_steps = 0
end_found = False
while not end_found:
    for dir in directions:
        dests = adj_list[cur_node]
        left_dest, right_dest = dests[0], dests[1]
        if dir == 'L':
            cur_node = left_dest
        else:
            cur_node = right_dest
        total_steps += 1
        if cur_node == end_node:
            end_found = True
            break

print(total_steps) # My puzzle answer: 13771