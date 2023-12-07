import re

# Get scratch cards
file = open('day4_input.txt', 'r')
scratch_cards = file.readlines()
file.close()

# Calculate the point value of each scratch card - each matching number doubles points starting at 1
total_points = 0
for scratch_card in scratch_cards:
    # Get winning numbers and playing numbers
    nums = re.sub('Card\s+\d+:\s+', '', scratch_card).split('|')
    win_nums = {int(win_num) for win_num in nums[0].split()}
    play_nums = [int(play_num) for play_num in nums[1].split()]

    # Calculate point value of the scratch card
    num_doubles = -1
    for play_num in play_nums:
        if play_num in win_nums:
            num_doubles += 1

    # Update total points if at least one match was found
    if num_doubles != -1:
        total_points += pow(2, num_doubles)

print(total_points) # My puzzle answer: 21088