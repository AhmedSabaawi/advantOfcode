# Mapping of letter cards to their corresponding values
letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


def classify(hand):
    # Count the frequency of each card in the hand
    counts = {card: hand.count(card) for card in set(hand)}

    # Check for different poker hand rankings
    if 5 in counts.values():
        return 6
    if 4 in counts.values():
        return 5
    if 3 in counts.values():
        return 4 if 2 in counts.values() else 3
    if list(counts.values()).count(2) == 2:
        return 2
    if 2 in counts.values():
        return 1
    return 0


def strength(hand):
    # Calculate the strength of the hand
    return (classify(hand), [letter_map.get(card, card) for card in hand])


plays = []

# Read and process each line in the file
with open("day7_1.txt") as file:
    for line in file:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

# Sort the plays based on the strength of each hand
plays.sort(key=lambda play: strength(play[0]))

total = 0

# Calculate the total score
for rank, (hand, bid) in enumerate(plays, 1):
    total += rank * bid

print(total)
