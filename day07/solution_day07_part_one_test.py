import unittest

from solution_day07 import Hand, parse_input, compare_hands, rank_hands, solve

class SolutionDay07PartOneTest(unittest.TestCase):
    def test_should_parse_the_input(self):
        input_lines = [
            "32T3K 765\n",
            "T55J5 684\n",
            "KK677 28\n",
            "KTJJT 220\n",
            "QQQJA 483\n",
        ]
        expected = [
            Hand("32T3K", 765),
            Hand("T55J5", 684),
            Hand("KK677", 28),
            Hand("KTJJT", 220),
            Hand("QQQJA", 483),
        ]
        actual = parse_input(input_lines)
        assert expected == actual

    def test_should_compare_the_points_in_two_hands(self):
        hand_1 = Hand("KK677", 1)
        hand_2 = Hand("KTJJT", 1)
        assert compare_hands(hand_1, hand_2) > 0
        hand_3 = Hand("T55J5", 0)
        hand_4 =Hand("QQQJA", 483) 
        assert compare_hands(hand_4, hand_3) > 0

    def test_should_rank_the_hands(self):
        input_hands = [
            Hand("32T3K", 765),
            Hand("T55J5", 684),
            Hand("KK677", 28),
            Hand("KTJJT", 220),
            Hand("QQQJA", 483),
        ]
        expected = [
            Hand("32T3K", 765),
            Hand("KTJJT", 220),
            Hand("KK677", 28),
            Hand("T55J5", 684),
            Hand("QQQJA", 483),
        ]
        actual = rank_hands(input_hands)
        print("Sorted:")
        print(list(map(lambda x:x.cards, actual)))
        assert expected == actual

    def test_should_score_the_solution(self):
        input_lines = [
            "32T3K 765\n",
            "T55J5 684\n",
            "KK677 28\n",
            "KTJJT 220\n",
            "QQQJA 483\n",
        ]
        expected = 6440
        actual = solve(input_lines)
        assert expected == actual
     
