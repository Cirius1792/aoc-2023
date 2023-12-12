import unittest

import numpy as np

from solution_day09_part_two import extrapolate_backward, solve


class SolutionDay09PartTwoTest(unittest.TestCase):
    def test_should_extrapolate_backward(self):
        vector = np.array([10, 13, 16, 21, 30, 45])
        expected_extrapolated_values = np.array([0, 2, -2, 5, 5][::-1])
        actual_extrapolated_values = extrapolate_backward(vector)
        assert (expected_extrapolated_values == actual_extrapolated_values).all()

    def test_should_solve_the_problem(self):
        problem_input = [
            "0 3 6 9 12 15\n",
            "1 3 6 10 15 21\n",
            "10 13 16 21 30 45\n",
        ]
        expected_solution = 2
        actual_solution = solve(problem_input)
        assert expected_solution == actual_solution
