import os

from advent2024.common.model import Base

test_solution_01 = 14
test_solution_02 = 34


class Input(Base):
    pass


def parse_data(data: str):
    return [list(line.strip()) for line in data.splitlines()]


def puzzle01(data: list[list[str]], test: bool):
    print("Day 08 Puzzle 01")
    solution = 0
    print("Solution:", solution)
    antennaes = {}
    n = len(data)
    m = len(data[0])
    for i in range(n):
        for j in range(m):
            if data[i][j] != ".":
                if data[i][j] not in antennaes:
                    antennaes[data[i][j]] = [(i, j)]
                else:
                    antennaes[data[i][j]].append((i, j))

    antinodes = set()
    for antenna in antennaes:
        for i in range(len(antennaes[antenna])):
            for j in range(i + 1, len(antennaes[antenna])):
                ax, ay = antennaes[antenna][i]
                bx, by = antennaes[antenna][j]
                dx = ax - bx
                dy = ay - by
                if dx < 0:
                    px = ax - abs(dx)
                    qx = bx + abs(dx)
                elif dx > 0:
                    px = ax + abs(dx)
                    qx = bx - abs(dx)
                else:
                    px = ax
                    qx = bx
                if dy < 0:
                    py = ay - abs(dy)
                    qy = by + abs(dy)
                elif dy > 0:
                    py = ay + abs(dy)
                    qy = by - abs(dy)
                else:
                    py = ay
                    qy = by
                if px >= 0 and px < n and py >= 0 and py < m:
                    antinodes.add((px, py))
                if qx >= 0 and qx < n and qy >= 0 and qy < m:
                    antinodes.add((qx, qy))

    solution = len(antinodes)
    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 08 Puzzle 01 Done")


def puzzle02(data: list[list[str]], test: bool):
    print("Day 08 Puzzle 02")
    solution = 0
    antennaes = {}
    n = len(data)
    m = len(data[0])
    for i in range(n):
        for j in range(m):
            if data[i][j] != ".":
                if data[i][j] not in antennaes:
                    antennaes[data[i][j]] = [(i, j)]
                else:
                    antennaes[data[i][j]].append((i, j))

    antinodes = set([x for antenna in antennaes.values() for x in antenna])
    for antenna in antennaes:
        for i in range(len(antennaes[antenna])):
            for j in range(i + 1, len(antennaes[antenna])):
                ax, ay = antennaes[antenna][i]
                bx, by = antennaes[antenna][j]
                dx = ax - bx
                dy = ay - by
                px = ax
                qx = bx
                py = ay
                qy = by
                while px >= 0 and px < n and py >= 0 and py < m:
                    if dx < 0:
                        px = px - abs(dx)
                    elif dx > 0:
                        px = px + abs(dx)
                    else:
                        px = px
                    if dy < 0:
                        py = py - abs(dy)
                    elif dy > 0:
                        py = py + abs(dy)
                    else:
                        py = py
                    if px >= 0 and px < n and py >= 0 and py < m:
                        antinodes.add((px, py))
                while qx >= 0 and qx < n and qy >= 0 and qy < m:
                    if dx < 0:
                        qx = qx + abs(dx)
                    elif dx > 0:
                        qx = qx - abs(dx)
                    else:
                        qx = qx
                    if dy < 0:
                        qy = qy + abs(dy)
                    elif dy > 0:
                        qy = qy - abs(dy)
                    else:
                        qy = qy
                    if qx >= 0 and qx < n and qy >= 0 and qy < m:
                        antinodes.add((qx, qy))

    solution = len(antinodes)
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 08 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()
    data = parse_data(data)
    if input.puzzle == 1:
        puzzle01(data, input.test)
    else:
        puzzle02(data, input.test)
