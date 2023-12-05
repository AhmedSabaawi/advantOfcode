# Read the file and split into blocks
with open("day_5_1.txt") as file:
    blocks = file.read().split("\n\n")

# Extract seeds from the first block and convert them to integers
seeds = [int(x) for x in blocks[0].split(":")[1].split()]

# Iterate over each block except the first one
for block in blocks[1:]:
    # Parse the ranges from the block
    ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]

    # Create a new list of seeds based on the ranges
    new_seeds = []
    for seed in seeds:
        for start, offset, count in ranges:
            if offset <= seed < offset + count:
                new_seeds.append(seed - offset + start)
                break
        else:
            new_seeds.append(seed)

    seeds = new_seeds

# Print the minimum seed value
print(min(seeds))
