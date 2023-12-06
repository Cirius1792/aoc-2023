from typing import List, Tuple
from solution_day03 import filter_directions, is_symbol, parse_number


def find_gears(problem: List[str]) -> List[Tuple[int, int]]:
    n_rows, n_columns = len(problem), len(problem[0].strip())
    gear_numbers = []
    for row in range(n_rows):
        for column in range(n_columns):
            if problem[row][column] == '*':  
                # I'm on a *
                position_of_surrounding_numbers = []
                surroinding_numbers = []
                for direction in filter_directions(column, row, n_columns, n_rows):
                    character = problem[direction[0]][direction[1]]
                    if character.isdigit():  # I've found a number near to a symbol!
                        position_of_surrounding_numbers.append(direction)
                already_parsed = set()
                for psn in position_of_surrounding_numbers:
                    # Let's parse the numbers that I've found
                    if psn in already_parsed:
                        # Some of the positions I checked before could be part of an already parsed number, so I don't have to check them again
                        continue
                    number, parsed_indexes = parse_number(problem[psn[0]], psn[1])
                    # Parse the number and add its coordinates to the set of the already parsed
                    surroinding_numbers.append(number)
                    for pi in parsed_indexes:
                        already_parsed.add((psn[0], pi))
                if len(surroinding_numbers) == 2:
                    gear_numbers.append(
                        (surroinding_numbers[0], surroinding_numbers[1])
                    )

    return gear_numbers


def solve(lines: List[str]) -> int:
    acc = 0
    for g1, g2 in find_gears(lines):
        acc += g1 * g2
    return acc

if __name__ == "__main__":
    with open("./day03/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
