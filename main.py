import sys
from advent2024.day02 import day02
from advent2024.day01 import day01
from advent2024.day03 import day03
from advent2024.common.model import Base
import argparse


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code 2024 solutions.")
    parser.add_argument(
        "--day", type=int, required=True, help="Day of the challenge to run"
    )
    parser.add_argument(
        "--puzzle",
        type=int,
        required=True,
        choices=[1, 2],
        default=1,
        help="Puzzle number to run",
    )
    parser.add_argument(
        "--run",
        type=str,
        required=True,
        choices=["test", "real"],
        help="Run mode: 'test' or 'real'",
    )

    args = parser.parse_args()

    day = args.day
    puzzle = args.puzzle
    run_mode = args.run
    test_mode = True if run_mode == "test" else False

    match day:
        case 1:
            day01.day01(Base(test=test_mode, puzzle=puzzle))
        case 2:
            day02.day02(Base(test=test_mode, puzzle=puzzle))
        case 3:
            day03.day03(Base(test=test_mode, puzzle=puzzle))
        case _:
            print(f"Day {day} is not implemented yet.")


if __name__ == "__main__":
    main()
