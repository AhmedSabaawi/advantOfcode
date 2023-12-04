def count_matches(card):
    """Count the number of matches between winning numbers and user's numbers."""
    return len(set(card["winning"]) & set(card["user"]))


def process_cards(cards):
    """Process the cards according to the new rules and count the total number of cards."""
    total_cards = len(cards)  # Start with the original number of cards
    card_copies = [1] * len(cards)  # Initialize with one copy of each card

    for i in range(len(cards)):
        matches = count_matches(cards[i])
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    total_cards += sum(card_copies) - len(cards)  # Subtract the original set of cards
    return total_cards


# Re-reading the file and parsing the data
with open("day4_2.txt", "r") as file:
    cards = []
    for line in file:
        _, card_data = line.strip().split(": ")
        winning, user = card_data.split(" | ")
        cards.append(
            {
                "winning": list(map(int, winning.split())),
                "user": list(map(int, user.split())),
            }
        )

total_scratchcards = process_cards(cards)
print(total_scratchcards)
