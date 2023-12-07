import unittest

from solution_day05_part_two import solve_part_two, parse_seed_range

class SolutionDay05PartTwo(unittest.TestCase):
    def test_should_parse_the_seeds(self):
        seeds = "seeds: 79 4 55 2"
        expected_seeds = [79, 80, 81, 82, 55, 56]
        actual_seeds = list(parse_seed_range(seeds))
        assert expected_seeds == actual_seeds

    def test_should_solve_the_problem(self):
        problem_input = [
            "seeds: 79 14 55 13\n",
            "\n",
            "seed-to-soil map:\n",
            "50 98 2\n",
            "52 50 48\n",
            "\n",
            "soil-to-fertilizer map:\n",
            "0 15 37\n",
            "37 52 2\n",
            "39 0 15\n",
            "\n",
            "fertilizer-to-water map:\n",
            "49 53 8\n",
            "0 11 42\n",
            "42 0 7\n",
            "57 7 4\n",
            "\n",
            "water-to-light map:\n",
            "88 18 7\n",
            "18 25 70\n",
            "\n",
            "light-to-temperature map:\n",
            "45 77 23\n",
            "81 45 19\n",
            "68 64 13\n",
            "\n",
            "temperature-to-humidity map:\n",
            "0 69 1\n",
            "1 0 69\n",
            "\n",
            "humidity-to-location map:\n",
            "60 56 37\n",
            "56 93 4\n",
        ]
        expected = 46
        actual = solve_part_two(problem_input)
        assert expected == actual
