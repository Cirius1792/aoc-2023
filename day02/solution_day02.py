from typing import List
from collections import namedtuple

Extraction = namedtuple("Extraction", "red green blue")


def print_game(game_id:int, games:List[Extraction], is_valid:bool):
    separator = "="*20
    print(separator)
    print(f"Game: {game_id} - {is_valid}")
    for game in games:
        print(game)
    print(separator)

def minimum_viable_game(extractions:List[Extraction]):
    red_max, green_max, blue_max = 0, 0, 0
    for extraction in extractions:
        red_max = extraction.red if extraction.red > red_max else red_max
        green_max = extraction.green if extraction.green > green_max else green_max
        blue_max = extraction.blue if extraction.blue > blue_max else blue_max
    return Extraction(red_max, green_max, blue_max)

def solve(line: str, request: str):
    def is_valid_game(actual: Extraction, target: Extraction) -> bool:
        return (
            actual.red <= target.red
            and actual.green <= target.green
            and actual.blue <= target.blue
        )

    game_id, extractions = parse_game(line)
    current_game = minimum_viable_game(extractions)
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


if __name__ == "__main__":
    request = "12 red, 13 green, 14 blue"
    with open("./day02/input.txt", "r") as reader:
        acc = 0
        for line in reader:
            id, outcome = solve(line, request)
            print(f"Game {id} - {outcome}")
            if outcome:
                acc += id
        print(f"result: {acc}")
