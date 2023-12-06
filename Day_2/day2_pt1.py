import re

# Get games
file = open('day2_input.txt', 'r')
games = file.readlines()
file.close()

# Game contraints
COLOR_TO_COUNT = {'red': 12, 'green': 13, 'blue': 14}

# Create sets of all game ids and all invalid game ids
game_ids = set()
invalid_game_ids = set()
for game in games:

    # Get game id
    match = re.search('\d+', game)
    game_id = match.group()
    game_ids.add(game_id)

    # Get the cube sets of each game
    cube_sets = [cube_set.strip() for cube_set in re.sub('Game\s\d+:\s', '', game).split(';')]

    # Check if the game is invalid by checking if any round in the game is invalid
    invalid_game = False
    for cube_set in cube_sets:
        rounds_played = cube_set.split(',')
        for round_played in rounds_played:
            cleaned_round_played = round_played.split()
            count, color = cleaned_round_played[0], cleaned_round_played[1]
            if int(count) > COLOR_TO_COUNT[color]:
                invalid_game_ids.add(game_id)
                invalid_game = True
                break
        if invalid_game:
            break

# Calculate the sum of all valid game ids
valid_game_ids = [int(game_id) for game_id in game_ids.difference(invalid_game_ids)]
print(sum(valid_game_ids)) # My puzzle answer: 2331