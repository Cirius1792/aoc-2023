import numpy as np
from typing import List
from solution_day09 import difference_vector, parse_line


def extrapolate_backward(vector: np.ndarray) -> np.ndarray:
    if not np.any(vector):
        return np.zeros(1, dtype=np.int32)
    difference = difference_vector(vector)
    extrapolated_vector = extrapolate_backward(difference)
    extrapolated_value = np.array([vector[0] - extrapolated_vector[0]], dtype=np.int32)
    return np.concatenate((extrapolated_value, extrapolated_vector))


def solve(problem_input: List[str]) -> int:
    acc = [0 for _ in range(len(problem_input))]
    for i, line in enumerate(problem_input):
        vector = parse_line(line)
        extrapolated_values = extrapolate_backward(vector)
        # print(f"Line[{i}] - {extrapolated_values[0]}")
        acc[i] = extrapolated_values[0]
    return sum(acc)


if __name__ == "__main__":
    with open("./day09/input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")
