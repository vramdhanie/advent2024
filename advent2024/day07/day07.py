import os

from advent2024.common.model import Base

test_solution_01 = 3749
test_solution_02 = 11387


class Input(Base):
    pass


def parse_data(data: str):
    return {
        int(line.split(":")[0].strip()): [
            int(num.strip()) for num in line.split(":")[1].strip().split()
        ]
        for line in data.splitlines()
    }


def puzzle01(data: dict, test: bool):
    print("Day 07 Puzzle 01")
    solution = 0
    for key, value in data.items():
        sums = [value[0]]
        max_len = 2 ** (len(value) - 1)
        for i in range(1, len(value)):
            for j in range(len(sums)):
                sums.append(sums[j] + value[i])
                sums.append(sums[j] * value[i])
        solution += key if key in sums[-max_len:] else 0
    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 07 Puzzle 01 Done")


def puzzle02(data: dict, test: bool):
    print("Day 07 Puzzle 02")
    solution = 0
    for key, value in data.items():
        sums = [value[0]]
        for i in range(1, len(value)):
            for j in range(len(sums)):
                sums.append(sums[j] + value[i])
                sums.append(sums[j] * value[i])
                sums.append(int(str(sums[j]) + str(value[i])))
            k = 3 ** (i - 1)  # Define the number of elements to remove
            sums = sums[k:]  # Remove the first k elements from the list
        solution += key if key in sums else 0
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 07 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()
    data = parse_data(data)
    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
