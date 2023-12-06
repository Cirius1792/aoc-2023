import unittest
from solution_day03_part_two import solve, find_gears


class SolutionDay03Part2Test(unittest.TestCase):
    def test_example(self):
        sample = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        expected = 467835
        actual = solve(sample)
        assert expected == actual

    def test_find_a_gear(self):
        sample = ["......755.", "...$.*....", ".664.598.."]
        expected = [(755, 598)]
        actual = find_gears(sample)
        assert expected == actual
