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


def is_game_possible(game, max_cubes):
    """
    Determine if a game is possible given the maximum number of cubes of each color.

    Parameters:
    game (list): The game data as a list of tuples (color, count).
    max_cubes (dict): A dictionary with the maximum number of cubes of each color.

    Returns:
    bool: True if the game is possible, False otherwise.
    """
    for color, count in game:
        if count > max_cubes[color]:
            return False
    return True


def calculate_possible_games_sum(games, max_cubes):
    """
    Calculate the sum of IDs of games that are possible with the given maximum cubes.

    Parameters:
    games (dict): The games data.
    max_cubes (dict): A dictionary with the maximum number of cubes of each color.

    Returns:
    int: The sum of IDs of possible games.
    """
    return sum(
        game_id
        for game_id, game_data in games.items()
        if is_game_possible(game_data, max_cubes)
    )


# Main execution
file_path = "day_2_1.txt"
max_cubes = {"red": 12, "green": 13, "blue": 14}
games_from_file = read_games_from_file(file_path)
possible_games_sum = calculate_possible_games_sum(games_from_file, max_cubes)

print(possible_games_sum)
