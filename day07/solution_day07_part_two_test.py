import unittest

from solution_day07 import Hand
from solution_day07_part_two import compare_hands_pt2, solve


class SolutionDay07PartTwo(unittest.TestCase):
    def test_should_compare_the_points_in_two_hands_considering_j(self):
        hand_1 = Hand("QQQJA", 1)
        hand_2 = Hand("T55J5", 1)
        assert compare_hands_pt2(hand_1, hand_2) > 0
        hand_3 = Hand("T55J5", 0)
        hand_4 = Hand("KTJJT", 483)
        assert compare_hands_pt2(hand_4, hand_3) > 0
        hand_3 = Hand("JJJJJ", 0)
        hand_4 = Hand("QQQQ2", 483)
        assert compare_hands_pt2(hand_4, hand_3) < 0


    def test_should_solve_part_two(self):
        input_lines = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483",
        ]
        expected = 5905
        actual = solve(input_lines)
        assert expected == actual
