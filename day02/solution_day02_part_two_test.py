import unittest

from solution_day02 import Extraction, minimum_viable_game, parse_game
from solution_day02_part_two import solve

class SolutionPartTwoTest(unittest.TestCase):
#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    def test_game_1(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        _, game = parse_game(line)
        expected = Extraction(4, 2,6)
        actual = minimum_viable_game(game)
        assert actual == expected

    def test_game_2(self):
        line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        _, game = parse_game(line)
        expected = Extraction(1, 3,4)
        actual = minimum_viable_game(game)
        assert actual == expected

    def test_game_1_score(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        actual = solve(line)
        assert 48 == actual

    def test_game_2_score(self):
        line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        actual = solve(line)
        assert 12 == actual
