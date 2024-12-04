import os

from advent2024.common.model import Base

test_solution_01 = 2
test_solution_02 = 4


class Input(Base):
    pass


def read_data(filename: str):
    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()
    return [[int(x) for x in line.split(" ")] for line in data.splitlines()]


def is_safe(line: list[int], i: int):
    for j in range(i - 1, i + 1):
        new_line = line[:j] + line[j + 1 :]
        diff_line = new_line[0] - new_line[-1]
        asc = diff_line < 0

        safe = True
        for i in range(1, len(new_line)):
            diff = new_line[i - 1] - new_line[i]
            if diff == 0:
                safe = False
                break
            if abs(diff) > 3:
                safe = False
                break
            if (asc and diff > 0) or (not asc and diff < 0):
                safe = False
                break
        if safe:
            print("Safe", line, j)
            return True

    print("Not safe", line, j)
    return False


def puzzle01(data: list[list[int]], test: bool):
    print("Day 02 Puzzle 01")
    solution = 0
    # solution here
    for line in data:
        min = len(line) - 1
        max = len(line) * 3
        diff_line = line[0] - line[-1]
        asc = diff_line < 0
        safe = True
        if abs(diff_line) >= min and abs(diff_line) <= max:
            for i in range(1, len(line)):
                diff = line[i - 1] - line[i]
                if diff == 0:
                    safe = False
                    break
                if abs(diff) > 3:
                    safe = False
                    break
                if (asc and diff > 0) or (not asc and diff < 0):
                    safe = False
                    break
            if safe:
                solution += 1

    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 02 Puzzle 01 Done")


def puzzle02(data: list[list[int]], test: bool):
    print("Day 02 Puzzle 02")
    solution = 0
    # solution here
    for line in data:
        diff_line = line[0] - line[-1]
        asc = diff_line < 0

        safe = True
        for i in range(1, len(line)):
            diff = line[i - 1] - line[i]
            if diff == 0 or abs(diff) > 3:
                safe = False
            elif (asc and diff > 0) or (not asc and diff < 0):
                safe = False
            if not safe:
                safe = is_safe(line, i)
                break
        if safe:
            solution += 1
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 02 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    data = read_data(filename)

    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
