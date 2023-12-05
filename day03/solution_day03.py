from typing import List, Set, Tuple

DEBUG = False

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def filter_directions(column, row, n_columns, n_rows):
    for x, y in directions:
        if (
            row + x >= 0
            and row + x < n_rows
            and column + y >= 0
            and column + y < n_columns
        ):
            yield (row + x, column + y)


def find_numbers(problem: List[str]) -> Set[Tuple[int, int]]:
    n_rows, n_columns = len(problem), len(problem[0].strip())
    positions = set()
    for row in range(n_rows):
        for column in range(n_columns):
            if DEBUG:
                print(f"({row}-{column}) => {problem[row][column]}")
            if (
                not problem[row][column].isdigit() and problem[row][column] != "."
            ):  # I'm on a symbol!
                if DEBUG:
                    print(f"I'm a symbol -> {problem[row][column]}")
                for direction in filter_directions(column, row, n_columns, n_rows):
                    character = problem[direction[0]][direction[1]]
                    if character.isdigit():  # I've found a number near to a symbol!
                        if DEBUG:
                            print(
                                f"Found it! ({row}-{column}) => {problem[row][column]} for ({direction[0]}-{direction[1]}) => {character}"
                            )
                        positions.add(direction)
    return positions


def parse_number(line: str, x):
    i = x
    j = x - 1
    tmp = ""
    indexes = set()
    while i is not None or j is not None:
        if i is not None and (i > len(line) or not line[i].isdigit()):
            i = None
        if i is not None and i < len(line) and line[i].isdigit():
            tmp = tmp + line[i]
            indexes.add(i)
            i += 1
        if j is not None and (j < 0 or not line[j].isdigit()):
            j = None
        if j is not None and j >= 0 and line[j].isdigit():
            tmp = line[j] + tmp
            indexes.add(j)
            j -= 1
    return int(tmp), indexes


def retrieve_numbers(sample: List[str]) -> List[int]:
    numbers = []
    positions = find_numbers(sample)
    matched = set()
    for row, column in positions:
        if (row, column) not in matched:
            number, indexes = parse_number(sample[row], column)
            assert len(str(number)) == len(indexes)
            indexes = [(row, i) for i in indexes]
            if DEBUG: (f"{number} - {indexes}")
            numbers.append(number)
            for idx in indexes:
                matched.add(idx)
    return numbers


def solve(lines: List[str]) -> int:
    return sum(retrieve_numbers(lines))


if __name__ == "__main__":
    with open("./day03/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
