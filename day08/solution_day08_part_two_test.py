import unittest
from solution_day08_part_two import find_starting_nodes, solve


class SolutionDay08PartTwoTest(unittest.TestCase):
    def test_shold_find_the_starting_nodes(self):
        network = {
            "AAA": ["BBB", "CCC"],
            "BBB": ["CCA", "EEE"],
            "CCA": ["ZZZ", "GGG"],
        }
        expected_starting_nodes = ["AAA", "CCA"]
        actual_starting_nodes = find_starting_nodes(network)
        assert expected_starting_nodes == actual_starting_nodes

    def test_should_solve_the_problem(self):
        problem_input = [
            "LR\n",
            "\n",
            "11A = (11B, XXX)\n",
            "11B = (XXX, 11Z)\n",
            "11Z = (11B, XXX)\n",
            "22A = (22B, XXX)\n",
            "22B = (22C, 22C)\n",
            "22C = (22Z, 22Z)\n",
            "22Z = (22B, 22B)\n",
            "XXX = (XXX, XXX)\n",
        ]
        expected = 6
        actual = solve(problem_input)
        assert expected == actual
