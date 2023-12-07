import re
from collections import defaultdict

# Get scratch cards
file = open('day4_input.txt', 'r')
scratch_cards = file.readlines()
file.close()

# Calculate the total number of winning cards (originals and copies)
card_id_to_num_copies = defaultdict(int)
total_scratchcards = 0
for scratchcard in scratch_cards:
    # Get scratchcard id
    match = re.search('\d+', scratchcard)
    card_id = int(match.group())
    
    # Get winning numbers and playing numbers
    nums = re.sub('Card\s+\d+:\s+', '', scratchcard).split('|')
    win_nums = {int(win_num) for win_num in nums[0].split()}
    play_nums = [int(play_num) for play_num in nums[1].split()]

    # Calculate the number of wins for a single card
    num_wins = 0
    for play_num in play_nums:
        if play_num in win_nums:
            num_wins += 1

    # Update for the original card
    card_id_to_num_copies[card_id] += 1

    # Update for the number of current cards (original and copies)
    total_scratchcards += card_id_to_num_copies[card_id]

    # Update for copies earned based on the number of current cards (original and copies)
    for i in range(1, num_wins + 1):
        card_id_to_num_copies[card_id + i] += card_id_to_num_copies[card_id]

print(total_scratchcards) # My puzzle answer: 6874754