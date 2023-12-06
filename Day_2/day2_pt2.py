import re
from collections import defaultdict

# Get games
file = open('day2_input.txt', 'r')
games = file.readlines()
file.close()

''' Calculate the total power of all games where the power of a game is defined as the minimum
number of dice needed for each color to make a game valid '''
total_game_power = 0
for game in games:

    # Get the cube sets of each game
    cube_sets = [cube_set.strip() for cube_set in re.sub('Game\s\d+:\s', '', game).split(';')]

    # Find the minimum number of dice needed for each color to make the game valid
    color_to_count = defaultdict(int)
    for cube_set in cube_sets:
        rounds_played = cube_set.split(',')
        for round_played in rounds_played:
            cleaned_round_played = round_played.split()
            count, color = cleaned_round_played[0], cleaned_round_played[1]
            color_to_count[color] = max(color_to_count[color], int(count))

    # Update the total game power for the power of the current game
    min_set_power = 1
    for count in color_to_count.values():
        min_set_power *= count
    total_game_power += min_set_power

print(total_game_power) # My puzzle answer: 71585