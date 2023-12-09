import unittest

from solution_day06 import solve, find_winning_tb, parse_input

class SolutionDay06PartOneTest(unittest.TestCase):
    def test_should_parse_the_input(self):
        input = [
            "Time:      7  15   30\n",
            "Distance:  9  40  200\n",
        ]
        expected = [(7, 9), (15, 40), (30, 200)]
        actual = parse_input(input)
        assert expected == actual

    def test_should_find_the_winning_tb_1(self):
        race = (7, 9)
        expected = [2, 3, 4, 5]
        actual = find_winning_tb(race)
        assert expected == actual

    def test_should_find_the_winning_tb_2(self):
        race = (15, 40)
        expected = [i for i in range(4, 12)]
        actual = find_winning_tb(race)
        assert expected == actual

    def test_should_find_the_winning_tb_3(self):
        race = (30, 200)
        expected = [i for i in range(11, 20)]
        actual = find_winning_tb(race)
        assert expected == actual

    def test_should_solve_the_problem(self): 
        problem_input = [
                    "Time:      7  15   30\n",
                    "Distance:  9  40  200\n",
                ]
        expected = 288
        actual = solve(problem_input)
        assert expected == actual
        
