from collections import defaultdict

# Get hands and bids input
file = open('day7_input.txt', 'r')
hands_and_bids = file.readlines()
file.close()

# Types of hand to rank
FIVE_OF_KIND  = 7
FOUR_OF_KIND  = 6
FULL_HOUSE    = 5
THREE_OF_KIND = 4
TWO_PAIR      = 3
ONE_PAIR      = 2
HIGH_CARD     = 1

# Calculates the type of hand and encodes it to a rank
def hand_type(hand):
    card_to_freq = defaultdict(int)
    card_types_seen = set()
    for card in hand:
        card_to_freq[card] += 1
        card_types_seen.add(card)
    max_freq = max(card_to_freq.values())
    num_card_types = len(card_types_seen)
    if max_freq == 5:
        return FIVE_OF_KIND
    elif max_freq == 4:
        return FOUR_OF_KIND
    elif max_freq == 3 and num_card_types == 2:
        return FULL_HOUSE
    elif max_freq == 3 and num_card_types == 3:
        return THREE_OF_KIND
    elif max_freq == 2 and num_card_types == 3:
        return TWO_PAIR
    elif max_freq == 2 and num_card_types == 4:
        return ONE_PAIR
    elif max_freq == 1:
        return HIGH_CARD

# Calculates the strength of a hand based on a base 14 encoding
CARD_TO_STRENGTH = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                    '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
def hand_strength(hand):
    num_cards = len(hand)
    _hand_strength = 0
    for i, card in enumerate(hand):
        # Base 14 needed for strengh encoding
        _hand_strength += pow(13, num_cards - i) * CARD_TO_STRENGTH[card]
    return _hand_strength

# Create a list of info (hand type, hand strength, bid) of all hands 
rows = len(hands_and_bids)
rounds_info = [None] * rows
for i, hand_and_bid in enumerate(hands_and_bids):
    hand_and_bid = hand_and_bid.split()
    hand, bid = hand_and_bid[0], int(hand_and_bid[1])
    rounds_info[i] = (hand_type(hand), hand_strength(hand), bid)

# Rank all hands based primarily by rank and secondarily by strength
rounds_info.sort()

# Calculate the total winnings based on bid and rank of each hand
total_winnings = 0
for i, round_info in enumerate(rounds_info):
    total_winnings += (i + 1) * round_info[2]

print(total_winnings) # My puzzle answer: 245794640