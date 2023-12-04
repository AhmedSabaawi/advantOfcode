# First, let's read the file and parse the data
cards = []


# Function to calculate the points for each card
def calculate_points(card):
    matches = set(card["winning"]) & set(card["user"])
    return 2 ** len(matches) // 2 if matches else 0


# Adjusted file reading process
with open("day4_1.txt", "r") as file:
    for line in file:
        # Extracting the part after the colon and splitting by '|'
        _, card_data = line.strip().split(": ")
        winning, user = card_data.split(" | ")
        cards.append(
            {
                "winning": list(map(int, winning.split())),
                "user": list(map(int, user.split())),
            }
        )

# Now, let's calculate the total points
total_points = sum(calculate_points(card) for card in cards)
print(total_points)
