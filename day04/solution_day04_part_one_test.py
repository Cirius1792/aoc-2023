import unittest
from solution_day04 import parse_scratchcard, score, find_winning_numbers, solve


class SolutionDay04PartOneTest(unittest.TestCase):
    def test_should_parse_a_scratchcard(self):
        card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        card_id, your_numers, winning_numbers = (
            "1",
            set(["41", "48", "83", "86", "17"]),
            set(["83", "86", "6", "31", "17", "9", "48", "53"]),
        )
        actual_id, actual_numbers, actual_winning_numbers = parse_scratchcard(card)
        assert card_id == actual_id
        assert your_numers == actual_numbers
        assert winning_numbers == actual_winning_numbers

    def test_should_return_the_winning_numbers(self):
        your_numers = set(["41", "48", "83", "86", "17"])
        card_numbers = set(["83", "86", "6", "31", "17", "9", "48", "53"])

        expected_winning_numbers = set(["48", "83", "17", "86"])
        actual_winning_numbers = find_winning_numbers(your_numers, card_numbers)
        assert expected_winning_numbers == actual_winning_numbers

    def test_should_evaluate_the_score(self):
        winning_numbers = set(["48", "83", "17", "86"])
        expected_score = 8
        actual_score = score(winning_numbers)
        assert expected_score == actual_score

    def test_should_score_zero(self):
        winning_numbers = set()
        expected_score = 0
        actual_score = score(winning_numbers)
        assert expected_score == actual_score



    def test_should_solve_the_problem(self):
        problem_input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",
        ]
        expected_score = 13
        actual_score = solve(problem_input)
