# Re-defining the function as the execution state was reset
def calculate_ways(time, distance):
    ways = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        travel_distance = hold_time * travel_time
        if travel_distance > distance:
            ways += 1
    return ways


# Parsing the new input for a single race by removing spaces
time_single_race = int(
    "".join([str(t) for t in [48, 87, 69, 81]])
)  # Joining the times and converting to integer
distance_single_race = int(
    "".join([str(d) for d in [255, 1288, 1117, 1623]])
)  # Joining the distances and converting to integer

# Calculating the number of ways to win this specific single race
ways_specific_race = calculate_ways(time_single_race, distance_single_race)
ways_specific_race
print(ways_specific_race)
