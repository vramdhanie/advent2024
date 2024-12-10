from advent2024.day02 import day02
from advent2024.day01 import day01
from advent2024.day03 import day03
from advent2024.day04 import day04
from advent2024.day05 import day05
from advent2024.day06 import day06
from advent2024.day07 import day07
from advent2024.day08 import day08
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
            day01.run(Base(test=test_mode, puzzle=puzzle))
        case 2:
            day02.run(Base(test=test_mode, puzzle=puzzle))
        case 3:
            day03.run(Base(test=test_mode, puzzle=puzzle))
        case 4:
            day04.run(Base(test=test_mode, puzzle=puzzle))
        case 5:
            day05.run(Base(test=test_mode, puzzle=puzzle))
        case 6:
            day06.run(Base(test=test_mode, puzzle=puzzle))
        case 7:
            day07.run(Base(test=test_mode, puzzle=puzzle))
        case 8:
            day08.run(Base(test=test_mode, puzzle=puzzle))
        case _:
            print(f"Day {day} is not implemented yet.")


if __name__ == "__main__":
    main()
