from GetAocInput import get_aoc_input

DAY = 4
input_data = get_aoc_input(4)

global_counter = 0
x_mas_counter = 0


def main():
    global global_counter, x_mas_counter
    global_counter = 0  # Reset counter for Part 1
    x_mas_counter = 0  # Reset counter for Part 2

    test_data = list(map(list, (input_data).splitlines()))

    # Part 1: Check for "XMAS" in all directions
    for row, line in enumerate(test_data):
        for col, element in enumerate(line):
            if element == "X":
                check_all_directions(test_data, row, col)

    # Part 2: Check for "X-MAS" patterns
    for row, line in enumerate(test_data):
        for col, element in enumerate(line):
            if element == "A":  # Focus on 'A' as the center of X-MAS
                check_x_mas_pattern(test_data, row, col)

    print("Total 'XMAS' Matches (Part 1):", global_counter)
    print("Total 'X-MAS' Matches (Part 2):", x_mas_counter)


    print("---------")
    print(test_data)


def check_all_directions(test_data, x, y):

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Diagonal Up-Left
        (-1, 1),  # Diagonal Up-Right
        (1, -1),  # Diagonal Down-Left
        (1, 1)    # Diagonal Down-Right
    ]
    for dx, dy in directions:
        check_direction(test_data, x, y, dx, dy)


def check_direction(test_data, x, y, dx, dy):

    global global_counter

    word = ["X"]
    row, col = x, y

    while 0 <= row + dx < len(test_data) and 0 <= col + dy < len(test_data[0]) and len(word) < 4:
        row += dx
        col += dy
        word.append(test_data[row][col])

    word_string = "".join(word)
    if word_string == "XMAS":
        global_counter += 1


def check_x_mas_pattern(test_data, x, y):
    """
    Check if two diagonals centered at (x, y) form "MAS"
    """
    global x_mas_counter

    diagonal_pairs = [
        [(-1, -1), (1, 1)],  # ↖️ ↘️
        [(-1, 1), (1, -1)]   # ↗️ ↙️
    ]

    for dir1, dir2 in diagonal_pairs:
        word1 = extract_diagonal_word(test_data, x, y, dir1)
        word2 = extract_diagonal_word(test_data, x, y, dir2)

        if word1 == "MAS" and word2 == "SAM":
            x_mas_counter += 1


def extract_diagonal_word(test_data, x, y, direction):
    word = []
    for i in range(1, 4):
        x_new = x + direction[0] * i
        y_new = y + direction[1] * i

        if 0 <= x_new < len(test_data) and 0 <= y_new < len(test_data[0]):
            word.append(test_data[x_new][y_new])
        else:
            return ""
    return "".join(word)


    # Check both "MAS" and "SAM"
    return "".join(word) in ["MAS", "SAM"]

if __name__ == "__main__":
    main()