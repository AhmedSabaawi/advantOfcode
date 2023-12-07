# Map for letter cards
letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


def score(hand):
    # Count the frequency of each card in the hand
    counts = {card: hand.count(card) for card in set(hand)}

    # Determine the score based on poker hand rankings
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


def replacements(hand):
    if not hand:
        return [""]

    first_char_options = "23456789TQKA" if hand[0] == "J" else hand[0]
    return [x + y for x in first_char_options for y in replacements(hand[1:])]


def classify(hand):
    return max(score(replacement) for replacement in replacements(hand))


def strength(hand):
    return classify(hand), [letter_map.get(card, card) for card in hand]


plays = []

# Process each line in the file
with open("day7_1.txt") as file:
    for line in file:
        hand, bid = line.strip().split()
        plays.append((hand, int(bid)))

# Sort the plays based on hand strength
plays.sort(key=lambda play: strength(play[0]))

# Calculate the total score
total = sum(rank * bid for rank, (hand, bid) in enumerate(plays, 1))

print(total)
