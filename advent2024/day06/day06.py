import os

from advent2024.common.model import Base

test_solution_01 = 41
test_solution_02 = 6


class Input(Base):
    pass


def parse_data(data: str):
    return [list(line.strip()) for line in data.splitlines()]


def find_start(data: list[list[str]]):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == "^":
                return (j, i)


def puzzle01(data: list[list[str]], test: bool):
    print("Day 06 Puzzle 01")
    solution = 1
    j, i = find_start(data)
    m, n = len(data), len(data[0])
    exit = False
    direction = "^"
    data[i][j] = "X"
    while not exit:
        if direction == "^":
            if i == 0:
                exit = True
                break
            if data[i - 1][j] == "." or data[i - 1][j] == "X":
                i -= 1
                solution += 1 if data[i][j] == "." else 0
                data[i][j] = "X"
            else:
                direction = ">"
        elif direction == ">":
            if j == n - 1:
                exit = True
                break
            if data[i][j + 1] == "." or data[i][j + 1] == "X":
                j += 1
                solution += 1 if data[i][j] == "." else 0
                data[i][j] = "X"
            else:
                direction = "v"
        elif direction == "v":
            if i == m - 1:
                exit = True
                break
            if data[i + 1][j] == "." or data[i + 1][j] == "X":
                i += 1
                solution += 1 if data[i][j] == "." else 0
                data[i][j] = "X"
            else:
                direction = "<"
        elif direction == "<":
            if j == 0:
                exit = True
                break
            if data[i][j - 1] == "." or data[i][j - 1] == "X":
                j -= 1
                solution += 1 if data[i][j] == "." else 0
                data[i][j] = "X"
            else:
                direction = "^"
    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 06 Puzzle 01 Done")


def simulate_guard_with_obstruction(grid, obstruction_pos):
    # Define the directions: up, right, down, left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direction_index = 0  # Start facing "up"

    # Find the initial position of the guard
    start_position = find_start(grid)
    x, y = start_position

    visited_states = set()
    rows, cols = len(grid), len(grid[0])

    while 0 <= x < cols and 0 <= y < rows:
        # Record the current state (position and direction)
        state = (x, y, direction_index)
        if state in visited_states:
            return True  # Loop detected
        visited_states.add(state)

        # Calculate the next position
        dx, dy = directions[direction_index]
        next_x, next_y = x + dx, y + dy

        # Check if the next position is an obstruction or out of bounds
        if (next_x, next_y) == obstruction_pos or (
            0 <= next_x < cols and 0 <= next_y < rows and grid[next_y][next_x] == "#"
        ):
            # Turn right
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            x, y = next_x, next_y

    return False  # No loop detected


def find_loop_positions(grid):
    loop_positions = []
    start_position = find_start(grid)
    print(start_position)
    rows, cols = len(grid), len(grid[0])

    for y in range(rows):
        for x in range(cols):
            if (
                grid[y][x] == "." and (x, y) != start_position
            ):  # Skip the starting position
                if simulate_guard_with_obstruction(grid, (x, y)):
                    loop_positions.append((x, y))

    return loop_positions


def puzzle02(data: list[list[str]], test: bool):
    print("Day 06 Puzzle 02")
    solution = 1
    loop_positions = find_loop_positions(data)
    print(loop_positions)
    solution = len(loop_positions)
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 06 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = parse_data(file.read())

    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
