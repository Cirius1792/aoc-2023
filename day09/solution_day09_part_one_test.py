import unittest

import numpy as np

from solution_day09 import parse_line, difference_vector, extrapolate, solve


class SolutionDay09PartOneTest(unittest.TestCase):
    def test_should_parse_an_input_line(self):
        input_line = "1 3 6 10 15 21\n"
        expected_line = np.array([1, 3, 6, 10, 15, 21])
        actual_line = parse_line(input_line)
        assert (expected_line == actual_line).all()

    def test_should_create_the_difference_vector(self):
        vector = np.array([1, 3, 6, 10, 15, 21])
        expected_vector = np.array([2, 3, 4, 5, 6])
        actual_vector = difference_vector(vector)
        assert (expected_vector == actual_vector).all()

    def test_should_return_the_estrapolated_values(self):
        vector = np.array([1, 3, 6, 10, 15, 21])
        expected_extrapolated_values = np.array([0, 1, 7, 28])
        actual_extrapolated_values = extrapolate(vector)
        assert (expected_extrapolated_values == actual_extrapolated_values).all()

    def test_should_solve_the_problem(self):
        problem_input = [
            "0 3 6 9 12 15\n",
            "1 3 6 10 15 21\n",
            "10 13 16 21 30 45\n",
        ]
        expected_solution = 114
        actual_solution = solve(problem_input)
        assert expected_solution == actual_solution
