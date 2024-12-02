import os

from advent2024.common.model import Base
from collections import Counter

test_solution_01 = 11
test_solution_02 = 31


class Input(Base):
    pass


def puzzle01(data: str, test: bool):
    print("Day 01 Puzzle 01")
    solution = 0
    left = []
    right = []
    for line in data.splitlines():
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    for i, j in zip(sorted_left, sorted_right):
        solution += abs(i - j)
    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 01 Puzzle 01 Done")


def puzzle02(data: str, test: bool):
    print("Day 01 Puzzle 02")
    solution = 0
    left = []
    right = []
    for line in data.splitlines():
        left.append(int(line.split("   ")[0]))
        right.append(int(line.split("   ")[1]))

    left_count = Counter(left)
    right_count = Counter(right)

    for key, value in left_count.items():
        solution += value * (key * right_count[key])
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 01 Puzzle 02 Done")


def day01(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()

    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
