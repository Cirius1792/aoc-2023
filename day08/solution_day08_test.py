import unittest
from solution_day08 import parse_network, navigate, solve

class SolutionDay08PartOneTest(unittest.TestCase):

    def test_should_parse_the_input_network(self):
        network_lines = [
                "AAA = (BBB, CCC)\n",
                "BBB = (DDD, EEE)\n",
                "CCC = (ZZZ, GGG)\n",
                "DDD = (DDD, DDD)\n",
                "EEE = (EEE, EEE)\n",
                "GGG = (GGG, GGG)\n",
                "ZZZ = (ZZZ, ZZZ)\n",
                ]
        expected_network = {
                "AAA": ["BBB", "CCC"],
                "BBB": ["DDD", "EEE"],
                "CCC": ["ZZZ", "GGG"],
                "DDD": ["DDD", "DDD"],
                "EEE": ["EEE", "EEE"],
                "GGG": ["GGG", "GGG"],
                "ZZZ": ["ZZZ", "ZZZ"],
                 }
        actual_network = parse_network(network_lines)
        assert expected_network == actual_network

    def test_should_navigate_the_network(self):
        network = {
                "AAA": ["BBB", "CCC"],
                "BBB": ["DDD", "EEE"],
                "CCC": ["ZZZ", "GGG"],
                 }
        current_node = "AAA"
        instruction = "L"
        expected_node = "BBB"
        actual_new_node = navigate(current_node, instruction, network)
        assert expected_node == actual_new_node

        instruction = "LR"
        expected_node = "EEE"
        actual_new_node = navigate(current_node, instruction, network)
        assert expected_node == actual_new_node

    def test_should_solve_the_problem(self):
        problem_input = [
                        "RL\n",
                        "\n",
                        "AAA = (BBB, CCC)\n",
                        "BBB = (DDD, EEE)\n",
                        "CCC = (ZZZ, GGG)\n",
                        "DDD = (DDD, DDD)\n",
                        "EEE = (EEE, EEE)\n",
                        "GGG = (GGG, GGG)\n",
                        "ZZZ = (ZZZ, ZZZ)\n",
                ]
        expected = 2
        actual = solve(problem_input)
        assert expected == actual

    def test_should_solve_the_problem_iterating_the_route(self):
        problem_input = [
                        "LLR\n",
                        "\n",
                        "AAA = (BBB, BBB)\n",
                        "BBB = (AAA, ZZZ)\n",
                        "ZZZ = (ZZZ, ZZZ)\n",
               ]
        expected = 6
        actual = solve(problem_input)
        assert expected == actual


 
        
