import os

from advent2024.common.model import Base

test_solution_01 = 143
test_solution_02 = 123


class Input(Base):
    pass


def parse_data(data: str):
    rules = {}
    updates = []
    stage = "rules"
    for line in data.splitlines():
        if line == "":
            stage = "updates"
            continue
        if stage == "rules":
            pre, post = [int(x) for x in line.split("|")]
            if pre not in rules:
                rules[pre] = [post]
            else:
                rules[pre].append(post)
        else:
            updates.append([int(x) for x in line.split(",")])
    return rules, updates


def is_valid(rules: dict, update: list):
    for i, page in enumerate(update):
        if page in rules:
            for post in rules[page]:
                if post in update[:i]:
                    return False
    return True


def validate_and_reorder(rules: dict, update: list):
    changed = True
    while changed:
        changed = False
        # perform a single pass
        for i, page in enumerate(update):
            page_index = i
            if page in rules:
                for post in rules[page]:
                    if post in update[:i]:
                        # get the index of post in update
                        index = update.index(post)
                        # swap the elements
                        update[page_index], update[index] = (
                            update[index],
                            update[page_index],
                        )
                        page_index = index
                        changed = True
                        break
            if changed:
                break

    return update[len(update) // 2]


def puzzle01(rules: dict, updates: list, test: bool):
    print("Day 05 Puzzle 01")
    solution = 0
    for update in updates:
        if is_valid(rules, update):
            # find the middle element of update
            middle = len(update) // 2
            solution += update[middle]

    print("Solution:", solution)
    if test:
        assert solution == test_solution_01
    print("Day 05 Puzzle 01 Done")


def puzzle02(rules: dict, updates: list, test: bool):
    print("Day 05 Puzzle 02")
    solution = 0
    for update in updates:
        if not is_valid(rules, update):
            solution += validate_and_reorder(rules, update)
    print("Solution:", solution)
    if test:
        assert solution == test_solution_02
    print("Day 05 Puzzle 02 Done")


def run(input: Input):
    filename = "test.txt" if input.test else "data.txt"

    with open(os.path.join(os.path.dirname(__file__), filename), "r") as file:
        data = file.read()

    rules, updates = parse_data(data)

    if input.puzzle == 1:
        puzzle01(rules, updates, input.test)
    else:
        puzzle02(rules, updates, input.test)
