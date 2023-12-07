import unittest

from solution_day04_part_two import find_won_cards, count_won_cards, count_score, solve

class SolutionDay04PartTwoTest(unittest.TestCase):
    def test_return_won_cards(self):
        winning_numbers = set([41, 48, 83, 86])
        card_id = 1
        expected_won_cards = [2, 3, 4, 5]
        won_cards = find_won_cards(card_id, winning_numbers)
        assert expected_won_cards == won_cards

    def test_winning_card_counter(self):
        problem_input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",
        ]
        expected_cards = {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
        actual_cards = count_won_cards(problem_input)
        assert expected_cards == actual_cards

    def test_eval_score(self):
        won_card_count = {1: 1, 2: 2, 3: 4, 4: 8, 5: 14, 6: 1}
        expected_score = 30
        actual_score = count_score(won_card_count)
        assert expected_score == actual_score

    def test_solve(self):
        problem_input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11\n",
        ]
        expected_score = 30
        actual_score = solve(problem_input)
        assert expected_score == actual_score


