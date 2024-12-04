# Advent of Code 2024
My solutions for the Advent of Code 2024. I only post these the day after the challenge was published.

You need to replace data.txt with the actual data for the challenge in each directory.

## Running the code

To set up the project and run the code using Poetry, follow these steps:

1. **Install Poetry**: If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

2. **Install Dependencies**: Navigate to the project directory and install the dependencies by running:
    ```bash
    poetry install
    ```

3. **Run the Code**: Use the following command to run the code with the specified day, puzzle, and run mode:
    ```bash
    poetry run python main.py --day <day> --puzzle <puzzle> --run <run>
    ```

Replace `<day>`, `<puzzle>`, and `<run>` with the appropriate values for the challenge you want to run. For example:

    ```bash
    poetry run python main.py --day 1 --puzzle 1 --run test
    ```