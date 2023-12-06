# 1. Determine the number of ways to beat the record in each race.
# 2. Multiply these numbers together.


# Re-defining the function as the execution state was reset
def calculate_ways(time, distance):
    ways = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        travel_distance = hold_time * travel_time
        if travel_distance > distance:
            ways += 1
    return ways


# Parsing the input for Part 1
times_part1 = [48, 87, 69, 81]
distances_part1 = [255, 1288, 1117, 1623]

# Calculating ways for each race in Part 1
ways_per_race_part1 = [
    calculate_ways(time, distance)
    for time, distance in zip(times_part1, distances_part1)
]

# Multiplying the results together for Part 1
result_part1 = 1
for ways in ways_per_race_part1:
    result_part1 *= ways

print(f"Part 1: {result_part1}")
