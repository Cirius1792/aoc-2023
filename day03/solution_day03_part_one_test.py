import unittest

from solution_day03 import filter_directions, find_numbers, parse_number, retrieve_numbers, solve

class SolutionDay03Test(unittest.TestCase):
    def test_build_search_indexes_first_pos(self):
        n_rows, n_columns = 3, 3
        current_position = (0, 0)
        actual_directions = set(
            filter_directions(
                current_position[0], current_position[1], n_columns, n_rows
            )
        )
        assert set([(0, 1), (1, 1), (1, 0)]) == actual_directions

    def test_build_search_indexes_middle_grid(self):
        n_rows, n_columns = 3, 3
        current_position = (1, 1)
        expected_directions = set(
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 0), (2, 1), (2, 2)]
        )
        actual_directions = set(
            filter_directions(
                current_position[0], current_position[1], n_columns, n_rows
            )
        )
        assert expected_directions == actual_directions

    def test_find_number(self):
        sample = ["467.", "...*"]
        expected = set([(0, 2)])
        actual = find_numbers(sample)
        assert expected == actual
        sample = [
            "467..114..",
            "...*......",
            "..35..633.",
        ]
        expected = set([(0, 2), (2, 3), (2, 2)])
        actual = find_numbers(sample)
        assert expected == actual
        sample = [
            "288..20.$...",
            "......*.....",
            ".......1....",
        ]
        expected = set([(0, 5), (0, 6), (2, 7)])
        actual = find_numbers(sample)
        assert expected == actual


    def test_parse_number(self):
        line = "467..114.."
        expected_value, expected_indexes = 467, set([0, 1, 2])
        actual_value, actual_indexes = parse_number(line, 1)
        assert actual_value == expected_value
        assert actual_indexes == expected_indexes

    def test_parse_number_in_the_corner(self):
        line = "467..110.."
        expected_value, expected_indexes = 110, set([5, 6, 7])
        actual_value, actual_indexes = parse_number(line, 5)
        assert actual_value == expected_value
        assert actual_indexes == expected_indexes

        actual_value, actual_indexes = parse_number(line, 7)
        assert actual_value == expected_value
        assert actual_indexes == expected_indexes


    def test_retrieve_numbers(self):
        sample = ["467.", "...*"]
        expected = [467]
        actual = retrieve_numbers(sample)
        assert expected == actual
        sample = [
            "467..114..",
            "...*......",
            "..35..633.",
        ]
        expected = set([467, 35])
        actual = set(retrieve_numbers(sample))
        assert actual == expected

    def test_final(self):
        sample_input = [
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

        expected = 4361
        actual = solve(sample_input)
        assert expected == actual
 
