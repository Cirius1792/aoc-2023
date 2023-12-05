import unittest

from solution_day02 import solve, Extraction, parse_game, parse_request, parse_extractions

class Solution02Test(unittest.TestCase):
    request = "12 red, 13 green, 14 blue"

    def test_game_1_OK(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected_game_id, expected_outcome = 1, True
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_game_2_OK(self):
        line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        expected_game_id, expected_outcome = 2, True
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_game_3_KO(self):
        line = (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        expected_game_id, expected_outcome = 3, False
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_game_4_KO(self):
        line = (
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        expected_game_id, expected_outcome = 4, False
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_game_5_OK(self):
        line = (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        )
        expected_game_id, expected_outcome = 5, True
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_game_6_OK(self):
        line = (
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 11 red, 2 green"
        )
        expected_game_id, expected_outcome = 5, True
        actual_game_id, actual_outcome = solve(line, self.request)
        assert actual_game_id == expected_game_id
        assert actual_outcome == expected_outcome

    def test_parse_request(self):
        expected = Extraction(12, 13, 14)
        actual = parse_request(self.request)
        assert expected == actual

    def test_parse_game_one_extraction(self):
        line = "Game 1: 3 blue, 4 red"
        expected_game, expected_cubes = 1, [Extraction(4, 0, 3)]
        actual_game, actual_cubes = parse_game(line)
        assert expected_game == actual_game
        assert expected_cubes[0] == actual_cubes[0]

    def test_parse_game_three_extractions(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected_game, expected_cubes = 1, [
            Extraction(4, 0, 3),
            Extraction(1, 2, 6),
            Extraction(0, 2, 0),
        ]
        actual_game, actual_cubes = parse_game(line)
        assert expected_game == actual_game
        assert expected_cubes[0] == actual_cubes[0]

        assert expected_cubes[1] == actual_cubes[1]

        assert expected_cubes[2] == actual_cubes[2]


