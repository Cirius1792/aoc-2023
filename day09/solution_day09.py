import numpy as np
from typing import List
from numba import jit, prange


def parse_line(input_line: str) -> np.ndarray:
    return np.array(list(map(int, input_line.split())), dtype=np.int32)


@jit(nopython=True)
def difference_vector(vector: np.ndarray) -> np.ndarray:
    return vector[1:] - vector[:-1]


@jit(nopython=True)
def extrapolate(vector: np.ndarray) -> np.ndarray:
    if not np.any(vector):
        return np.zeros(1, dtype=np.int32)
    difference = difference_vector(vector)
    extrapolated_vector = extrapolate(difference)
    extrapolated_value = np.array(
        [extrapolated_vector[-1] + vector[-1]], dtype=np.int32
    )
    return np.concatenate((extrapolated_vector, extrapolated_value))


def solve(problem_input: List[str]) -> int:
    acc = [0 for _ in range(len(problem_input))]
    for i, line in enumerate(problem_input):
        vector = parse_line(line)
        extrapolated_values = extrapolate(vector)
        # print(f"Line[{i}] - {extrapolated_values[-1]}")
        acc[i] = extrapolated_values[-1]
    return sum(acc)


if __name__ == "__main__":
    with open("./day09/input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")
