from typing import List
import unittest
from collections import namedtuple

Extraction = namedtuple("Extraction", "red green blue")


def print_game(game_id:int, games:List[Extraction], is_valid:bool):
    separator = "="*20
    print(separator)
    print(f"Game: {game_id} - {is_valid}")
    for game in games:
        print(game)
    print(separator)

def solve(line: str, request: str):
    def is_valid_game(actual: Extraction, target: Extraction) -> bool:
        return (
            actual.red <= target.red
            and actual.green <= target.green
            and actual.blue <= target.blue
        )

    red_max, green_max, blue_max = 0, 0, 0
    game_id, extractions = parse_game(line)
    for extraction in extractions:
        red_max = extraction.red if extraction.red > red_max else red_max
        green_max = extraction.green if extraction.green > green_max else green_max
        blue_max = extraction.blue if extraction.blue > blue_max else blue_max
    current_game = Extraction(red_max, green_max, blue_max)
    target_game = parse_request(request)
    is_valid = is_valid_game(current_game, target_game)
    print_game(game_id, extractions, is_valid)
    return game_id, is_valid


def parse_game(line: str):
    game_info, extraction_info = line.split(":")
    game_id = int(game_info.split(" ")[1])
    extractions = parse_extractions(extraction_info)
    return game_id, extractions


def parse_extractions(extractions: str):
    parsed_extractions = []
    for extraction in extractions.split(";"):
        parsed_extractions.append(parse_request(extraction.strip()))
    return parsed_extractions


def parse_request(line: str):
    R = "red"
    G = "green"
    B = "blue"
    parsed = {R: 0, G: 0, B: 0}
    for cubes in line.split(","):
        number, color = cubes.strip().split(" ")
        number = int(number)
        parsed[color.strip()] = number
    return Extraction(parsed[R], parsed[G], parsed[B])


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


if __name__ == "__main__":
    request = "12 red, 13 green, 14 blue"
    with open("./02/input.txt", "r") as reader:
        acc = 0
        for line in reader:
            id, outcome = solve(line, request)
            print(f"Game {id} - {outcome}")
            if outcome:
                acc += id
        print(f"result: {acc}")
