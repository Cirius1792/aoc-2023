import unittest

from typing import List, Tuple


def parse_input(input_lines: List[str]) -> List[Tuple[int, int]]:
    return []


class SolutionDay06PartOneTest(unittest.TestCase):
    def test_should_parse_the_input(self):
        input = [
            "Time:      7  15   30\n",
            "Distance:  9  40  200\n",
        ]
        expected = [(7, 9), (15, 40), (30, 200)]
        actual = parse_input(input)
        assert expected == actual
