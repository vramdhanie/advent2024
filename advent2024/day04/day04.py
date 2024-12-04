import os

from advent2024.common.model import Base

test_solution_01 = 18
test_solution_02 = 9


class Input(Base):
    pass


def parse_data(data: str):
    return [list(line) for line in data.splitlines()]


def count_occurrences(i: int, j: int, data: list[list[str]], m: int, n: int):
    # There is an X at i, j
    # Count the XMAS in all 8 directions
    MAS = "XMAS"
    count = 0
    # Up-left
    if i >= 3 and j >= 3:
        valid = True
        for k in range(1, 4):
            if data[i - k][j - k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Up
    if i >= 3:
        valid = True
        for k in range(1, 4):
            if data[i - k][j] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Left
    if j >= 3:
        valid = True
        for k in range(1, 4):
            if data[i][j - k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Down-left
    if i < m - 3 and j >= 3:
        valid = True
        for k in range(1, 4):
            if data[i + k][j - k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Down
    if i < m - 3:
        valid = True
        for k in range(1, 4):
            if data[i + k][j] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Right
    if j < n - 3:
        valid = True
        for k in range(1, 4):
            if data[i][j + k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Down-right
    if i < m - 3 and j < n - 3:
        valid = True
        for k in range(1, 4):
            if data[i + k][j + k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    # Up-right
    if i >= 3 and j < n - 3:
        valid = True
        for k in range(1, 4):
            if data[i - k][j + k] == MAS[k]:
                continue
            else:
                valid = False
                break
        if valid:
            count += 1
    return count


def count_occurrences_2(i: int, j: int, data: list[list[str]], m: int, n: int):
    # There is an A at i, j
    if i >= 1 and j >= 1 and i < m - 1 and j < n - 1:
        tl = data[i - 1][j - 1]
        tr = data[i - 1][j + 1]
        bl = data[i + 1][j - 1]
        br = data[i + 1][j + 1]
        if tl == "M" and tr == "M" and bl == "S" and br == "S":
            return 1
        if tl == "S" and tr == "S" and bl == "M" and br == "M":
            return 1
        if tl == "S" and tr == "M" and bl == "S" and br == "M":
            return 1
        if tl == "M" and tr == "S" and bl == "M" and br == "S":
            return 1
    return 0


def puzzle01(data: list[list[str]], test: bool):
    print("Day 04 Puzzle 01")
    solution = 0

    m = len(data)
    n = len(data[0])
    for i in range(m):
        for j in range(n):
            if data[i][j] == "X":
                solution += count_occurrences(i, j, data, m, n)

    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 04 Puzzle 01 Done")


def puzzle02(data: list[list[str]], test: bool):
    print("Day 04 Puzzle 02")
    solution = 0

    m = len(data)
    n = len(data[0])
    for i in range(m):
        for j in range(n):
            if data[i][j] == "A":
                solution += count_occurrences_2(i, j, data, m, n)

    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 04 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()

    data = parse_data(data)

    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
