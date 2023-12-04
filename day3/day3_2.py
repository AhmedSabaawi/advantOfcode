# Read the file and split into lines
grid = open("day_3_2.txt").read().splitlines()
total_sum = 0

# Iterate through each character in the grid
for row_index, row in enumerate(grid):
    for col_index, character in enumerate(row):
        # Skip non-asterisk characters
        if character != "*":
            continue

        coordinate_set = set()

        # Check surrounding characters
        for check_row in [row_index - 1, row_index, row_index + 1]:
            for check_col in [col_index - 1, col_index, col_index + 1]:
                # Conditions to skip the character
                if (
                    check_row < 0
                    or check_row >= len(grid)
                    or check_col < 0
                    or check_col >= len(grid[check_row])
                    or not grid[check_row][check_col].isdigit()
                ):
                    continue
                # Adjust column index for multi-digit numbers
                while check_col > 0 and grid[check_row][check_col - 1].isdigit():
                    check_col -= 1
                coordinate_set.add((check_row, check_col))

        # Process only if exactly two distinct coordinates are found
        if len(coordinate_set) != 2:
            continue

        number_list = []

        # Extract numbers from the coordinates
        for cr, cc in coordinate_set:
            number_str = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                number_str += grid[cr][cc]
                cc += 1
            number_list.append(int(number_str))

        # Calculate product and add to total
        total_sum += number_list[0] * number_list[1]

# Print the result
print("---")
print(total_sum)
