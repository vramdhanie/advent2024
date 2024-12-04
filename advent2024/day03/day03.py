import os

from advent2024.common.model import Base

import re
from functools import reduce

test_solution_01 = 322
test_solution_02 = 209


class Input(Base):
    pass


def process_string(data: str):
    print("Processing: ", data)
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = pattern.findall(data)

    return reduce(lambda acc, match: acc + int(match[0]) * int(match[1]), matches, 0)


def puzzle01(data: str, test: bool):
    print("Day 03 Puzzle 01")
    solution = 0

    solution = process_string(data)

    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 03 Puzzle 01 Done")


def puzzle02(data: str, test: bool):
    print("Day 03 Puzzle 02")
    solution = 0
    parts = data.split("don't()")

    solution = process_string(parts[0])
    for part in parts[1:]:
        do_index = part.find("do()")
        if do_index != -1:
            part = part[do_index + len("do()") :]
            solution += process_string(part)

    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 03 Puzzle 02 Done")


def day03(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()

    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
