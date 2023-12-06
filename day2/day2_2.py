def parse_game_data(line):
    """
    Parse a line of game data into a dictionary format.

    Parameters:
    line (str): A string representing a line from the game data file.

    Returns:
    tuple: A tuple containing the game ID and a list of tuples with cube color and count.
    """
    game_id, data = line.split(": ")
    game_id = int(game_id.split(" ")[1])  # Extracting the game number
    subsets = data.split("; ")
    game_data = []
    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            game_data.append((color, int(count)))
    return game_id, game_data


def read_games_from_file(file_path):
    """
    Read game data from a file and return it in a structured format.

    Parameters:
    file_path (str): The path to the file containing game data.

    Returns:
    dict: A dictionary with game IDs as keys and game data as values.
    """
    try:
        with open(file_path) as f:
            lines = f.read().splitlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    games = {}
    for line in lines:
        game_id, game_data = parse_game_data(line)
        games[game_id] = game_data
    return games


def minimum_cubes_required(game):
    """
    Calculate the minimum number of cubes of each color required for a game.

    Parameters:
    game (list): The game data as a list of tuples (color, count).

    Returns:
    dict: A dictionary with the minimum number of cubes required for each color.
    """
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for color, count in game:
        min_cubes[color] = max(min_cubes[color], count)
    return min_cubes


def calculate_power_of_set(cubes):
    """
    Calculate the power of a set of cubes.

    Parameters:
    cubes (dict): A dictionary with the number of cubes of each color.

    Returns:
    int: The power of the set, calculated as the product of the numbers of cubes of each color.
    """
    return cubes["red"] * cubes["green"] * cubes["blue"]


# Main execution
file_path = "day_2_2.txt"
games_from_file = read_games_from_file(file_path)

# Calculate the minimum set of cubes for each game and their power
total_power = 0
for game_id, game_data in games_from_file.items():
    max_cubes = minimum_cubes_required(game_data)
    game_power = calculate_power_of_set(max_cubes)
    total_power += game_power

print(total_power)
