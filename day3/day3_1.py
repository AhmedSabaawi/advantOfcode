def read_grid(file_path):
    """Read the grid from a file."""
    with open(file_path) as file:
        return file.read().splitlines()


def find_number_starts(grid):
    """Find starting points of all numbers in the grid."""
    number_starts = set()

    for row_index, row in enumerate(grid):
        for col_index, char in enumerate(row):
            if char.isdigit() or char == ".":
                continue

            # Check adjacent cells for the start of a number
            for delta_row in range(-1, 2):
                for delta_col in range(-1, 2):
                    adj_row, adj_col = row_index + delta_row, col_index + delta_col
                    if (
                        0 <= adj_row < len(grid)
                        and 0 <= adj_col < len(grid[adj_row])
                        and grid[adj_row][adj_col].isdigit()
                    ):
                        # Move to the start of the number
                        while adj_col > 0 and grid[adj_row][adj_col - 1].isdigit():
                            adj_col -= 1
                        number_starts.add((adj_row, adj_col))

    return number_starts


def sum_numbers(grid, number_starts):
    """Sum all numbers starting from the given points."""
    total_sum = 0

    for start_row, start_col in number_starts:
        number_str = ""
        while start_col < len(grid[start_row]) and grid[start_row][start_col].isdigit():
            number_str += grid[start_row][start_col]
            start_col += 1
        total_sum += int(number_str)

    return total_sum


# Main execution
grid = read_grid("day_3_1.txt")
number_starts = find_number_starts(grid)
result = sum_numbers(grid, number_starts)
print(result)
