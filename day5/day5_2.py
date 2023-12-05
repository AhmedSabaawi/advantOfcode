# Read the input file and split it into blocks
with open("day_5_1.txt") as file:
    blocks = file.read().strip().split("\n\n")

# Process the input values
input_values = list(map(int, blocks[0].split(":")[1].split()))
seed_ranges = [
    (input_values[i], input_values[i] + input_values[i + 1])
    for i in range(0, len(input_values), 2)
]

# Process each block
for block in blocks[1:]:
    line_ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
    new_ranges = []

    while seed_ranges:
        start, end = seed_ranges.pop()
        for a, b, c in line_ranges:
            overlap_start = max(start, b)
            overlap_end = min(end, b + c)
            if overlap_start < overlap_end:
                new_ranges.append((overlap_start - b + a, overlap_end - b + a))
                if overlap_start > start:
                    seed_ranges.append((start, overlap_start))
                if end > overlap_end:
                    seed_ranges.append((overlap_end, end))
                break
        else:
            new_ranges.append((start, end))

    seed_ranges = new_ranges

# Print the minimum value in the seed ranges
print(min(seed_ranges)[0])
